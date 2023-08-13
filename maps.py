from pymongo import MongoClient
from math import radians, sin, cos, sqrt, atan2
import folium

client = MongoClient('mongodb+srv://sarvajeeth21417:HhJzePCNWYpkduSf@cluster0.laaviq9.mongodb.net/?retryWrites=true&w=majority')
db = client['Data']
ngos_collection = db['NGO']
donors_collection = db['Needy']

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  

    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

ngos = list(ngos_collection.find())
donors = list(donors_collection.find())

# Create a map centered at a specific location
map_center = [28.5398, 77.2490]  # Example coordinates (Bengaluru, India)
# m = folium.Map(location=map_center, zoom_start=10)
higher_zoom = 12  # You can adjust this value to set the desired zoom level
m = folium.Map(location=map_center, zoom_start=higher_zoom)

# Add markers for NGOs
# Add markers for NGOs
for ngo in ngos:
    folium.Marker(
        location=[ngo['location']['latitude'], ngo['location']['longitude']],
        popup=ngo['name'],  # You can customize the popup content
        icon=folium.Icon(color='green')
    ).add_to(m)

# Add markers for Donors
for donor in donors:
    folium.Marker(
        location=[donor['location']['latitude'], donor['location']['longitude']],
        popup=donor['name'],  # You can customize the popup content
        icon=folium.Icon(color='blue')
    ).add_to(m)


# Save the map to an HTML file
m.save('map.html')

print("Mapping complete.")
client.close()
