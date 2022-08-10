import pandas as pd
from bs4 import BeautifulSoup
from requests import request
import requests

# Playing around with some CSV data using Pandas.

data = pd.read_csv('Days59-80:Advanced/day71/salaries_by_college_major.csv')

# print(data.head())
# print(data.shape)
# print(data.columns)

# print(data.isna())

clean_data = data.dropna()

# print(clean_data.tail())

# print(clean_data.head())


# Find the major with the highest starting salary.
# My solution:
# print(clean_data.sort_values('Starting Median Salary', ascending=False).head(1)['Undergraduate Major'])


# Subtract columns and insert new column 
# spread_col = clean_data['Mid-Career 90th Percentile Salary'] - clean_data['Mid-Career 10th Percentile Salary']
# clean_data.insert(1, 'Spread', spread_col)
# print(clean_data.head())

# Group By
# print(clean_data.groupby('Group').count())
































# html_doc = requests.get('https://payscale.com/college-salary-report/majors-that-pay-you-back/bachelors')

# soup = BeautifulSoup(requests.get('https://payscale.com/college-salary-report/majors-that-pay-you-back/bachelors').content, "html.parser")
# table = soup.find("table")

# data_file = 'Days59-80:Advanced/day71/salaries_by_college_major.csv'

# df = pd.read_csv(table)
# clean_data = df.dropna()
# pd.options.display.float_format = '${:,.2f}'.format 

# print(table.getText())




