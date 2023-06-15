import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

import folium
from opencage.geocoder import OpenCageGeocode

number = input("phone number :")

phoneNumber = phonenumbers.parse(number)

Key = "ab4bfe453b29491c992b8501f41b9fb5"

yourLocation = geocoder.description_for_number(phoneNumber,"en")
print("location : "+yourLocation)

service = carrier.name_for_number(phoneNumber,"en")
print("service provider : "+service)

geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(loction=[lat,lng],zoom_start = 9)

folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)

myMap.save("Location.html")