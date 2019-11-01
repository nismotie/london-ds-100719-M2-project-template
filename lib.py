# You don't have to use these classes, but we recommend them as a good place to start!
import requests
import os
from dotenv import load_dotenv
import pymongo



def mongoinsert(db_name, collection_name, dictionary):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[db_name]
    mycollection = mydb[collection_name]
    mydict = dictionary
    mycollection.insert_one(mydict)

class Weather():
    def __init__(self):
        self.url = 'https://api.darksky.net/forecast/'
        self.key = os.getenv("DARKSKYKEY")
        self.weather_days = []
        self.rains = []
    
    def getweather(self, coordinates, date_list):
        for date in date_list:
            response = requests.get(f'{self.url}{self.key}/{coordinates[0]},{coordinates[1]},{date}T15:00:00?exclude=minutely,hourly,daily,alerts,flags')
            r = response.json()
            self.weather_days.append(r)
            
    def api_test(self, coordinates):
        response = requests.get(f'{self.url}{self.key}/{coordinates[0]},{coordinates[1]},2012-03-31T15:00:00?exclude=minutely,hourly,daily,alerts,flags')
        if response.status_code == 200:
            print('Success!')
        else:
            print('Status Incorrect')
        return response.json()
        
            
    def rainmaker(self):
        for weather_day in self.weather_days:
            if 'icon' in weather_day['currently']:
                if 'rain' in weather_day['currently']['icon'].lower():
                    self.rains.append(True)
                else:
                    self.rains.append(False)
            else:
                self.rains.append(False) 

def make_df(table_name): # Takes the name of a table and makes a pandas dataframe from it
    return pd.read_sql_query(f"""SELECT * FROM {table_name}""", con)
        
