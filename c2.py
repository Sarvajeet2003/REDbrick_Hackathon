from django.shortcuts import render
from django.db.models import F
from math import radians, sin, cos, sqrt, atan2

from .models import NGO, Donor

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


def map_Donor_to_ngo(request):
    ngos = NGO.objects.all()
    individuals = Donor.objects.all()

    for individual in individuals:
        nearest_ngo = None
        nearest_distance = float('inf')

        for ngo in ngos:
            distance = calculate_distance(
                individual.location['latitude'],
                individual.location['longitude'],
                ngo.location['latitude'],
                ngo.location['longitude']
            )
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_ngo = ngo

        individual.matched_ngo = nearest_ngo
        individual.save()

        nearest_ngo.matched_Donor.add(individual)
        nearest_ngo.save()

    return render(request, 'mapping_complete.html')
