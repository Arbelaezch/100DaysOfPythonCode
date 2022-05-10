from cProfile import label
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

data_file = "Days59-80:Advanced/day72/QueryResults.csv"

df = pd.read_csv(data_file)

df.columns = ['DATE', 'TAG', 'POSTS']

# # Finds the sum of posts for each unique TAG
# print(df.groupby(["TAG"]).sum())
# # Counds the number of new entries for each TAG
# print(df.groupby(["TAG"]).count())

# Convert entire column to type DateTime
df.DATE = pd.to_datetime(df['DATE'])

# PIVOTs the data so that each row shows the posts for each tag on every given date.
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
# Overrides reshaped_df and replaces each NaN with 0.
reshaped_df.fillna(0, inplace=True) 
# # Finds if there are any NaN left in the dataframe.
# reshaped_df.isna().values.any()

# Calculates a Rolling Mean dataframe.
# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()

# Change size of graph.
plt.figure(figsize=(17,8))
# Size of ticks
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
# Plots the data for java in a single graph.
# plt.plot(reshaped_df.index, reshaped_df['java'], color='r', label='java')
# plt.plot(reshaped_df.index, reshaped_df['python'], color='g', label='python')

# # Plot the PIVOTed data
# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column], linewidth=2, label=reshaped_df[column].name)
    
# plot the Rolled Mean df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)

# Provides legend
plt.legend(fontsize=16)


# Increase Font Size of labels
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
# Lower limit of 0.
plt.ylim(0, 35000)

# Displays the graph
plt.show()



# print(df.head)