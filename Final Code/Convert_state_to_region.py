import pandas as pd

# Read the XLSX file into a pandas DataFrame
df = pd.read_excel('/users/lynx/MGT6203/MGT_Project/Outage data/Complied_clean_outage_data_v2.xlsx')

# Mapping of states to regions
state_regions = {
    'Alabama': 'Southeast',
    'Alaska': 'West',
    'Arizona': 'Southwest',
    'Arkansas': 'South',
    'California': 'West',
    'Colorado': 'West',
    'Connecticut': 'Northeast',
    'Delaware': 'Northeast',
    'Florida': 'Southeast',
    'Georgia': 'Southeast',
    'Hawaii': 'West',
    'Idaho': 'West',
    'Illinois': 'Midwest',
    'Indiana': 'Midwest',
    'Iowa': 'Midwest',
    'Kansas': 'Midwest',
    'Kentucky': 'Southeast',
    'Louisiana': 'South',
    'Maine': 'Northeast',
    'Maryland': 'Northeast',
    'Massachusetts': 'Northeast',
    'Michigan': 'Midwest',
    'Minnesota': 'Midwest',
    'Mississippi': 'Southeast',
    'Missouri': 'Midwest',
    'Montana': 'West',
    'Nebraska': 'Midwest',
    'Nevada': 'West',
    'New Hampshire': 'Northeast',
    'New Jersey': 'Northeast',
    'New Mexico': 'Southwest',
    'New York': 'Northeast',
    'North Carolina': 'Southeast',
    'North Dakota': 'Midwest',
    'Ohio': 'Midwest',
    'Oklahoma': 'South',
    'Oregon': 'West',
    'Pennsylvania': 'Northeast',
    'Rhode Island': 'Northeast',
    'South Carolina': 'Southeast',
    'South Dakota': 'Midwest',
    'Tennessee': 'Southeast',
    'Texas': 'South',
    'Utah': 'West',
    'Vermont': 'Northeast',
    'Virginia': 'Southeast',
    'Washington': 'West',
    'West Virginia': 'Southeast',
    'Wisconsin': 'Midwest',
    'Wyoming': 'West'
}

# Function to classify states into regions
def classify_region(state):
    return state_regions.get(state, 'Other')

# Create a new column with the region for each state
df['Region'] = df['Affected State'].apply(classify_region)

# Save to a new XLSX file
df.to_excel('/users/lynx/MGT6203/MGT_Project/Outage data/Complied_clean_outage_data_v3.xlsx', index=False)

print('Done!')