import pandas as pd

# Read the Excel sheet into a DataFrame
df = pd.read_excel('/users/lynx/MGT6203/MGT_Project/2002_2010_format_A.xlsx')

# Convert the mixed date column to datetime format
df['Restoration datetime'] = pd.to_datetime(df['Restoration'])
df['Date Event Began'] = pd.to_datetime(df['Date'])
df['Time Event Began'] = pd.to_datetime(df['Time'].astype(str))

# Split to date and time columns
df['Date of Restoration'] = pd.to_datetime(df['Restoration datetime']).dt.date
df['Time of Restoration'] = pd.to_datetime(df['Restoration datetime']).dt.time
df['Date Event Began'] = pd.to_datetime(df['Date']).dt.date
df['Time Event Began'] = pd.to_datetime(df['Time']).dt.time

# Remove the intermediate column
df.drop('Restoration datetime', axis=1, inplace=True)
df.drop('Restoration', axis=1, inplace=True)
df.drop('Date', axis=1, inplace=True)
df.drop('Time', axis=1, inplace=True)

#Save the modified DataFrame back to Excel
df.to_excel('/users/lynx/MGT6203/MGT_Project/Cleaned_datesA.xlsx', index=False)

print('Done!')