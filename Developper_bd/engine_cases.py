import pandas as pd
from sqlalchemy.types import String , Integer ,Date,Float
import sqlalchemy
from sqlalchemy import create_engine
from datetime import date
today = date.today().strftime('%d_%m_%Y')

engine = create_engine("mysql+pymysql://root:root@localhost/corona") #bd corona
engine.connect() # connect to the database

df_europe = pd.read_csv("donnees_world_covidvirus_{}.csv".format(today))
df_europe['Date'] = pd.to_datetime(df_europe['Date'])
df_europe.to_sql('full_data',con= engine ,if_exists='replace',
                  chunksize=1000,
                  index=False,
                  dtype= {"Date": Date,"Country": String(22),"Lat": Float,"Long": Float,
                          "Confirmed": Integer,"Deaths": Integer,"Recovered": Integer, 
                          "Code":String(4),"Continent":String(7),"Region":String(20),
                          "Population":Integer,"LifeExpectancy":Float})
#google                         
df_google = pd.read_csv("C:/Users/Utilisateur/Downloads/google_reports/donnees_google_mobility{}.csv".format(today))
df_google['Date'] = pd.to_datetime(df_google['Date'])
df_google.to_sql('google_data',con= engine ,if_exists='replace',
                  chunksize=1000,
                  index=False,
                  dtype= {"Country": String(23),"Date": Date,"retail": Float,"grocery and pharmacy": Float,
                          "parks":Float,"transit stations": Float,"workplaces": Float,
                          "residential": Float,"Code": String(5)})   
 #apple 
df_apple = pd.read_csv("C:/Users/Utilisateur/Downloads/apple_reports/donnees_apple_mobility{}.csv".format(today))
df_apple['Date'] = pd.to_datetime(df_apple['Date'])      
df_apple.to_sql('apple_data',con= engine ,if_exists='replace',
                  chunksize=1000,
                  index=False,
                  dtype= {"Country": String(15),"Date": Date,"driving": Float,"transit": Float,
                          "walking":Float,"Code": String(5)})                                         

                          