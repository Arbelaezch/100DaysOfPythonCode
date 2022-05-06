import pandas as pd

data_file = 'Days59-80:Advanced/day71/salaries_by_college_major.csv'

df = pd.read_csv(data_file)
clean_df = df.dropna()