# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:07:05 2021

@author: Kathryn Haske

Get specified indicators for given years and countries from the World Bank API
and save the dataframe as as CSV file
"""

import requests
import pandas as pd

def get_wb_data(var, param, counrty='all'):
    """
    Function to get data from World Bank API

    Args:
        var (string): indicator of interest
        param (string): parameters to send with API call
        country (string): counrties of interest

    Returns:
        Pandas dataframe from json response data
        
    """
    req = 'http://api.worldbank.org/v2/country/'+counrty+'/indicator/'+var
    response = requests.get(req, params=param)
    response.raise_for_status()
    return pd.DataFrame(response.json()[1])

def clean_wb_df(df, value_column):
    """
    Function to get clean data from World Bank API

    Args:
        df (dataframe): dataframe created from worldbank json data
        value_column (string): name of column to be created

    Returns:
        Pandas dataframe with counrty code as key
        
    """
    df2 = pd.DataFrame(columns=['country',value_column])
    for index, row in df.iterrows():
        country = row['country']
        country_code = country['id']
        data = [country['value'],row['value']]
        df2.loc[country_code] = data
    return df2
        
save_filename = '../data/worldbankpop.csv' #file name to save to
total_records = '500' #maximum results to return from API call
year = []
var = []
col_name = []
df = []

#Get total population for year 2000
year.append('2000')
var.append('SP.POP.TOTL')
col_name.append('2000_population')

#Get total population for year 2005
year.append('2005')
var.append('SP.POP.TOTL')
col_name.append('2005_population')

#Get total population for year 2010
year.append('2010')
var.append('SP.POP.TOTL')
col_name.append('2010_population')

#Get total population for year 2015
year.append('2015')
var.append('SP.POP.TOTL')
col_name.append('2015_population')


# Get a dataframe for each indicator and year
for i in range(len(var)):
    parameters = {
        'date':year[i],
        'format':'json',
        'per_page':total_records
    }
    df.append(clean_wb_df(get_wb_data(var[i],parameters), col_name[i]))

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
