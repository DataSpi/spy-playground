""" 
https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=2

Given a table of purchases by date, calculate the month-over-month percentage change in revenue. 
The output should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd decimal point, 
and sorted from the beginning of the year to the end of the year.

The percentage change column will be populated from the 2nd month forward and can be calculated as
((this month's revenue - last month's revenue) / last month's revenue)*100.
"""

import pandas as pd 

sf_trans = pd.read_excel("data/raw/sf_transactions.xlsx")

# calc the revenue of each month
sf_trans['month'] =  sf_trans.created_at.dt.strftime('%Y-%m')#.dt.month

pivot = pd.pivot_table(data=sf_trans, index='month', values='value', aggfunc='sum')#.style.bar().format('{:,.0f}')

# percentage change in rev? 
pivot['changes'] = pivot.value.diff()#.fillna(0)
pivot['pct_changes'] = pivot.value.pct_change()#.fillna(0)
pivot.style.format({'pct_changes':'{:.2%}', 'value':'{:.0f}', 'changes':'{:.0f}'})

output = pivot['pct_changes']
output # this is what you'll see when you click in the "Expected Result" button in the source link on top of the page






