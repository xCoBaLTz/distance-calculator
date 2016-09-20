import googlemaps
from datetime import datetime

def distance(orig, dest):
  origin = orig
  destination = dest
  gmaps = googlemaps.Client(key='AIzaSyDBubBQL2tNO9bKjv5gYOLBcCeRghAOi7o')
  distance_matrix = gmaps.distance_matrix(origin, destination)
  return (distance_matrix['rows'][0]['elements'][0]['distance']['text'])

#enter the origin and destination of the place you wish to recieve a distance of
print (distance("Ryerson University, Toronto ON", "Harvard University, Cambridge MA"))
