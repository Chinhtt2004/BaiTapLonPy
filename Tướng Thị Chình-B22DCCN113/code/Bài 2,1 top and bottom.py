
import pandas as pd

# Load the provided CSV file to examine its structure and prepare for further processing
file_path = 'results.csv'
df = pd.read_csv(file_path)

# Display the first few rows and column information to understand the data
# Filter columns that have numerical data types (float64 or int64) for processing
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Prepare to store results for top and bottom 3 players in each metric
top_bottom_results = []

# Loop through each numerical column to find the top and bottom 3 players
for col in numerical_columns:
    # Sort the data in descending order for top 3 and ascending order for bottom 3
    top_3 = df.nlargest(3, col)[['Name', col]]
    bottom_3 = df.nsmallest(3, col)[['Name', col]]
    
    # Append results with metric name, top 3, and bottom 3
    for i, row in top_3.iterrows():
        top_bottom_results.append([col, 'Top', row['Name'], row[col]])
    for i, row in bottom_3.iterrows():
        top_bottom_results.append([col, 'Bottom', row['Name'], row[col]])

# Convert results to a DataFrame for saving
result_df = pd.DataFrame(top_bottom_results, columns=['Metric', 'Category', 'Player', 'Value'])
print(result_df)
# Save the result to 'result1.csv'
result_file_path = 'result1.csv'
result_df.to_csv(result_file_path, index=False)

# Return the path for user to download the file
result_file_path
