# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:45:54 2022

@author: SAM
"""
import pandas as pd

#file_name = pd.read_csv('file.csv')

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

# summary of the data

data.info()

# working with calculation

costPerItem = 11.73
sellingPricePerItem = 21.11
numberOfItemPurchased = 6

# matemaical operation

profitPerItem = sellingPricePerItem - costPerItem
profitPerTransaction = numberOfItemPurchased*profitPerItem
costPerTransaction = numberOfItemPurchased * costPerItem
sellingPricePerTransaction = numberOfItemPurchased * sellingPricePerItem

# costPerTranscation coulum

#costPerTransaction = numberOfItemPurchased * costPerItem
#variable = dataframe['colum_name']


CostPerItems = data['CostPerItem']


NumberofItemsPurchased = data['NumberOfItemsPurchased']

sellingPricePerItems = data['SellingPricePerItem']
#NumberOfItemsPurchased = data['numberOfItemPurchased']
days = data['Day']

data.info()
# adding a new colum to a dataframe

#data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['CostPerTransaction'] = CostPerItems * NumberofItemsPurchased

CPT = data['CostPerTransaction']

data['sellingPricePerTransaction'] = NumberofItemsPurchased * sellingPricePerItems


SPT = data['sellingPricePerTransaction']

# profit and markup formular
# profit = (sales - cost)
# markup = (sales - cost)/

# profit calculation

data['ProfitPerTransaction'] = SPT - CPT

ProfitPerTransaction = data['ProfitPerTransaction']

# markup

data['Markup'] = ProfitPerTransaction / CPT

# rounding up markup

data['MarkupRounding'] = round(data['Markup'], 2)

# combining fields

#DOB = 'Day' + '-' + 'Month' + '-' + 'Year'

day = data['Day'].astype(str)

year = data['Year'].astype(str)

month = data['Month']

data['DOB'] = day + '-' + month + '-' + year

data.iloc[0:15]  # views the first 15 rows
data.iloc[:, 2]  # brings in all the row on the second column
data.iloc[4, 2]  # brings in all the 4th row on 2nd column

# splitting colum

# var name = colum.str.split('sep' , expand=True)

column_split = data['ClientKeywords'].str.split(',', expand=True)

# splitting the colums

data['ClientAge'] = column_split[0]
data['ClientType'] = column_split[1]
data['ClientLenghtOfContract'] = column_split[2]

# replacing a separator

data['ClientAge'] = data['ClientAge'].str.replace('[', '')

data['ClientLenghtOfContract'] = data['ClientLenghtOfContract'].str.replace(
    ']', '')

data['ItemDescription'] = data['ItemDescription'].str.lower()


# bringing anther dataset and merging to existing one
# bringing in value_inc_season dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# merging the two datasets

#newdataset = pd.merge(old_dataset, new_dataset, on='key')

data = pd.merge(data, seasons, on='Month')

# dropping of column

#df = df.drop('columname', axis=1)

data = data.drop('ClientKeywords', axis=1)
data = data.drop('Day', axis=1)
data = data.drop(['Year', 'Month'], axis=1)

# exporting the file

data.to_csv('Value_inc_cleaned.csv', index=False)





C:/Users/SAM/Desktop/python_data_science/SalWebDesign.Com-Python-Tableau-Complete-Data-Analytics-Bootcamp/7. Tableau Project 2 - Blue Bank