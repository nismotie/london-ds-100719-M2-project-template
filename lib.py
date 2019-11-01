import requests
import os
from dotenv import load_dotenv
import pymongo



def mongoinsert(db_name, collection_name, dictionary): 
    myclient = pymongo.MongoClient("mongodb://localhost:27017/") # Connect to mongo server
    mydb = myclient[db_name] # Create new database
    mycollection = mydb[collection_name] # Create new collection
    mycollection.insert_one(dictionary) # Inserting data into the collection

class Weather():
    def __init__(self):
        self.url = 'https://api.darksky.net/forecast/' # Making attributes for Weather object
        self.key = os.getenv("DARKSKYKEY") # Loading API key
        self.weather_days = []
        self.rains = []
    
    def getweather(self, coordinates, date_list):
        for date in date_list:
            response = requests.get(f'{self.url}{self.key}/{coordinates[0]},{coordinates[1]},{date}T15:00:00?exclude=minutely,hourly,daily,alerts,flags') # A way of making formatted API requests
            r = response.json()
            self.weather_days.append(r)
            
    def api_test(self, coordinates): # Testing the API to make sure it works before sending too many requests
        response = requests.get(f'{self.url}{self.key}/{coordinates[0]},{coordinates[1]},2012-03-31T15:00:00?exclude=minutely,hourly,daily,alerts,flags')
        if response.status_code == 200:
            print('Success!')
        else:
            print('Status Incorrect')
        return response.json()
        
            
    def rainmaker(self): # Fills the rain attribute with boolean values for the rain data
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
        
