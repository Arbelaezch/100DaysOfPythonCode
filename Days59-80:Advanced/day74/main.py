from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv('Days59-80:Advanced/day74/TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Days59-80:Advanced/day74/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Days59-80:Advanced/day74/Daily Bitcoin Price.csv')
df_btc_price.dropna(inplace=True)

df_unemployment = pd.read_csv('Days59-80:Advanced/day74/UE Benefits Search vs UE Rate 2004-19.csv')

# Convert date strings to Datetime type.
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

# Resample data so that it is displayed monthly. 
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()

# ---------------------------------------------------------
# # Chart of Tesla Stock price vs Tesla search popularity.
# plt.figure(figsize=(14,7), dpi=120) 
# plt.title('Tesla Web Search vs Price', fontsize=18)

# # Increase the size and rotate the labels on the x-axis
# plt.xticks(fontsize=14, rotation=45)

# ax1 = plt.gca() # get current axis
# ax2 = ax1.twinx()
 
# ax1.set_ylabel('TSLA Stock Price', color='#E6232E') # can use a HEX code
# ax2.set_ylabel('Search Trend', color='skyblue') # or a named colour
 
# # Set the minimum and maximum values on the axes
# ax1.set_ylim([0, 600])
# ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

# ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
# ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)

# # Create locators for ticks on the time axis.
# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt = mdates.DateFormatter('%Y')

# # format the ticksax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)

# plt.show()
# # ---------------------------------------------------------
# # CHART OF BITCOIN PRICE VS SEARCH POPULARITY
# plt.figure(figsize=(14,7), dpi=120)
 
# plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
# plt.xticks(fontsize=14, rotation=45)
 
# ax1 = plt.gca()
# ax2 = ax1.twinx()
 
# ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# # Create locators for ticks on the time axis.
# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt = mdates.DateFormatter('%Y')
 
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
 
# ax1.set_ylim(bottom=0, top=15000)
# ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
 
# # Experiment with the linestyle and markers
# ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, 
#          color='#F08F2E', linewidth=3, linestyle='--')
# ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH, 
#          color='skyblue', linewidth=3, marker='o')
 
# plt.show()
# ---------------------------------------------------------
# # CHART OF UNEPLOYMENT RATE VS SEARCHES FOR UNEMPLOYMENT BENEFITS.

# # Create locators for ticks on the time axis.
# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt = mdates.DateFormatter('%Y')

# plt.figure(figsize=(14,7), dpi=120)
# plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=14, rotation=45)
 
# ax1 = plt.gca()
# ax2 = ax1.twinx()
 
# ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
 
# ax1.set_ylim(bottom=3, top=10.5)
# ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
 
# # Show the grid lines as dark grey lines
# ax1.grid(color='grey', linestyle='--')
 
# # Change the dataset used
# ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, 
#          color='purple', linewidth=3, linestyle='--')
# ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, 
#          color='skyblue', linewidth=3)
 
# plt.show()
# # ---------------------------------------------------------
# # ROLLING AVERAGE
# plt.figure(figsize=(14,8), dpi=120)
# plt.title('Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=14, rotation=45)
 
# ax1 = plt.gca()
# ax2 = ax1.twinx()

# # Create locators for ticks on the time axis.
# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt = mdates.DateFormatter('%Y')
 
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
 
# ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)
 
# ax1.set_ylim(bottom=3, top=10.5)
# ax1.set_xlim([df_unemployment.MONTH[0], df_unemployment.MONTH.max()])
 
# # Calculate the rolling average over a 6 month window
# roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
 
# ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, 'purple', linewidth=3, linestyle='-.')
# ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)
 
# plt.show()
# # ---------------------------------------------------------
# UE Benefits Search vs UE Rate 2004-20 (INCLUDES 2020)
df_ue_2020 = pd.read_csv('Days59-80:Advanced/day74/UE Benefits Search vs UE Rate 2004-20.csv')
df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)

plt.figure(figsize=(14,7), dpi=120)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)
 
ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])
 
ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, 'purple', linewidth=3)
ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)
 
plt.show()
