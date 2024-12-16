import openai
import pandas as pd
import fitz  # PyMuPDF
import re
import anthropic
from anthropic import HUMAN_PROMPT, AI_PROMPT
import os
import shutil
import json
import subprocess

class Signal:
    def __init__(self, var_name, acronym, signal_name, numer, denom, signal_type):
        self.var_name = var_name
        self.acronym = acronym
        self.signal_name = signal_name
        self.numer = numer
        self.denom = denom
        self.signal_type = signal_type

class LLMPaperGenerator:
    def __init__(self, base_dir, model='openai', llm_model='gpt-3.5-turbo', temperature=0.7, max_tokens=1024):
        # Model configuration
        self.model = model
        self.llm_model = llm_model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
        
        # Directory configuration
        self.base_dir = os.path.abspath(base_dir)
        self.pdfs_dir = os.path.join(self.base_dir, 'pdfs')
        
        # Create necessary directories
        os.makedirs(self.pdfs_dir, exist_ok=True)
        
        # Initialize API clients
        if self.model == 'openai':
            openai.api_key = self.openai_api_key
            
        # Load compustat dictionary
        dict_path = os.path.join(self.base_dir, 'compustat_variable_dictionary.csv')
        self.compustat_var_names = self.load_compustat_variable_dictionary(dict_path)

    def cleanup_latex_files(self, base_path, file_prefix):
        """Clean up auxiliary LaTeX files."""
        extensions = ['.aux', '.log', '.out', '.bbl', '.blg']
        for ext in extensions:
            file_path = os.path.join(base_path, f"{file_prefix}{ext}")
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    print(f"Removed {file_path}")
                except Exception as e:
                    print(f"Error removing {file_path}: {str(e)}")

    def compile_and_move_pdf(self, tex_file_path):
        """Compile LaTeX to PDF and handle file management."""
        tex_filename = os.path.basename(tex_file_path)
        tex_name = os.path.splitext(tex_filename)[0]
        
        # Store original directory
        original_dir = os.getcwd()
        os.chdir(self.base_dir)
        
        try:
            # Run pdflatex twice
            for _ in range(2):
                os.system(f'pdflatex -interaction=nonstopmode {tex_filename}')
            
            # Run bibtex if there's a .bib file
            bib_file = f"{tex_name}.bib"
            if os.path.exists(bib_file):
                os.system(f'bibtex {tex_name}')
                
                # Run pdflatex two more times
                for _ in range(2):
                    os.system(f'pdflatex -interaction=nonstopmode {tex_filename}')
            
            # Move PDF to pdfs directory if successful
            if os.path.exists(f"{tex_name}.pdf"):
                shutil.move(
                    os.path.join(self.base_dir, f"{tex_name}.pdf"),
                    os.path.join(self.pdfs_dir, f"{tex_name}.pdf")
                )
                print(f"PDF moved to: {os.path.join(self.pdfs_dir, tex_name)}.pdf")
                
                # Clean up auxiliary files
                self.cleanup_latex_files(self.base_dir, tex_name)
                return True
            else:
                print(f"Error: PDF not generated for {tex_name}")
                return False
                
        except Exception as e:
            print(f"Error during PDF compilation: {str(e)}")
            return False
            
        finally:
            os.chdir(original_dir)


    def process_version(self, signal, version, cleaned_text):
        """Process a single version of the paper."""
        # Create version-specific file names
        tex_file_name = f"{signal.var_name}_modified_v{version}"
        output_file_path = os.path.join(self.base_dir, f"{tex_file_name}.tex")
        pdf_file_path = os.path.join(self.pdfs_dir, f"{tex_file_name}.pdf")
        bib_file_name = tex_file_name

        # Check if PDF already exists
        if os.path.exists(pdf_file_path):
            print(f"PDF already exists for {tex_file_name}. Skipping processing...")
            return

        # Generate sections
        introduction_sections, bib_entries = self.generate_intro(signal.signal_name, cleaned_text)
        data_section = self.generate_data_section(signal.signal_name, signal.denom, signal.numer, signal.signal_type)
        abstract_text = self.extract_abstract(cleaned_text)
        conclusion = self.generate_conclusion(signal.signal_name, abstract_text)

        # Update bibliography reference
        versioned_text = cleaned_text.replace(
            f"\\bibliography{{{signal.var_name}}}", 
            f"\\bibliography{{{bib_file_name}}}"
        )

        # Export modified LaTeX
        self.export_modified_latex(
            original_latex=versioned_text,
            output_file_path=output_file_path,
            introduction_sections=introduction_sections,
            data_section=data_section,
            conclusion=conclusion
        )

        # Create bibliography entries
        if bib_entries:
            self.create_bib_entries(bib_entries, signal, version=version)
        else:
            print(f"No bib entries to add for version {version}.")

        # Compile PDF and clean up
        print(f"Compiling version {version} for {signal.var_name}...")
        self.compile_and_move_pdf(output_file_path)
        
        print(f"Completed processing version {version} for {signal.var_name}")

    @staticmethod
    def load_compustat_variable_dictionary(dictionary_file_path):
        compustat_var_names = pd.read_csv(dictionary_file_path)
        return pd.Series(compustat_var_names['shortername'].values, index=compustat_var_names['acronym']).to_dict()

    @staticmethod
    def clean_latex_title_page(text, varName, signalName, acronym):
        text = re.sub(r"\bThis report\b", "This paper", text)

        # Replace the title text before "and the Cross Section of Stock Returns"
        text = re.sub(
            r"(\\title\{.*?:\\\\)(.*?)( and the Cross Section of Stock Returns\})",
            rf"\1{signalName}\3",
            text,
            flags=re.DOTALL
        )

        pattern = r"(the asset pricing implications of )(.*?)(, and its robustness)"

        # Replace the identified text with "varName (acronym)"
        text = re.sub(pattern, rf"\1{signalName} ({acronym})\3", text)

        # Remove specific phrases as before
        text = text.replace("Online Appendix for Assaying Anomalies:\\\\", "")
        text = text.replace(" using the protocol proposed by Novy-Marx and Velikov (2023)", "")
        text = text.replace("\\vspace{\\baselineskip}{Robert Novy-Marx}\\and {Mihail Velikov}", "I. M. Harking")  # Remove Robert Novy-Marx and Mihail Velikov as authors

        # Pattern to match \includegraphics commands
        graphics_pattern = r'(\\includegraphics(?:\[[^\]]*\])?\{[^}]*\})'

        # Split the text into segments, separating \includegraphics commands
        segments = re.split(graphics_pattern, text)

        # Process segments: replace varName with signalName only in non-graphics segments
        for i in range(len(segments)):
            # If the segment is not an \includegraphics command (i.e., not matching the pattern)
            if not re.match(graphics_pattern, segments[i]):
                # Replace varName with signalName in this segment
                segments[i] = segments[i].replace(varName, acronym)

        # Rejoin the segments back into a single string
        new_text = ''.join(segments)

        # Replace bibliography reference
        new_text = new_text.replace("\\bibliography{newSignalTestBib}", f"\\bibliography{{{varName}}}")

        return new_text

    def generate_prompt(self, prompt_type, **kwargs):
        if prompt_type == 'introduction':
            main_prompt = f"""
            Write an introduction for a finance academic paper discussing the signal '{kwargs['signal_name']}' that predicts stock returns. Please follow these detailed guidelines:

            Structure and Style:
            1. Motivation (2 paragraphs, ~200 words total):
            - Open with a broad statement about market efficiency or asset pricing
            - Identify the specific gap or puzzle in the literature
            - Use active voice and declarative statements

            2. Hypothesis Development (3 paragraphs, ~300 words total):
            - Present economic mechanisms linking the signal to returns
            - Draw on established theoretical frameworks
            - Build logical arguments step by step
            - Support each claim with citations to foundational papers in LaTeX format, such as \\cite{{AuthorsYear}}

            3. Results Summary (3 paragraphs, ~300 words total):
            - Lead with the strongest statistical finding
            - Present results in order of importance
            - Use precise statistical language
            - Include economic significance
            - Mirror exactly the terminology used in the results section

            4. Contribution (3 paragraphs, ~300 words total):
            - Position relative to 3-4 most closely related papers
            - Cite papers from the following journals: Journal of Finance, Journal of Financial Economics, Review of Financial Studies, Journal of Accounting Research, Journal of Accounting and Economics
            - Highlight methodological innovations
            - Emphasize novel findings
            - End with broader implications

            Writing Guidelines:
            - Use active voice (e.g., "We find" instead of "It is found")
            - Maintain formal academic tone
            - Include 2-3 citations per paragraph on average in LaTeX format, e.g., \\cite{{AuthorsYear}}
            - Use \\citep{{AuthorsYear}} for parenthetical citations
            - Use present tense for established findings
            - Use past tense for your specific results
            - Avoid speculation beyond the data
            - Make clear distinctions between correlation and causation

            Base the results section strictly on the following data, matching its terminology and precision:
            {kwargs['modified_latex']}

            Please provide the introduction in JSON format inside <response></response> XML tags, with each section as separate keys, and include the BibTeX entries for all citations used:

            ```json
            {{
                "motivation": "Your motivation text here.",
                "hypothesis_development": "Your hypothesis development text here.",
                "results_summary": "Your results summary text here.",
                "contribution": "Your contribution text here.",
                "bib_entries": {{
                    "CitationKey1": "BibTeX entry for CitationKey1",
                    "CitationKey2": "BibTeX entry for CitationKey2",
                    ...
                }}
            }}
            """
            return main_prompt
        elif prompt_type == 'data':
            if kwargs['signal'] == 'ratio':
                prompt_data = f"""
                The data section should include a description of the construction of the signal, '{kwargs['signal_name']}', 
                which is constructed as the ratio of COMPUSTAT variable '{kwargs['numer']}' and COMPUSTAT variable '{kwargs['denom']}'.
                """
            elif kwargs['signal'] == 'diff':
                prompt_data = f"""
            The data section should include a description of the construction of the signal, '{kwargs['signal_name']}', 
            which is constructed as the difference of COMPUSTAT variable '{kwargs['numer']}' and its lag, scaled by lagged COMPUSTAT variable '{kwargs['denom']}'.
            """
            prompt_example = """
            The data section should be similar to this one:
            Our study investigates the predictive power of a financial signal 
            derived from accounting data for cross-sectional returns, focusing 
            specifically on the ratio of current assets to earnings before interest, 
            taxes, depreciation, and amortization (EBITDA). We obtain accounting and 
            financial data from COMPUSTAT, covering firm-level observations for 
            publicly traded companies. To construct our signal, we use COMPUSTAT’s 
            item ACT for current assets and item EBITDA for earnings. Current assets
            (ACT) represent the firm's short-term assets, which are expected to be 
            converted to cash or consumed within a year, including cash, receivables, 
            and inventories. EBITDA, on the other hand, provides a measure of core 
            operating performance by isolating operating income from non-operating 
            expenses and tax effects. 
            The construction of the signal follows a straightforward ratio format, 
            where we divide ACT by EBITDA for each firm in each year of our sample. 
            This ratio captures the relative scale of a firm's liquid or short-term 
            assets against its operational income, offering insight into how 
            efficiently the firm utilizes current assets to generate earnings. 
            By focusing on this relationship, the signal aims to reflect aspects of
            liquidity management and operational efficiency in a manner that is
            both scalable and interpretable. We construct this ratio using 
            end-of-fiscal-year values for both ACT and EBITDA to ensure consistency 
            and comparability across firms and over time.

            Please provide the data section in JSON format inside <response></response> XML tags:

            ```json
            {
                "data_section": "Your data section text here."
            }
            """
            return prompt_data + prompt_example
        elif prompt_type == 'conclusion':
            main_prompt = f"""
            Write a conclusion for a financial research paper analyzing the signal '{kwargs['signal_name']}' in predicting stock returns.
            Summarize the key findings of the analysis, discussing the significance of the signal in terms of predictive power and practical implications.
            Conclude with suggestions for future research and limitations of this study. The conclusion should be based on the following abstract:
            {kwargs['abstract_text']}

            Please provide the conclusion in JSON format inside <response></response> XML tags:

            ```json
            {{
                "conclusion": "Your conclusion text here."
            }}
            """
            return main_prompt

    def call_llm(self, prompt):
        if self.model == 'openai':
            response = openai.ChatCompletion.create(
                model=self.llm_model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            response_text = response['choices'][0]['message']['content'].strip()
        elif self.model == 'anthropic':
            # Adjust the code to use the Messages API
            client = anthropic.Client(api_key=self.anthropic_api_key)
            message = client.messages.create(
                model=self.llm_model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            # Assuming the response content is in message.content[0].text
            response_text = message.content[0].text.strip()
        else:
            raise ValueError(f"Unsupported model: {self.model}")
        return response_text


    def parse_llm_response(self, response_text):
        """
        Parse the LLM response text and extract JSON content with robust error handling.
        
        Args:
            response_text (str): Raw response text from the LLM
            
        Returns:
            dict: Parsed JSON response or None if parsing fails
        """
        def clean_json_string(json_str):
            """Clean and prepare JSON string for parsing."""
            # Remove any markdown code block markers
            json_str = re.sub(r'```json\s*|\s*```', '', json_str)
            
            # Fix common JSON formatting issues
            json_str = json_str.replace('\\"', '"')  # Fix escaped quotes
            json_str = json_str.replace('\\\\', '\\')  # Fix double escapes
            
            # Fix LaTeX-specific issues
            json_str = re.sub(r'\\([^\\])', r'\\\\\1', json_str)  # Escape single backslashes
            json_str = re.sub(r'\\\\([\\{}])', r'\\\1', json_str)  # Fix over-escaped special chars
            
            return json_str.strip()

        def extract_json_content(text):
            """Extract JSON content from various formats."""
            # Try different patterns to find JSON content
            patterns = [
                # XML tags
                r'<response>\s*(\{.*?\})\s*</response>',
                # Markdown code blocks
                r'```(?:json)?\s*(\{.*?\})\s*```',
                # Plain JSON object
                r'(\{(?:[^{}]|(?:\{[^{}]*\}))*\})',
                # JSON array
                r'(\[(?:[^\[\]]|(?:\[[^\[\]]*\]))*\])'
            ]
            
            for pattern in patterns:
                matches = re.finditer(pattern, text, re.DOTALL)
                for match in matches:
                    try:
                        json_str = clean_json_string(match.group(1))
                        return json.loads(json_str)
                    except json.JSONDecodeError:
                        continue
            
            return None

        def extract_sections_as_json(text):
            """Convert non-JSON formatted text into JSON structure."""
            # Try to extract sections if JSON parsing fails
            sections = {}
            
            # Look for common section patterns
            section_patterns = [
                # Key-value pairs separated by colons
                r'^([A-Za-z_]+):\s*(.+?)(?=(?:[A-Za-z_]+:|$))',
                # Markdown headers
                r'#{1,6}\s*([A-Za-z_]+)\s*\n(.*?)(?=(?:#{1,6}|$))',
                # LaTeX sections
                r'\\section\{([^}]+)\}\s*(.*?)(?=(?:\\section|$))'
            ]
            
            for pattern in section_patterns:
                matches = re.finditer(pattern, text, re.DOTALL | re.MULTILINE)
                for match in matches:
                    key = match.group(1).strip().lower().replace(' ', '_')
                    value = match.group(2).strip()
                    sections[key] = value
            
            return sections if sections else None

        try:
            # First attempt: Try to find and parse JSON content
            json_content = extract_json_content(response_text)
            if json_content:
                return json_content
            
            # Second attempt: Try to extract sections if no valid JSON found
            sections = extract_sections_as_json(response_text)
            if sections:
                return sections
            
            # Third attempt: If it's a single section response, return as is
            if 'data_section' in response_text.lower() or 'conclusion' in response_text.lower():
                return {"content": response_text.strip()}
            
            # Log failure if no parsing method succeeds
            print("Failed to parse response. Response text:")
            print(response_text[:500] + "..." if len(response_text) > 500 else response_text)
            return None
            
        except Exception as e:
            print(f"Error parsing LLM response: {str(e)}")
            print("Original response text:")
            print(response_text[:500] + "..." if len(response_text) > 500 else response_text)
            return None

    @staticmethod
    def fix_invalid_escape_sequences(json_str):
        # Replace unescaped backslashes with escaped backslashes
        # This regex replaces any backslash not followed by a valid escape character
        json_str_fixed = re.sub(
            r'\\(?![\\\"/bfnrtu])',
            r'\\\\',
            json_str
        )
        return json_str_fixed

    def generate_intro(self, signal_name, modified_latex):
        prompt = self.generate_prompt('introduction', signal_name=signal_name, modified_latex=modified_latex)
        response_text = self.call_llm(prompt)
        json_response = self.parse_llm_response(response_text)
        if json_response:
            introduction_sections = {
                "motivation": json_response.get("motivation", ""),
                "hypothesis_development": json_response.get("hypothesis_development", ""),
                "results_summary": json_response.get("results_summary", ""),
                "contribution": json_response.get("contribution", "")
            }
            bib_entries = json_response.get("bib_entries", {})
            return introduction_sections, bib_entries
        else:
            print("Failed to generate introduction.")
            return None, None

    def generate_data_section(self, signal_name, denom, numer, signal):
        prompt = self.generate_prompt('data', signal_name=signal_name, denom=denom, numer=numer, signal=signal)
        response_text = self.call_llm(prompt)
        json_response = self.parse_llm_response(response_text)
        if json_response and "data_section" in json_response:
            return json_response["data_section"]
        else:
            print("Failed to generate data section.")
            return None

    def generate_conclusion(self, signal_name, abstract_text):
        prompt = self.generate_prompt('conclusion', signal_name=signal_name, abstract_text=abstract_text)
        response_text = self.call_llm(prompt)
        json_response = self.parse_llm_response(response_text)
        if json_response and "conclusion" in json_response:
            return json_response["conclusion"]
        else:
            print("Failed to generate conclusion.")
            return None

    def replace_latex_introduction(self, text, introduction_sections):
        # Combine the sections into a single introduction text
        introduction_text = (
            f"{introduction_sections['motivation']}\n\n"
            f"{introduction_sections['hypothesis_development']}\n\n"
            f"{introduction_sections['results_summary']}\n\n"
            f"{introduction_sections['contribution']}\n\n"
        )

        # Replace % with \%
        introduction_text = introduction_text.replace('%', '\\%')
        
        # Replace $ with \$
        introduction_text = introduction_text.replace('$', '\\$')
        
        # Replace \\n\\n with \n\n
        introduction_text = introduction_text.replace('\\n\\n', '\n\n')        

        # Optional: clean up multiple spaces that might have been created
        #introduction_text = ' '.join(introduction_text.split())
        introduction_text = re.sub(r'[ ]{2,}', ' ', introduction_text)


        # Use re.escape to escape special characters in LaTeX commands
        intro_section_escaped = re.escape("\\section{Introduction}")
        next_section_escaped = re.escape("\\section{")

        # Build the pattern to match the Introduction section
        pattern = f"({intro_section_escaped})(.*?)(?={next_section_escaped})"

        # Define the replacement function
        def replacement_func(match):
            return match.group(1) + "\n\n" + introduction_text + "\n\n"

        # Perform the substitution using re.DOTALL to match across newlines
        modified_text = re.sub(pattern, replacement_func, text, flags=re.DOTALL)

        return modified_text

    def replace_latex_data_section(self, original_text, insert_text, section_title="\\section{Signal diagnostics}"):
        # Find the position of the section title
        section_index = original_text.find(section_title)

        if section_index == -1:
            print("Section title not found in the original text.")
            return original_text  # Return the original text if the section title isn't found

        # Insert the text before the section title
        modified_text = original_text[:section_index] + "\n\n" + "\\section{Data}\n\n" + insert_text + "\n" + original_text[section_index:]

        return modified_text

    def replace_latex_conclusion(self, text, new_conclusion):
        # Define the conclusion section content
        conclusion_section = f"\\section{{Conclusion}}\n\n{new_conclusion}\n\n"

        # Replace \\n\\n with \n\n
        conclusion_section = conclusion_section.replace('\\n\\n', '\n\n')        

        # Define the exact pattern to match "\newpage \clearpage \begin{figure}[!htbp]"
        pattern = r"\\newpage\s*\\clearpage\s*\\begin\{figure\}\[!htbp\]"
        match = re.search(pattern, text)
        if match:
            # Insert the conclusion right before the matched pattern
            start, end = match.span()  # Get the position of the match
            return text[:start] + conclusion_section + text[start:]
        else:
            # If the specified pattern is not found, add the conclusion at the end
            return text + conclusion_section

    def export_modified_latex(self, original_latex, output_file_path, introduction_sections=None, data_section=None, conclusion=None):
        modified_latex = original_latex
        if introduction_sections:
            modified_latex = self.replace_latex_introduction(modified_latex, introduction_sections)
        if data_section:
            modified_latex = self.replace_latex_data_section(modified_latex, data_section)
        if conclusion:
            modified_latex = self.replace_latex_conclusion(modified_latex, conclusion)

        with open(output_file_path, 'w') as file:
            file.write(modified_latex)

        print(f"Saved modified LaTeX file at {output_file_path}")

    def extract_abstract(self, latex_content):
        match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", latex_content, re.DOTALL)
        if match:
            abstract_text = match.group(1).strip()
            return abstract_text
        else:
            print("No abstract found in the document.")
            return None

    def extract_citations(self, text):
        # Extract all citation keys from the LaTeX text
        citations = re.findall(r'\\cite\{(.*?)\}', text)
        # Split multiple citations within the same \cite command
        citation_keys = []
        for citation in citations:
            keys = [key.strip() for key in citation.split(',')]
            citation_keys.extend(keys)
        return list(set(citation_keys))  # Return unique citation keys

    def create_bib_entries(self, bib_entries, signal, version=None):
        """Create bibliography entries with proper paths."""
        source_bib_path = os.path.join(self.base_dir, 'newSignalTestBib.bib')
        
        # Create version-specific bib filename if version is provided
        if version is not None:
            destination_bib_path = os.path.join(self.base_dir, f"{signal.var_name}_modified_v{version}.bib")
        else:
            destination_bib_path = os.path.join(self.base_dir, f"{signal.var_name}.bib")

        try:
            # Copy the original bib file to a new file based on the signal's variable name
            shutil.copy(source_bib_path, destination_bib_path)

            # Write the bib entries to the .bib file
            with open(destination_bib_path, 'a') as bib_file:
                for key, entry in bib_entries.items():
                    entry_fixed = entry.replace('\\n', '\n')
                    bib_file.write(entry_fixed + '\n')
            print(f"Appended {len(bib_entries)} bib entries to {destination_bib_path}")
        except FileNotFoundError:
            print(f"Source BibTeX file {source_bib_path} not found.")

