import pandas as pd 

""" Question 1: 
IBM wants to reward employees who meet certain criteria. However, to ensure fairness, the following conditions must be met:


•	The employee must have been with the company for at least 3 years
•	The employee's department must have at least 5 employees
•	The salary must be within the top 10% of salaries within the department


The output should include the Employee ID, Salary, and Department of the employees meeting the criteria.
"""

"""___first try. this is really hard w/o groupby. I'm so stupid__
emp_sal = pd.read_excel("data/raw/employee-salaries.xlsx")

## 3y seniority
output = emp_sal.query("tenure>=3").reset_index().copy()


# dept have at least 5 emps
output.department.value_counts() # so, all dept left have more than 5 emps. 
# we don't have to filter this criterium anymore


# the sal be in top 10% of dept sal 
pivot = output[['department', 'salary']].pivot(columns='department')
pivot = pivot.quantile(0.9).reset_index().drop(columns='level_0')# this the the 90th percentile. those who are in top 10 have value higher than this. 
pivot = pivot.rename(columns={0.9:'_90th'}) # 0.9 is actually a column name in float format, so we do not have to put "" surround it. 
sup_dict=pivot.set_index(keys='department').to_dict()['_90th']

indices =[]
for i in output.department.unique():
    _90th=sup_dict[i]
    # print(i, _90th)
    # print(output.query("department==@i and salary>=@_90th").index)
    index_list = output.query("department==@i and salary>@_90th").index.to_list()
    for i in index_list: 
        indices.append(i)
indices
output.loc[indices, :]
"""



# this is the solution BingAI gave me. this is so much easier. now I know where I miss. 
emp_sal = pd.read_excel("data/raw/employee-salaries.xlsx")

## 3y seniority
output = emp_sal.query("tenure>=3").reset_index().copy()

# dept have at least 5 emps
output = output.groupby('department').filter(lambda x: len(x) >= 5)

# the sal be in top 10% of dept sal 
output = output.groupby('department').apply(lambda x: x[x['salary'] > x['salary'].quantile(0.9)])





