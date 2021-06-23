# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:50:37 2021

@author: Kathryn Haske

Get specified indicators for given years and countries from the World Bank API
and save the dataframe as as CSV file

Indicators: Youth literacy rate for income groups 
            years: 2000, 2005, 2010, and 2015
"""

from functions import get_wb_data, clean_wb_df
     
save_filename = '../data/worldbanklit.csv' #file name to save to
total_records = '500' #maximum results to return from API call
areas = 'XM;XN;XP;XT;XD;1W'
year = []
var = []
col_name = []
df = []

#Get literacy rate, youth total (% of people ages 15-24) for year 2000
year.append('2000')
var.append('SE.ADT.1524.LT.ZS')
col_name.append('2000_youth_literacy')

#Get literacy rate, youth total (% of people ages 15-24) for year 2005
year.append('2005')
var.append('SE.ADT.1524.LT.ZS')
col_name.append('2005_youth_literacy')

#Get literacy rate, youth total (% of people ages 15-24) for year 2010
year.append('2010')
var.append('SE.ADT.1524.LT.ZS')
col_name.append('2010_youth_literacy')

#Get literacy rate, youth total (% of people ages 15-24) for year 2015
year.append('2015')
var.append('SE.ADT.1524.LT.ZS')
col_name.append('2015_youth_literacy')

# Get a dataframe for each indicator and year
for i in range(len(var)):
    parameters = {
        'date':year[i],
        'format':'json',
        'per_page':total_records
    }
    df.append(clean_wb_df(get_wb_data(var[i],parameters, areas), col_name[i]))

# Join the dataframes
df_wb = df[0]
for k in range(1,len(df)):
    df_wb = df_wb.join(df[k].iloc[:,1], how='outer')
    
# Print info and save to csv
print('Rows:{} Columns:{}\n'.format(df_wb.shape[0],df_wb.shape[1]))
print('First 5 rows:')
print(df_wb.head())
print('Records with no na values: {}'.format(df_wb.dropna().shape[0]))
df_wb.to_csv(save_filename)
print('File '+save_filename+' saved')

