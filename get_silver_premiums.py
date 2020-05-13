# releveant imports
import os
import re
import time
from datetime import date

import numpy as np
import pandas as pd
import requests

# ignore SettingWithCopyWarning to mathe the output in the Terminal more readable
pd.options.mode.chained_assignment = None


# create folder for the HTMLs
folder_html = 'Gold_de'
if not os.path.exists(folder_html):
    os.makedirs(folder_html)
# create folder for CSVs
folder_csv = 'Gold_de_csv'
if not os.path.exists(folder_csv):
    os.makedirs(folder_csv)

# to name the file with the current date
date_today = date.today()

# for naming purposes
file_name = 'gold_de_'
end_html = '.html'
end_csv = '.csv'

# get the HTML and save it in the folder
url = 'https://www.gold.de/aufgeldtabelle/silber/'
r = requests.get(url)
with open(os.path.join(folder_html, file_name + date_today.strftime('%d.%m.%Y') + end_html), mode = 'w') as file:
    file.write(r.text)

# create the path to the html file
path_html = folder_html + '/' + file_name + date_today.strftime('%d.%m.%Y') + end_html

# create a pdandas DataFrame
df_list = pd.read_html(path_html)

# the table we are looking for is saved in the second index 
df = df_list[1]

# cleaning steps

# remove first row
df = df.iloc[1:]
# drop missing values 
df.dropna(axis = 1, how = 'all', inplace = True)
df.dropna(axis = 0, how = 'all', inplace = True)
# there are different columns that can be droped that aren't in each scrapping event
if 'Aufgeld in %.1' in df.columns.values:
    df.drop(columns = 'Aufgeld in %.1', inplace = True)
# remove a row which can be clicked to enlarge the table on the website 
df.drop(index = df[df['Rang']=="Gesamte Aufgeldtabelle anzeigen"].index.values, inplace = True)
# rename columns 
df.rename(columns = {'Produktbezeichnung':'Product', 'Produktpreis':'Price in EUR', 'Preis/kg':'Price/kg', 
                     'Preis/oz':'Price/oz', 'Preis/g':'Price/g', 'Aufgeld in %':'Premiums in %'}, inplace = True)
# transform strings to make them into a float
df['Price in EUR'] = df['Price  in EUR'].map(lambda x: str(x).replace('EUR', '').strip().replace('.', '').replace(',','.'))
df['Price/kg'] = df['Price/kg'].map(lambda x: str(x).replace('EUR', '').strip().replace('.', '').replace(',','.'))
df['Price/oz'] = df['Price/oz'].map(lambda x: str(x).replace('EUR', '').strip().replace('.', '').replace(',','.'))
df['Price/g'] = df['Price/g'].map(lambda x: str(x).replace('EUR', '').strip().replace('.', '').replace(',','.'))
df['Premiums in %'] = df['Premiums in %'].map(lambda x: str(x).replace('%', '').strip().replace('.', '').replace(',','.'))
# transform strings to floats
df['Price in EUR'] = df['Price in EUR'].astype('float')
df['Price/kg'] = df['Price/kg'].astype('float')
df['Price/oz'] = df['Price/oz'].astype('float')
df['Price/g'] = df['Price/g'].astype('float')
df['Premiums in %'] = df['Premiums in %'].astype('float')

# Output path
path_to_csv = folder_csv + '/' + file_name + date_today.strftime('%d.%m.%Y') + end_csv
# save cleand DataFrame
df.to_csv(path_to_csv)

# check if file exists
print(os.path.isfile(path_to_csv))