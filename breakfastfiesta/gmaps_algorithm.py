import pandas as pd
import gmaps
from datetime import datetime
from ipywidgets.embed import embed_minimal_html
apikey = 'AIzaSyAdzwCpBzLDrhbtsZbFUDNKPJA0zIpshic'
now = datetime.now()


start = (25.86313861266461, -80.247161730114)
end = start


# read file
df = pd.read_csv('BreakfastFiestaOrderLog_latlong.csv', usecols = ['Cliente', 'Orden', 'Delivery Address', 'Latitude', 'Longitude'], index_col='Cliente')

# remove all orders that will be picked up
df = df[~df['Delivery Address'].isin(['Pickup'])]

# drop blank cells
df = df.dropna()

df = df.head(22)



waypoints = list(zip(df['Latitude'],df['Longitude']))

gmaps.configure(api_key=apikey)

fig = gmaps.figure()

layer = gmaps.directions.Directions(start, end, waypoints = waypoints, optimize_waypoints=True, mode='car', api_key=apikey, departure_time=now)

fig.add_layer(layer)

embed_minimal_html('export.html', views=[fig])

