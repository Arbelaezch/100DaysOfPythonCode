from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

color_data = "Days59-80:Advanced/day73/data/colors.csv"
sets_data = "Days59-80:Advanced/day73/data/sets.csv"
themes_data = "Days59-80:Advanced/day73/data/themes.csv"




color_df = pd.read_csv(color_data)

sets_df = pd.read_csv(sets_data)

themes_df = pd.read_csv(themes_data)


# color_df.columns = ['DATE', 'TAG', 'POSTS']

# # Count number of transparent and non-transparent colors.
# print(color_df["is_trans"].value_counts())

# # Finds number of unique colors.
# print(color_df['name'].nunique())

# # Finds the earliest released sets
# print(sets_df[sets_df['year'] == 1949])

# # Finds sets with the most pieces.
# print(sets_df[sets_df['num_parts'] == 9987])

# # Groups and counts the number of Sets released each year.
# sets_by_year = sets_df.groupby('year').count()
# print(sets_by_year['set_num'])
# # Plots these sets, but removes the last two years, as neither year's data is complete.
# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])


# # Number of Themes per calendar year
# themes_by_year = sets_df.groupby('year').agg({'theme_id': pd.Series.nunique})
# themes_by_year.rename(columns = {'theme_id': 'nr_themes'}, inplace = True)
# plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])


# # Plot data on two separate axes.
# ax1 = plt.gca() # get current axes
# ax2 = ax1.twinx() 

# ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
# ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='b')

# ax1.set_xlabel('Year')
# ax1.set_ylabel('Number of Sets', color='green')
# ax2.set_ylabel('Number of Themes', color='blue')

# plt.show()


# # SCATTER PLOTS: Average number of parts per LEGO set
# parts_per_set = sets_df.groupby('year').agg({'num_parts': pd.Series.mean})
# plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
# plt.show()

# MERGE DATA and Create Bar Charts
set_theme_count = sets_df['theme_id'].value_counts()
set_theme_count[:5]
# Convert to Pandas DataFrame
set_theme_count = pd.DataFrame({'id':set_theme_count.index, 'set_count':set_theme_count.values})

# Merge the data
merged_df = pd.merge(set_theme_count, themes_df, on='id')

# Creating a bar chart
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
 
plt.bar(merged_df.name[:10], merged_df.set_count[:10])

plt.show()


