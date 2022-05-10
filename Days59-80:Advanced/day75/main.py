# Data analyzes the Android App store for various data.

import pandas as pd
import plotly.express as px


# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format


df_apps = pd.read_csv('Days59-80:Advanced/day75/apps.csv')

# Drop unused columns and remove NaN values
df_apps_clean = df_apps.dropna()

# Find and remove duplicates
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
df_apps_clean[df_apps_clean.App == 'Instagram']
print(df_apps_clean.shape)