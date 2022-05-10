import pandas as pd


# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format


df_apps = pd.read_csv('Days59-80:Advanced/day75/apps.csv')