# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 13:55:49 2021

@author: Kathryn Haske

Functions for data scripts
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

def clean_wb_df(df, value_column, mrnev=False):
    """
    Function to get clean data from World Bank API

    Args:
        df (dataframe): dataframe created from worldbank json data
        value_column (string): name of column to be created
        mrnev (bool): most recent year available (mrnev=1)

    Returns:
        Pandas dataframe with counrty code as key
        
    """
    if mrnev:
        df2 = pd.DataFrame(
            columns=['country',value_column,value_column+'_year'])
    else:
        df2 = pd.DataFrame(columns=['country',value_column])
    for index, row in df.iterrows():
        country = row['country']
        country_code = country['id']
        if mrnev:
            data = [country['value'],row['value'],row['date']]
        else: 
            data = [country['value'],row['value']]
        df2.loc[country_code] = data
    return df2

