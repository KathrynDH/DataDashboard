# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:54:46 2021

@author: Kathryn Haske

Load data from csv files for webpage graphs
"""

import pandas as pd


def read_data(filenames, drop_columns=None, join_method='left'):
    """
    Function to read data from csv files

    Args:
        filenames (list of strings): csv files to open
        drop_columns (string): duplicate columns to drop when joining
        join_method (string): how to join the dataframes

    Returns:
        Pandas dataframe from csv files
        
    """    
    df = pd.read_csv(filenames[0], index_col=0)
    for i in range(1,len(filenames)):
        df_other = pd.read_csv(filenames[i], index_col=0)
        df = df.join(df_other.drop(columns=drop_columns), how=join_method)
    return df
