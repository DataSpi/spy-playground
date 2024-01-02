""" 
IBM is working on a new feature to analyze user purchasing behavior for all Fridays in the first quarter of the year. 
For each Friday, calculate the average amount users have spent. 
The output should contain the week number of that Friday and average amount spent.
"""

import pandas as pd

# read & transform 
df = pd.read_csv("data/raw/user_purchases.csv", sep=';')
day_dict = {
    'Monday':0,
    'Tuesday':1,
    'Wednesday':2,
    'Thursday':3,
    'Friday':4,
    'Saturday':5,
    'Sunday':6,
}
df['day_num'] = df.day_name.replace(day_dict)
# df.head()


# filtering
# first quarter of the year
df.date = pd.to_datetime(df.date, dayfirst=True)
df['week'] = df.date.dt.isocalendar()['week']
df_1st_qtr = df.query("date.dt.month<=3")

# For each Friday, calculate the average amount users have spent
pd.pivot_table(
    data=df_1st_qtr.query('day_num==4'),
    index=['week', 'day_name'],
    values='amount_spent',
    aggfunc='mean'
).style.bar()


# testing live streaming on youtube for the first time. I dont know how to live stream properly yet. 
# hope that I will do better in the future