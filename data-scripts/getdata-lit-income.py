# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 8:55:05 2021

@author: Kathryn Haske

Get specified indicators for given years and countries from the World Bank API
and save the dataframe as as CSV file

Indicators: GNP and youth literacy rate for most recent year available
"""

from functions import get_wb_data, clean_wb_df

        
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

#Get population
var.append('SP.POP.TOTL')
col_name.append('population')


# Get a dataframe for each indicator for most recent year available (mrnev=1)
parameters = {
        'format':'json',
        'per_page':total_records,
        'mrnev':'1'
    }

for i in range(len(var)):
    df1 = get_wb_data(var[i],parameters)
    df2 = clean_wb_df(df1, col_name[i], mrnev=True)
    df.append(df2)

# Join the dataframes
df_wb = df[0]
for k in range(1,len(df)):
    df_wb = df_wb.join(df[k].iloc[:,1:3], how='outer')
    df_no_country = df_wb[df_wb['country'].isnull()]
    for index, row in df_no_country.iterrows():
        df_wb.at[index,'country']=df[k].at[index,'country']
    
# Print info and save to csv
print('Rows:{} Columns:{}\n'.format(df_wb.shape[0],df_wb.shape[1]))
print('First 5 rows:')
print(df_wb.head())
print('Records with no na values: {}'.format(df_wb.dropna().shape[0]))

df_wb.to_csv(save_filename)
print('File '+save_filename+' saved')
