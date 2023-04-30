import phonenumbers
import folium
from phonenumbers import geocoder

number=""

sanNumber=phonenumbers.parse(number)
yourlocation=geocoder.description_for_number(sanNumber,"en")
print(yourlocation)
from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

key='ee1d975c65734ffe8b258e70e193ec4b'

geocoder=OpenCageGeocode(key)
query=str(yourlocation)
results = geocoder.geocode(query)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_star=9)

folium.Marker([lat,lng],popup=yourlocation).add_to(myMap)

myMap.save("mylocation.html")
