# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:10:51 2021

@author: erick
"""


#import required packages

import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind,norm

#Create mock data

sample_A=norm.rvs(loc=500,scale=100,size=250,random_state=42).astype(int)
sample_B=norm.rvs(loc=550,scale=150,size=100,random_state=42).astype(int)

plt.hist(sample_A,density=True,alpha=0.5)
plt.hist(sample_B,density=True,alpha=0.5)
plt.show()

sample_A_mean=sample_A.mean()
sample_B_mean=sample_B.mean()
print(sample_A_mean,sample_B_mean)


#Set the Hypothesis & Acceptance criteria 
null_hypothesis="The mean of this sample A is equal to the mean of the Mean of sample B"
alternate_hypothesis="The mean of this sample A is equal to the mean of Sample B"
acceptance_criteria=0.05



#Execute the Hypothesis Test

t_statistic,p_value=ttest_ind(sample_A,sample_B)
print(t_statistic,p_value)

#Print the result (P-value)

if p_value<= acceptance_criteria:
    print(f" As our p-value statistic of {p_value} is higher than our acceptance criteria of {acceptance_criteria}, we reject the null hypothesis and conclude that {alternate_hypothesis}")
else:
    print(f" As our chi square statistic of {p_value} is lower than our acceptance cristeria of {acceptance_criteria} we reject the null hypothesis and conclude that {null_hypothesis}")

#WELCH T -TEST


#EXECUTE HYPOTHESIS TEST
t_statistic,p_value=ttest_ind(sample_A,sample_B,equal_var=False)
print(t_statistic,p_value)

#Print the result (P-value)

if p_value<= acceptance_criteria:
    print(f" As our p-value statistic of {p_value} is higher than our acceptance criteria of {acceptance_criteria}, we reject the null hypothesis and conclude that {alternate_hypothesis}")
else:
    print(f" As our chi square statistic of {p_value} is lower than our acceptance cristeria of {acceptance_criteria} we reject the null hypothesis and conclude that {null_hypothesis}")

