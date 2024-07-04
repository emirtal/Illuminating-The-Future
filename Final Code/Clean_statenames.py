import pandas as pd

''' Part 1 of this code will parse the dirty location data. From there it will look for state names both in full
name format and in two letter abbreviation. The second part of the code will expand the data since some entries
 have multiple states listed under one row. Now each state will have its own row with the same data that corresponds
 to that state. Part 3 of the code will then take those states and classify them into regions'''

# Read the XLSX file into a pandas DataFrame
df = pd.read_excel('/users/lynx/MGT6203/MGT_Project/Outage data/Complied_clean_outage_data_v1.xlsx')

# List of state names and abbreviations
state_names = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
               'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
               'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
               'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
               'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Puerto Rico',
               'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming',
               'PR', 'AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL',
               'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ',
               'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT', 'VA', 'VI', 'VT', 'WA',
               'WI', 'WV', 'WY']


# Function to extract state names from a string
def extract_state_names(text):
    extracted_states = []
    for state in state_names:
        if state in text:
            extracted_states.append(state)

    return extracted_states


# Create a new column containing the extracted state names
df['Extracted_States'] = df['Area Affected'].apply(lambda x: extract_state_names(str(x)))

# part 2

# Create a new DataFrame for the exploded rows
df_exploded = df.explode('Extracted_States').reset_index(drop=True)

# Drop rows with empty 'Extracted_States'
df_exploded = df_exploded.dropna(subset=['Extracted_States'])

# part 3
# Mapping of state abbreviations to full names
state_abbv = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    "DC": "Washington DC",
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
    "MP": "Northern Mariana Islands"
}

# Function to convert state abbreviations to full names
def convert_abbreviations(state):
    if len(state) == 2 and state.upper() in state_names:
        return state_abbv[state.upper()]
    return state

# Apply the conversion function to the "Extracted_States" column
df_exploded['Extracted_States'] = df_exploded['Extracted_States'].apply(convert_abbreviations)

# rename column
df_exploded = df_exploded.rename(columns={'Extracted_States': 'Affected State'})

# Save to a new XLSX file
df_exploded.to_excel('/users/lynx/MGT6203/MGT_Project/Outage data/Complied_clean_outage_data_v2.xlsx', index=True)

print('Done!')