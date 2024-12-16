import openai
import pandas as pd
import re
import os

# Load your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load the dictionary of COMPUSTAT variable acronyms and their full names
dictionary_file_path = 'compustat_variable_dictionary.csv'
compustat_var_names_df = pd.read_csv(dictionary_file_path)

# Convert the dictionary DataFrame into a dictionary for easy lookup
compustat_var_names = pd.Series(compustat_var_names_df.shortername.values, index=compustat_var_names_df.acronym).to_dict()

# Read the CSV file with signals into a pandas DataFrame
file_path = 'signals.csv'
signals_df = pd.read_csv(file_path)

# Function to map the acronyms to full COMPUSTAT variable names
def get_full_var_name(acronym):
    return compustat_var_names.get(acronym, acronym)  # Return the acronym if not found in dictionary

def extract_name_and_acronym(text):
    """
    Extracts the name and acronym from a given text.

    Parameters:
        text (str): The input string containing 'Name: ...' and 'Acronym: ...'.

    Returns:
        tuple: A tuple containing the name and acronym as strings.
    """
    import re

    # Use regular expressions to find the name and acronym
    name_match = re.search(r'Name:\s*(.*)', text)
    acronym_match = re.search(r'Acronym:\s*(.*)', text)

    # Extract the matched groups if they exist
    name = name_match.group(1).strip() if name_match else ''
    acronym = acronym_match.group(1).strip() if acronym_match else ''

    return name, acronym


# Function to generate a signal name using OpenAI's API
def generate_signal_name(numer, denom, signal_type, varName):
    # Convert acronyms to full variable names
    numer_full = get_full_var_name(numer)
    denom_full = get_full_var_name(denom)
    
    # Determine if the signal is negative based on the varName
    is_negative = varName.startswith("NEG")
    
    # Formulate the request prompt
    prompt = f"Create a descriptive and short name, as well as an acronym for a financial signal where the signal type is '{signal_type}'. Avoid using the words ratio and difference in the name. The acronym should only include capital letters."
    if signal_type == 'ratio':
        prompt += f"It is the ratio of '{numer_full}' to '{denom_full}'."
    elif signal_type == 'diff':
        prompt += f"It is the difference in '{numer_full}' scaled by '{denom_full}'."
    
    # Add information about negation
    if is_negative:
        prompt += " The signal should be the negative of the computed value."

    # Call OpenAI's Chat API to generate the signal name
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates descriptive signal names for financial ratios."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50  # Adjust token limit based on expected response length
    )
    
    # Separate the signal name and acronym


    # Extract the generated signal name from the response
    signal_output = response['choices'][0]['message']['content'].strip()
    signal_name, acronym = extract_name_and_acronym(signal_output)

    return signal_name, acronym

# Loop through each signal and generate a name, limited to 5 iterations for testing
for index, row in signals_df.iterrows():
    numer = row['numer']
    denom = row['denom']
    signal_type = row['signal']
    varName = row['varName']
    
    # Generate the signal name
    signal_name, acronym = generate_signal_name(numer, denom, signal_type, varName)
    
    # Add the generated signal name to the DataFrame (you can create a new column)
    signals_df.loc[index, 'signal_name'] = signal_name
    signals_df.loc[index, 'acronym'] = acronym

    # Optionally print the generated signal name
    print(f"Generated signal name for {numer}/{denom} ({signal_type}): {signal_name}")


signals_df.to_csv('signals_df.csv', index=False)
