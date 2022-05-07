import pandas as pd
from bs4 import BeautifulSoup
from requests import request
import requests

html_doc = requests.get('https://payscale.com/college-salary-report/majors-that-pay-you-back/bachelors')

soup = BeautifulSoup(requests.get('https://payscale.com/college-salary-report/majors-that-pay-you-back/bachelors').content, "html.parser")
table = soup.find("table")

# data_file = 'Days59-80:Advanced/day71/salaries_by_college_major.csv'

# df = pd.read_csv(table)
# clean_df = df.dropna()
# pd.options.display.float_format = '${:,.2f}'.format 

# print(table.getText())




