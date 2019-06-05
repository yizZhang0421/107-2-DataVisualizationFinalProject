# https://medium.com/@bobhaffner/folium-lines-with-arrows-25a0fe88e4e
# https://tour.settour.com.tw/product/GFG0000010620

import folium

def get_bearing(p1, p2):
    
    long_diff = np.radians(p2.lon - p1.lon)
    
    lat1 = np.radians(p1.lat)
    lat2 = np.radians(p2.lat)
    
    x = np.sin(long_diff) * np.cos(lat2)
    y = (np.cos(lat1) * np.sin(lat2) 
        - (np.sin(lat1) * np.cos(lat2) 
        * np.cos(long_diff)))
    bearing = np.degrees(np.arctan2(x, y))
    
    # adjusting for compass bearing
    if bearing < 0:
        return bearing + 360
    return bearing

def get_arrows(locations, color='blue', size=6, n_arrows=3):
    Point = namedtuple('Point', field_names=['lat', 'lon']) 
    
    # creating point from our Point named tuple
    p1 = Point(locations[0][0], locations[0][1])
    p2 = Point(locations[1][0], locations[1][1])
    
    # getting the rotation needed for our marker.  
    # Subtracting 90 to account for the marker's orientation
    # of due East(get_bearing returns North)
    rotation = get_bearing(p1, p2) - 90
    
    # get an evenly space list of lats and lons for our arrows
    # note that I'm discarding the first and last for aesthetics
    # as I'm using markers to denote the start and end
    arrow_lats = np.linspace(p1.lat, p2.lat, n_arrows + 2)[1:n_arrows+1]
    arrow_lons = np.linspace(p1.lon, p2.lon, n_arrows + 2)[1:n_arrows+1]
    
    arrows = []
    
    #creating each "arrow" and appending them to our arrows list
    for points in zip(arrow_lats, arrow_lons):
        arrows.append(folium.RegularPolygonMarker(location=points, 
                      fill_color=color, number_of_sides=3, 
                      radius=size, rotation=rotation).add_to(some_map))
    return arrows

from math import sin, cos, sqrt, atan2, radians
def distance_between_coordinate(p1, p2):
    R = 6373.0
    lat1 = radians(p1[0])
    lon1 = radians(p1[1])
    lat2 = radians(p2[0])
    lon2 = radians(p2[1])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

import numpy as np
from collections import namedtuple
# using omaha coordinates 
center_lat = 34.42889
center_lon = 135.24056
# generating a couple of random latlongs in the omaha area

day1=['33758桃園市大園區航站南路9號', '1 Senshukukokita, Izumisano-shi, Osaka 549-0001日本', '1 Chome-9-15 Shinkitano, Yodogawa Ward, Osaka, 532-0025日本']
day2=['1 Chome-9-15 Shinkitano, Yodogawa Ward, Osaka, 532-0025日本', 'Saganakanoshimacho, Ukyo Ward, Kyoto, 616-8383日本', '294 Kiyomizu, Higashiyama Ward, Kyoto, 605-0862日本', '2 Chome-221 Kiyomizu, Higashiyama Ward, Kyoto, 605-0862日本', '68 Fukakusa Yabunouchicho, Fushimi Ward, Kyoto, 612-0882日本', '600-1 Kabatacho, Tenri, Nara 632-0084日本']
day3=['600-1 Kabatacho, Tenri, Nara 632-0084日本', '4-2051 Higashimaikocho, Tarumi Ward, Kobe, Hyogo 655-0047日本', 'Yamamotodori, Chuo Ward, Kobe, Hyogo 650-0003日本', '1 Chome-6-1 Higashikawasakicho, Chuo Ward, Kobe, Hyogo 650-0044日本', '6 Chome-10-1 Minatojima Nakamachi, Chuo Ward, Kobe, Hyogo 650-0046日本']
day4=['6 Chome-10-1 Minatojima Nakamachi, Chuo Ward, Kobe, Hyogo 650-0046日本', '2 Chome-1-33 Sakurajima, Konohana Ward, Osaka, 554-0031日本', '1 Chome-1-111 Sakurajima, Konohana Ward, Osaka, 554-0031日本']
day5=['1 Chome-1-111 Sakurajima, Konohana Ward, Osaka, 554-0031日本', '1 Osakajo, Chuo Ward, Osaka, 540-0002日本', '1 Chome-2-4 Nishishinsaibashi, Chuo Ward, Osaka, 542-0086日本', '1 Senshukukokita, Izumisano-shi, Osaka 549-0001日本', '33758桃園市大園區航站南路9號']
schedule=[day1, day2, day3, day4, day5]
route_color=['blue', 'green', 'orange', 'purple', 'yellow']

some_map = folium.Map(location=[center_lat, center_lon], zoom_start=10)

from geopy import geocoders
g_api_key = 'AIzaSyBwHB-NjjRNdh3mLCmQbDSkqjN69be6xZc' # 需啟動Geocoding API服務
g = geocoders.GoogleV3(g_api_key)

for i in schedule:
    for j in range(1, len(i)):
        a=i[j-1]
        place, (lat, long) = list(g.geocode(a, exactly_one=False))[0]
        p1 = [lat, long]
        b=i[j]
        place, (lat, long) = list(g.geocode(b, exactly_one=False))[0]
        p2 = [lat, long]
        if a=='33758桃園市大園區航站南路9號' and b=='1 Senshukukokita, Izumisano-shi, Osaka 549-0001日本':
            p1[1]-=0.001
            p2[1]-=0.001
        if b=='33758桃園市大園區航站南路9號' and a=='1 Senshukukokita, Izumisano-shi, Osaka 549-0001日本':
            p1[1]+=0.001
            p2[1]+=0.001
        folium.Marker(p1).add_to(some_map)
        folium.Marker(p2).add_to(some_map)
        folium.PolyLine(locations=[p1, p2], color=route_color[schedule.index(i)]).add_to(some_map)
        arrows = get_arrows(locations=[p1, p2], n_arrows=int(distance_between_coordinate(p1, p2)//10))
        for arrow in arrows:
            arrow.add_to(some_map)

some_map.save('direction.html')
import webbrowser
webbrowser.open("direction.html")