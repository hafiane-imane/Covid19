
import pandas as pd
from datetime import datetime
import datetime

# Chercher la date courante formaté
from datetime import date
today = date.today().strftime('%d_%m_%Y')

# Chercher les données
full_table = pd.read_csv('https://raw.githubusercontent.com/imdevskp/covid_19_jhu_data_web_scrap_and_cleaning/master/covid_19_clean_complete.csv', 
                       parse_dates=['Date'])

full_table = full_table[['Date', 'Country/Region','Lat','Long','Confirmed', 'Deaths', 'Recovered']]
full_table = full_table.rename(columns={'Country/Region': 'Country'})
#  clean and transform
pays_europe =['Italy' , 'Portugal' , 'Spain' , 'France' , 'Netherlands' , 'Germany' , 'Poland' , 'Ireland', 'Ukraine', 'Romania' , 'Switzerland' , 'Albania' ,  'Austria,Belarus', 'Belgium' ,'Bosnia and Herzegovina', 'Bulgaria','Croatia','Denmark' ,'Estonia', 'Finland','Greece','Hungary', 'Iceland', 'Latvia' ,'Lithuania','Malta' ,'Moldova' , 'Montenegro','Norway', 'North Macedonia', 'Russia', 'Serbia', 'Slovakia' ,'Slovenia' , 'Sweden','Turkey'  ,'Ukraine' , 'United Kingdom']
europe = full_table[full_table.Country.isin(pays_europe)]

cc= pd.read_csv("contry.csv")
ccn = cc.drop(columns=['Unnamed: 0', 'SurfaceArea',
       'IndepYear' , 'GNP', 'GNPOld',
       'LocalName', 'GovernmentForm', 'HeadOfState', 'Capital', 'Code2'])

cn_europe = ccn[ccn.Name.isin(pays_europe)]
cn_europe= cn_europe.rename(columns={"Name": "Country"})

df_europe =  pd.merge(europe,cn_europe, on='Country')

df_europe.to_csv("donnees_world_covidvirus_{}.csv".format(today), index = False)


