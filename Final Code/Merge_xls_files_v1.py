#import pip
#pip.main(['install', 'openpyxl'])

import pandas as pd
import os

''' Merge multiple excel sheets into one master using pandas'''

# Directories
directories = {
    "Directory_A": '/users/lynx/MGT6203/MGT_Project/Outagedata/Format_A',
    "Directory_B": '/users/lynx/MGT6203/MGT_Project/Outagedata/Format_B',
    "Directory_C": '/users/lynx/MGT6203/MGT_Project/Outagedata/Format_C'
}

# Loop over directories
for directory_key, directory_path in directories.items():
    # Initialize an empty DataFrame to store the merged data
    merged_df = pd.DataFrame()

    # Loop over files in the directory
    for file in os.listdir(directory_path):
        if file.endswith('.xls') or file.endswith('.xlsx'):
            file_path = os.path.join(directory_path, file)
            df = pd.read_excel(file_path)

            # Append to master DataFrame
            merged_df = merged_df.append(df, ignore_index=True)

    # Create a new Excel file with the merged data for the current directory
    output_path = f'/users/lynx/MGT6203/MGT_Project/df_{directory_key}.xlsx'
    merged_df.to_excel(output_path, index=True)

    # Print completion message for the current directory
    print(f'Merged data for {directory_key} saved to {output_path}')

print('Done!')