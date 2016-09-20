import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDBubBQL2tNO9bKjv5gYOLBcCeRghAOi7o')
distance = gmaps.distance_matrix("Ryerson University, Toronto ON", "Harvard University, Cambridge MA")

print distance['rows'][0]['elements'][0]['distance']['text']
