from models import Signal, LLMPaperGenerator
import pandas as pd
import os

# Configuration
BASE_DIR = "./tex"  # Base directory containing .tex files and other resources
N_SIGNALS = 96  # Number of signals to use
N_VERSIONS = 3  # Number of versions to generate

if __name__ == "__main__":
    # Setup paths
    signals_df_path = os.path.join(BASE_DIR, "signals_df.csv")
    dict_path = os.path.join(BASE_DIR, "compustat_variable_dictionary.csv")
    
    # Call the generator class with base directory
    generator = LLMPaperGenerator(
        base_dir=BASE_DIR,
        model='anthropic', 
        llm_model='claude-3-5-sonnet-latest', 
        temperature=0.2, 
        max_tokens=8192
    )     
    
    # Load the signals dataframe
    signals_df = pd.read_csv(signals_df_path)

    # Loop through the signals dataframe
    for index, row in signals_df.iloc[1:N_SIGNALS].iterrows():
        signal = Signal(
            var_name=row['varName'],
            acronym=row['acronym'],
            signal_name=row['signal_name'],
            numer=row['numer'],
            denom=row['denom'],
            signal_type=row['signal']
        )

        try:
            tex_file_path = os.path.join(BASE_DIR, f"{signal.var_name}.tex")
            with open(tex_file_path, 'r') as file:
                latex_text = file.read()
        except FileNotFoundError:
            print(f"File {tex_file_path} not found.")
            continue

        cleaned_text = generator.clean_latex_title_page(latex_text, signal.var_name, signal.signal_name, signal.acronym)
        
        # Generate versions
        for version in range(1, N_VERSIONS + 1):
            generator.process_version(signal, version, cleaned_text)