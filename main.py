import pandas as pd
import numpy as np
from datetime import datetime, timedelta
# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = 'updated_file.csv'
# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
# Initialize an empty dictionary to store results
result_dict = {}

# Calculate various statistical measures for all columns starting from the second column
for column_name in df.columns[1:]:
    column_data = df[column_name]

    # Calculate statistical measures
    column_max = np.max(column_data)
    column_min = np.min(column_data)
    column_range = column_max - column_min
    column_mean = np.mean(column_data)
    column_median = np.median(column_data)
    column_std = np.std(column_data)
    column_rms = np.sqrt(np.mean(column_data**2))
    column_mad = np.mean(np.abs(column_data - column_mean))
    column_iqr = np.percentile(column_data, 75) - np.percentile(column_data, 25)
    column_skewness = column_data.skew()
    column_kurtosis = column_data.kurtosis()

    # Store results in the dictionary
    result_dict[f"{column_name}_max"] = column_max
    result_dict[f"{column_name}_min"] = column_min
    result_dict[f"{column_name}_range"] = column_range
    result_dict[f"{column_name}_mean"] = column_mean
    result_dict[f"{column_name}_median"] = column_median
    result_dict[f"{column_name}_std"] = column_std
    result_dict[f"{column_name}_rms"] = column_rms
    result_dict[f"{column_name}_mad"] = column_mad
    result_dict[f"{column_name}_iqr"] = column_iqr
    result_dict[f"{column_name}_skewness"] = column_skewness
    result_dict[f"{column_name}_kurtosis"] = column_kurtosis


df['TIME_STAMP'] = pd.to_datetime(df['TIME_STAMP'], format='%H:%M:%S.%f')
total_execution_time = (df['TIME_STAMP'] - df['TIME_STAMP'].shift()).sum().total_seconds()
print(f"Total Execution Time: {total_execution_time} seconds")
result_dict["Execution_Time"] = total_execution_time

result_df = pd.DataFrame(list(result_dict.items()), columns=['Feature', 'Value'])
print(result_df)
