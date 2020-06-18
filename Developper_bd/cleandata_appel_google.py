
import pandas as pd
from datetime import datetime
import datetime

# Chercher la date courante formaté
from datetime import date
today = date.today().strftime('%d_%m_%Y')
#apple
apple = pd.read_csv('C:/Users/Utilisateur/Downloads/apple_reports/apple_mobility_report.csv')
apple = apple[['country', 'date','driving','transit','walking']]
apple = apple.rename(columns={'country': 'Country','date': 'Date'})
apple['Date'] = pd.to_datetime(apple['Date'])
pays_europe =['Italy' , 'Portugal' , 'Spain' , 'France' , 'Netherlands' , 'Germany' , 'Poland' , 'Ireland', 'Ukraine', 'Romania' , 'Switzerland' , 'Albania' ,  'Austria,Belarus', 'Belgium' ,'Bosnia and Herzegovina', 'Bulgaria','Croatia','Denmark' ,'Estonia', 'Finland','Greece','Hungary', 'Iceland', 'Latvia' ,'Lithuania','Malta' ,'Moldova' , 'Montenegro','Norway', 'North Macedonia', 'Russia', 'Serbia', 'Slovakia' ,'Slovenia' , 'Sweden','Turkey'  ,'Ukraine' , 'United Kingdom']
europe_apple = apple[apple.Country.isin(pays_europe)]
cc= pd.read_csv("contry.csv")
ccn = cc.drop(columns=['Unnamed: 0', 'SurfaceArea',
       'IndepYear' , 'GNP', 'GNPOld',
       'LocalName', 'GovernmentForm', 'HeadOfState', 'Capital', 'Code2','Continent','Region','Population','LifeExpectancy'])
cn_europe = ccn[ccn.Name.isin(pays_europe)]
cn_europe= cn_europe.rename(columns={"Name": "Country"})
df_europe_apple =  pd.merge(europe_apple,cn_europe, on='Country')

df_europe_apple.to_csv("C:/Users/Utilisateur/Downloads/apple_reports/donnees_apple_mobility{}.csv".format(today), index = False)
#google 


google = pd.read_csv('C:/Users/Utilisateur/Downloads/google_reports/mobility_report_countries.csv')
google = google[['country', 'date','retail','grocery and pharmacy','parks','transit stations','workplaces','residential']]
google = google.rename(columns={'country': 'Country','date': 'Date'})
google['Date'] = pd.to_datetime(google['Date'])
pays_europe =['Italy' , 'Portugal' , 'Spain' , 'France' , 'Netherlands' , 'Germany' , 'Poland' , 'Ireland', 'Ukraine', 'Romania' , 'Switzerland' , 'Albania' ,  'Austria,Belarus', 'Belgium' ,'Bosnia and Herzegovina', 'Bulgaria','Croatia','Denmark' ,'Estonia', 'Finland','Greece','Hungary', 'Iceland', 'Latvia' ,'Lithuania','Malta' ,'Moldova' , 'Montenegro','Norway', 'North Macedonia', 'Russia', 'Serbia', 'Slovakia' ,'Slovenia' , 'Sweden','Turkey'  ,'Ukraine' , 'United Kingdom']
europe_google = google[google.Country.isin(pays_europe)]
cc= pd.read_csv("contry.csv")
ccn = cc.drop(columns=['Unnamed: 0', 'SurfaceArea',
       'IndepYear' , 'GNP', 'GNPOld',
       'LocalName', 'GovernmentForm', 'HeadOfState', 'Capital', 'Code2','Continent','Region','Population','LifeExpectancy'])
cn_europe = ccn[ccn.Name.isin(pays_europe)]

cn_europe= cn_europe.rename(columns={"Name": "Country"})
df_europe_google =  pd.merge(europe_google,cn_europe, on='Country')
df_europe_google['Date'] = pd.to_datetime(df_europe_google['Date'])
df_europe_google.to_csv("C:/Users/Utilisateur/Downloads/google_reports/donnees_google_mobility{}.csv".format(today), index = False)



