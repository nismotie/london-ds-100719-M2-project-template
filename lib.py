# You don't have to use these classes, but we recommend them as a good place to start!

class MongoHandler():
    pass

class Weather():
    def __init__(self):
        self.url = 'https://api.darksky.net/forecast/'
        self.key = os.getenv("DARKSKYKEY")
        self.weather_days = []
        self.rains = []
    
    def getweather(latitude, longitude, date_list):
        for date in date_list:
            response = requests.get(f'https://api.darksky.net/forecast/{self.key}/{latitude},{[longitude]},{date}T15:00:00?exclude=minutely,hourly,daily,alerts,flags')
            r = response.json()
            self.weather_days.append(r)
            
    def rainmaker(self):
        for weather_day in self.weather_days:
            if 'rain' in weather_day['currently']['icon']:
                self.rains.append(True)
            else:
                self.rains.append(False)

def make_df(table_name): # Takes the name of a table and makes a pandas dataframe from it
    return pd.read_sql_query(f"""SELECT * FROM {table_name}""", con)
        
