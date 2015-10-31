# Using the Haversine formula for geographic Great Circle Distance
#
# As per https://en.wikipedia.org/wiki/Haversine_formula

from numpy import cos,radians,sin,sqrt,power,arcsin

def distance(lat1, long1, lat2, long2):
    radius = 6371 # radius of the earth in km, roughly https://en.wikipedia.org/wiki/Earth_radius

    # Lat,long are in degrees but we need radians
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    long1 = radians(long1)
    long2 = radians(long2)

    dlat = lat2-lat1
    dlon = long2-long1

    a = power(sin(dlat/2),2) + cos(lat1)*cos(lat2)*power(sin(dlon/2),2)
    distance = 2 * radius * arcsin(sqrt(a))

    return distance

