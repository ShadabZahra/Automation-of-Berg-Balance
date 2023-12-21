import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = 'Patient001_Task04_unfiltered.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
acceleration_columns = df.columns[162:198]
print(acceleration_columns)
# Initialize an empty dictionary to store results
result_dict = {}

# Calculate mean and standard deviation for all columns starting from the second column
for column_name in df.columns[1:]:
    column_mean = df[column_name].mean()
    column_std = df[column_name].std()

    # Store results in the dictionary
    result_dict[f"{column_name}_mean"] = column_mean
    result_dict[f"{column_name}_std"] = column_std

# Create a DataFrame from the dictionary
result_df = pd.DataFrame(list(result_dict.items()), columns=['Feature', 'Value'])

# Print or display the DataFrame
print(result_df)
