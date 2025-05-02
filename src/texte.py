from geopy.geocoders import Nominatim

# Use aqui para pegar a cordenada
geolocator = Nominatim(user_agent="texte")

local = geolocator.geocode("rio de janeiro")

print(f"{local.latitude}, {local.longitude}")