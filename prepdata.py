# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 11:04:16 2021

@author: Kathryn Haske
"""
import pandas as pd
import plotly.graph_objs as go


def read_data(filenames, drop_columns=None, join_method='left'):
    df = pd.read_csv(filenames[0], index_col=0)
    for i in range(1,len(filenames)):
        df_other = pd.read_csv(filenames[i], index_col=0)
        df = df.join(df_other.drop(columns=drop_columns), how=join_method)
    return df


def line_graph(x_list, df, name_col, y_cols, chart_title, x_label, y_label):
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

def bar_chart(x_vals, y_vals, chart_title, x_label, y_label):
    graph = go.Bar(
      x = x_vals,
      y = y_vals
      )

    graph_layout = dict(title = chart_title,
                xaxis = dict(title = x_label),
                yaxis = dict(title = y_label),
                )
    return dict(data=graph, layout=graph_layout)

def get_graphs():
    files = ['data/worldbanklit.csv','data/worldbankpop.csv']
    drop_dup_col = 'country'
    df = read_data(files, drop_dup_col).dropna()
    
    figures = []
    year_list = ['2000', '2005', '2010', '2015']
    
    figures.append(
        line_graph(
            year_list, df, 'country', slice(0,5,1), 
            'title', 'year', 'youth literacy rate'
            )
        )
    
    figures.append(
        bar_chart(
            df.country.tolist(), df.iloc[:,4].tolist(), 
            'title', 'country', 'youth literacy rate'
            )
        )
    
    return figures
