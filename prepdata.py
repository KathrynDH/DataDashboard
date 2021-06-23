# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 11:04:16 2021

@author: Kathryn Haske

Load data and create graphs for webpage
Function get_graphs called by myapp/routes.py
"""
import pandas as pd
import plotly.graph_objs as go


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


def line_graph(x_list, df, name_col, y_cols, chart_title, x_label, y_label):
    """
    Function to create plotly line graph

    Args:
        x_list (list): graph x values
        df (Pandas DataFrame): dataframe to use for series and y-values
        name_col (string): df column to use for series names
        y_cols (int or slice object): df column numbers to use for y-values
        chart_title (string): title for chart
        x_label (string): label for x-axis
        y_label (string): label for y-axis

    Returns:
        dictionary for plotly line graph
        
    """
    graph = []
    
    for index, row in df.iterrows():
        graph.append(go.Scatter(
            x = x_list,
            y = row.tolist()[y_cols],
            mode = 'lines',
            name = row[name_col]
      ))

    graph_layout = dict(title = chart_title,
                xaxis = dict(title = x_label),
                yaxis = dict(title = y_label),
                )
    return dict(data=graph, layout=graph_layout)

def scatter_plot(x_vals, y_vals, names, chart_title, x_label, y_label):
    """
    Function to create plotly scatter plot

    Args:
        x_vals (list): graph x values
        y_vals (list): graph y values
        names (list of strings): title for each marker
        chart_title (string): title for chart
        x_label (string): label for x-axis
        y_label (string): label for y-axis

    Returns:
        dictionary for plotly bar graph
        
    """
    graph= [go.Scatter(
            x = x_vals,
            y = y_vals,
            mode = 'markers',
            text=names,
            marker=dict(
                color=y_vals, #set color equal to a variable
                colorscale='Viridis' # plotly colorscale
                )
            )]

    graph_layout = dict(title = chart_title,
                xaxis = dict(title = x_label),
                yaxis = dict(title = y_label),
                )
    return dict(data=graph, layout=graph_layout)

def bar_chart(x_vals, y_vals, chart_title, x_label, y_label):
    """
    Function to create plotly bar graph

    Args:
        x_vals (list): graph x values
        y_vals (list): graph y values
        chart_title (string): title for chart
        x_label (string): label for x-axis
        y_label (string): label for y-axis

    Returns:
        dictionary for plotly bar graph
        
    """
    graph = [go.Bar(
      x = x_vals,
      y = y_vals
      )]

    graph_layout = dict(title = chart_title,
                xaxis = dict(title = x_label),
                yaxis = dict(title = y_label),
                )
    return dict(data=graph, layout=graph_layout)

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


    #return figures
    return df2
