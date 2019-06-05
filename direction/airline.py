import folium
some_map = folium.Map(location=[25, 122], zoom_start=10)

airsport_coordinate=[[25.0772482, 121.2322312], [34.4368344, 135.242957]]
folium.Marker(airsport_coordinate[0], popup=folium.Popup('<b>桃園國際機場</b>', max_width=300,min_width=200)).add_to(some_map)
folium.Marker(airsport_coordinate[1], popup=folium.Popup('<b>關西國際機場</b>', max_width=300,min_width=200)).add_to(some_map)
folium.PolyLine(locations=[airsport_coordinate[0], airsport_coordinate[1]], color='blue').add_to(some_map)

some_map.save('airline.html')
import webbrowser
webbrowser.open("airline.html")