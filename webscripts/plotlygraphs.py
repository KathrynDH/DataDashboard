# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:56:55 2021

@author: Kathryn Haske

Create plotly graphs for webpage
"""

import pandas as pd
import plotly.graph_objs as go

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
        dictionary for plotly scatter plot
        
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
