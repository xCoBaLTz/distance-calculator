import googlemaps
from datetime import datetime

def distance(self, origin, destination)
  self.origin = origin
  self.destination = destination
  
  gmaps = googlemaps.Client(key='AIzaSyDBubBQL2tNO9bKjv5gYOLBcCeRghAOi7o')
  distance-matrix = gmaps.distance_matrix(self.origin, self.destination)
  
  return distance-matrix['rows'][0]['elements'][0]['distance']['text']

distance("Ryerson University, Toronto ON", "Harvard University, Cambridge MA")
