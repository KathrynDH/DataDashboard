# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 11:04:16 2021

@author: Kathryn Haske

Load data and create graphs for webpage
Function get_graphs called by myapp/routes.py
"""
from webscripts.getdata import read_data
from webscripts.plotlygraphs import line_graph, scatter_plot, bar_chart

def get_graphs():
    """
    Function to load data and create graphs
    called by myapp/routes.py

    Args:
       none

    Returns:
        list of plotly figures
        
    """
    #files to load for first four graphs: youth literacy and population data
    files = ['data/worldbanklit.csv','data/worldbankpop.csv']
    #duplicate columns in files
    drop_dup_col = 'country'
    df = read_data(files, drop_dup_col).dropna()
    
    figures = []
    year_list = ['2000', '2005', '2010', '2015']
    
    # figure-0
    figures.append(
        line_graph(
            year_list, df, 'country', slice(1,5,1), 
            'Literacy rate, youth (ages 15-24) <br>by country income category',
            'year', 'youth literacy rate %'
            )
        )
    
    # figure-1
    figures.append(
        bar_chart(
            df.country.tolist(), df.iloc[:,4].tolist(), 
            '2015 literacy rate, youth (ages 15-24) <br>by country income category',
            None, 'youth literacy rate %'
            )
        )
 
    # figure-2
    figures.append(
        line_graph(
            year_list, df, 'country', slice(5,9,1), 
            'Population by country income category',
            'year', 'population'
            )
        )
    
    # figure-3
    figures.append(
        bar_chart(
            df.country.tolist(), df.iloc[:,8].tolist(), 
            '2015 population by country income category',
            None, 'population'
            )
        )

    #file to load for graph: GNP and youth literacy
    files = ['data/worldbank-lit-inc.csv', 'data/country-list.csv']
    df2 = read_data(files, drop_dup_col,'inner').dropna()
        
    # figure-4
    figures.append(
        scatter_plot(
            df2.iloc[:,1], df2.iloc[:,3], df2.iloc[:,0],
            'Youth literacy rate and GNP USD',
            'GNP', 'youth literacy rate %'
            )
        )
    
    #get GNP under 5k and youth literacy
    df3 = df2[df2['gnp']<5000]
        
    # figure-5
    figures.append(
        scatter_plot(
            df3.iloc[:,1], df3.iloc[:,3], df3.iloc[:,0],
            'Youth literacy rate and GNP under 5,000 USD',
            'GNP', 'youth literacy rate %'
            )
        )

    return figures
