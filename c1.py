from pymongo import MongoClient
from math import radians, sin, cos, sqrt, atan2

client = MongoClient('mongodb+srv://sarvajeeth21417:HhJzePCNWYpkduSf@cluster0.laaviq9.mongodb.net/?retryWrites=true&w=majority')
db = client['Data']
ngos_collection = db['NGO']
donors_collection = db['Donor']  # Changed the collection name

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
donors = list(donors_collection.find())  # Changed the collection name

for donor in donors:  # Changed variable names and collection references
    nearest_ngo = None
    nearest_distance = float('inf')

    for ngo in ngos:
        distance = calculate_distance(
            donor['location']['latitude'],  # Adjusted the field names
            donor['location']['longitude'],  # Adjusted the field names
            ngo['location']['latitude'],
            ngo['location']['longitude']
        )
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_ngo = ngo

    donors_collection.update_one(
        {'_id': donor['_id']},
        {'$set': {'matched_ngo': nearest_ngo}}
    )

    ngos_collection.update_one(
        {'_id': nearest_ngo['_id']},
        {'$addToSet': {'matched_donor': donor}}  # Changed the field name
    )

print("Mapping complete.")
client.close()
