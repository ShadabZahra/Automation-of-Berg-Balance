import pandas as pd
import numpy as np

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = 'Patient001_Task04_unfiltered.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Columns containing acceleration data
acceleration_columns = df.columns[162:198]

for i in range(0, len(acceleration_columns), 3):
    group_columns = acceleration_columns[i:i+3]
    sma_values = []
    for j in range(0, len(df)):
        window_data = df.loc[j, group_columns]
        sma = np.sum(np.abs(window_data))
        sma_values.append(sma)
    # Extract coordinate name and create new column names
    coordinate_name = group_columns[0].split('_')[0]+'_'+group_columns[0].split('_')[1]
    sma_col_name = f"{coordinate_name}"
    df[f"{sma_col_name}_SMA"] = sma_values

print(list(df.columns))
output_csv_path = 'updated_file.csv'
df.to_csv(output_csv_path, index=False)
print(f"SMA values added to {output_csv_path}")



print(df.head())
# # Save the updated DataFrame to a new CSV file
# output_csv_path = 'your_updated_file.csv'
# df.to_csv(output_csv_path, index=False)
#
# print(f"SMA values added to {output_csv_path}")
