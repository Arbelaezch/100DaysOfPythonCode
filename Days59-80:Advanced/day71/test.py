import pandas as pd

data_file = 'Days59-80:Advanced/day71/salaries_by_college_major.csv'

df = pd.read_csv(data_file)
clean_df = df.dropna()
pd.options.display.float_format = '${:,.2f}'.format 

# # Finds the id of the row with the max value in the given column.
# clean_df['Starting Median Salary'].idxmax()

# # Finds the value of the given column of the given row.
# clean_df['Undergraduate Major'].loc[43]
# clean_df['Undergraduate Major'][43]

# # Highest mid career salary
# print(clean_df['Mid-Career Median Salary'].max())
# print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
# print(f"Highest Mid-Career Salary: {clean_df['Undergraduate Major'][8]}")

# # Lowest Mid Career Salary
# print(clean_df['Starting Median Salary'].min())
# print(clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()])

# # Find the difference between two columns for every row, and add that data as a new column to the dataframe.
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
# print(clean_df.head())

# Sort by descending order for a given column
# low_risk = clean_df.sort_values('Spread', ascending=False)
# print(low_risk[['Undergraduate Major', 'Spread']].head())

# # Sort by descending by a columns
# print(clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False).head())

# # Group by column and count
# print(clean_df.groupby('Group').count())
# # Group by column and mean
print(clean_df.groupby('Group').mean())