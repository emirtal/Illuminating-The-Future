import pandas as pd

# Read the Excel sheet into a DataFrame
df = pd.read_excel('/users/lynx/MGT6203/MGT_Project/2011_2014_format_B.xlsx')

# Convert the mixed date column to datetime format
df['Date Event Began2'] = pd.to_datetime(df['Date Event Began'])
df['Time Event Began2'] = pd.to_datetime(df['Time Event Began'])
df['Date of Restoration2'] = pd.to_datetime(df['Date of Restoration'])
df['Time of Restoration2'] = pd.to_datetime(df['Time of Restoration'])

# Split to date and time columns
df['Date Event Began2'] = pd.to_datetime(df['Date Event Began']).dt.date
df['Time Event Began2'] = pd.to_datetime(df['Time Event Began']).dt.time
df['Date of Restoration2'] = pd.to_datetime(df['Date of Restoration']).dt.date
df['Time of Restoration2'] = pd.to_datetime(df['Time of Restoration']).dt.time

# Remove the intermediate column
df.drop('Date Event Began', axis=1, inplace=True)
df.drop('Time Event Began', axis=1, inplace=True)
df.drop('Date of Restoration', axis=1, inplace=True)
df.drop('Time of Restoration', axis=1, inplace=True)

# rename columns
df = df.rename(columns={'Date Event Began2': 'Date Event Began', 'Time Event Began2':
    'Time Event Began', 'Date of Restoration2': 'Date of Restoration',
                        'Time of Restoration2': 'Time of Restoration'})

# Save the modified DataFrame back to Excel
df.to_excel('/users/lynx/MGT6203/MGT_Project/Cleaned_datesB.xlsx', index=False)

print('Done!')
