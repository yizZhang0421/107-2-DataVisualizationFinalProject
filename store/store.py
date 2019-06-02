from bs4 import BeautifulSoup
import requests as req

from geopy import geocoders
g_api_key = 'AIzaSyBwHB-NjjRNdh3mLCmQbDSkqjN69be6xZc'   # 需啟動Geocoding API服務
g = geocoders.GoogleV3(g_api_key)


name_list=[]
lat_list=[]
long_list=[]
address_list=[]
for i in range(1, 6, 1):
    res = req.get('https://www.settour.com.tw/ec/retail/loadStore.html?region='+str(i))
    res_string='<tbody>'+res.text+'</tbody>'
    
    soup = BeautifulSoup(res_string, 'html.parser')
    datas=soup.find_all('tbody')[0]
    for j in datas.findChildren(recursive=False):
        name=j.findChildren(recursive=False)[0].text
        for k in (j.findChildren(recursive=False)[1]):
            address_tmp=k.replace('\n', '').replace(' ', '')
            address=''
            if address_tmp=='名古屋市中村區名3-13-267樓':
                address='名古屋市中村區名3-13'
                break
            for l in address_tmp:
                address+=l
                if l=='號':
                    break
            break
        place, (lat, long) = list(g.geocode(address, exactly_one=False))[0]
        name_list.append(name)
        lat_list.append(lat)
        long_list.append(long)
        address_list.append(address)


for i in range(5):
    print(name_list[i]+', '+address_list[i]+', '+str(lat_list[i])+', '+str(long_list[i]))


import folium

m = folium.Map(
        [23.770876, 120.934757], 
        zoom_start=8, 
        tiles='CartoDB positron', 
        max_bounds=False, 
        no_wrap = False)
for i in range(len(name_list)):
    popup=folium.Popup('<b>'+name_list[i]+'</b><br>'+address_list[i], max_width=300,min_width=200)
    folium.Marker([float(lat_list[i]), float(long_list[i])], popup=popup, tooltip='Click me!').add_to(m)
m.save('store.html')

import webbrowser
webbrowser.open("store.html")

