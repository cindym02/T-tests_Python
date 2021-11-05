#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 22:36:21 2021

@author: cindy
"""

import pandas as pd

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

diabetes_small = diabetes.sample(100)

list(diabetes_small)

diabetes['totalCountProcedures'] = diabetes['num_procedures'] + diabetes['num_lab_procedures']

from scipy.stats import ttest_ind


# (1) Is there a difference between sex (M:F) (IV) 
# and the number of days in hospital (DV)? Yes

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']
ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])

# Ttest_ind_Result_statistic= 9.542637042242887
# P-value= 1.4217299655114968e-21
# Statistically significant since P-value <= 0.05, reject null hypothesis


# (2) Is there a difference between RACE (Caucasian and African American) 
# and the number of days in hospital (DV)? Yes

Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])

# Ttest_indResult(statistic=-5.0610017032095325, 
# pvalue=4.178330085585203e-07
# Statistically significant since P-value <= 0.05, reject null hypothesis


# (3) Is there a difference between RACE (Asian and African American) (IV)
# and the number of lab procedures performed? (DV) Yes

Asian = diabetes[diabetes['race']=='Asian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Asian['num_lab_procedures'], AfricanAmerican['num_lab_procedures'])

# Ttest_indResult(statistic=-3.9788715315360292
# pvalue=6.948907528800307e-05
# Statistically significant since P-value <= 0.05, reject null hypothesis


# (4) Is there a difference between Age ([20-30 years] and [60-70 years]) (IV)
# and the number of days in hospital (DV)? Yes

Young_adult = diabetes[diabetes['age']=='[20-30)']
Elderly = diabetes[diabetes['age']=='[60-70)']
ttest_ind(Young_adult['time_in_hospital'], Elderly['time_in_hospital'])

# Ttest_indResult(statistic=-10.795432348028305, 
# pvalue=4.172084976100482e-27
# Statistically significant since P-value <= 0.05, reject null hypothesis



