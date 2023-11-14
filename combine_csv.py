import os
import pandas as pd

# Set the path to the folder containing your CSV files
folder_path = 'Data/'

# Get a list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()
dfs = []

for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate all DataFrames in the list into one
combined_data = pd.concat(dfs, ignore_index=True)

#Dictionary mapping values in the 'gender' column to new values
mapping = {0: 'Unknown', 1: 'Male', 2: 'Female'}

# Use the 'map' method to change the values in the 'gender' column
combined_data['gender'] = combined_data['gender'].map(mapping)

# Save the combined DataFrame to a new CSV file
combined_data.to_csv('Data/CombinedCSV.csv', index=False)
