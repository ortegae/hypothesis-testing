# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:08:52 2021

@author: erick
"""

#Import required packages 
import pandas as pd 
from scipy.stats import chi2_contingency,chi,chi2

#import data 
campaign_data=pd.read_excel("grocery_database.xlsx",sheet_name="campaign_data")

#Filter Data

#Filtered by column name
campaign_data=campaign_data.loc[campaign_data["mailer_type"] !="Control"]

#summarize to get observed frequencies

observed_values=pd.crosstab(campaign_data["mailer_type"],campaign_data["signup_flag"]).values

mailer1_signup_rate=123/(252+123)
mailer2_signup_rate=127/(209+127)

print(mailer1_signup_rate,mailer2_signup_rate)

#State hypothesis and set acceptance criteria 

null_hypothesis="There is no relationship between mailer type and signup rate. They are independent"
alternate_hypothesis="There is a relationship between mailer type and signup rate. There are not indendent"
acceptance_criteria=0.05

#calculate expected frequencies & chi square statistic

chi2_statistic,p_value,dof,expected_values=chi2_contingency(observed_values,correction=False)

print(chi2_statistic,p_value)

#Find the critical value for our test 
#ppf=percentage point function

critical_value=chi2.ppf(1-acceptance_criteria,dof)
print(critical_value)

#Print the results (Chi2 statistic)

if chi2_statistic>= critical_value:
    print(f" As our chi square statistic of {chi2_statistic} is higher than our critical value of {critical_value}, we reject the null hypothesis and conclude that {alternate_hypothesis}")
else:
    print(f" As our chi square statistic of {chi2_statistic} is lower than our critical value of {critical_value}, we reject the null hypothesis and conclude that {null_hypothesis}")

#Print the results (p_value, best for stakeholders)

if p_value<= critical_value:
    print(f" As our p-value statistic of {p_value} is higher than our acceptance criteria of {acceptance_criteria}, we reject the null hypothesis and conclude that {alternate_hypothesis}")
else:
    print(f" As our chi square statistic of {p_value} is lower than our acceptance cristeria of {acceptance_criteria} we reject the null hypothesis and conclude that {null_hypothesis}")



