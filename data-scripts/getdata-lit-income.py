# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 8:55:05 2021

@author: Kathryn Haske

Get specified indicators for given years and countries from the World Bank API
and save the dataframe as as CSV file

Indicators: GNP and youth literacy rate for most recent year available
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
        value_column (string): name of value column to be created

    Returns:
        Pandas dataframe with counrty code as key, value column and year
        
    """
    df2 = pd.DataFrame(columns=['country',value_column,value_column+'_year'])
    for index, row in df.iterrows():
        country = row['country']
        country_code = country['id']
        data = [country['value'],row['value'],row['date']]
        df2.loc[country_code] = data
    return df2
        
save_filename = '../data/worldbank-lit-inc.csv' #file name to save to
total_records = '500' #maximum results to return from API call
year = []
var = []
col_name = []
df = []

#Get total GNP per capita
var.append('NY.GNP.PCAP.CD')
col_name.append('gnp')

#Get literacy rate, youth total (% of people ages 15-24)
var.append('SE.ADT.1524.LT.ZS')
col_name.append('youth_literacy')


# Get a dataframe for each indicator for most recent year available (mrnev=1)
for i in range(len(var)):
    parameters = {
        #'date':year[i],
        'format':'json',
        'per_page':total_records,
        'mrnev':'1'
    }
    df1 = get_wb_data(var[i],parameters)
    df2 = clean_wb_df(df1, col_name[i])
    df.append(df2)

# Join the dataframes
df_wb = df[0]
for k in range(1,len(df)):
    df_wb = df_wb.join(df[k].iloc[:,1:3], how='outer')
    
# Print info and save to csv
print('Rows:{} Columns:{}\n'.format(df_wb.shape[0],df_wb.shape[1]))
print('First 5 rows:')
print(df_wb.head())
print('Records with no na values: {}'.format(df_wb.dropna().shape[0]))

df_wb.to_csv(save_filename)
print('File '+save_filename+' saved')
