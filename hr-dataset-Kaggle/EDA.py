import pandas as pd
import matplotlib.pyplot as plt



hr_df = pd.read_csv("HRDataset_v14.csv")
hr_df.columns

[
    'Employee_Name', 'EmpID',
    'MarriedID', 'MaritalStatusID',
    'GenderID', 'EmpStatusID', 'DeptID', 'PerfScoreID', 'FromDiversityJobFairID',
    'Salary',
    'Termd', 
    'PositionID', 'Position', 
    'State', 'Zip', 
    'DOB',
    'Sex', 
    'MaritalDesc', 'CitizenDesc', 'HispanicLatino', 'RaceDesc',
    'DateofHire', 'DateofTermination', 'TermReason', 
    'EmploymentStatus',
    'Department', 'ManagerName', 'ManagerID', 
    'RecruitmentSource',
    'PerformanceScore', 'EngagementSurvey', 'EmpSatisfaction',
    'SpecialProjectsCount', 'LastPerformanceReview_Date', 
    'DaysLateLast30',
    'Absences'
]

# categorical data
lkp_cols=[
    'MarriedID', 'MaritalStatusID',
    'GenderID', 'EmpStatusID', 'DeptID', 'PerfScoreID', 'FromDiversityJobFairID',
    # 'Salary', 
    'Termd', 
    'PositionID', 'Position', 
    'State', 'Zip', 
    'DOB',
    'Sex', 
]
for i in lkp_cols: 
    print('---', i)
    print(hr_df[i].value_counts())
    