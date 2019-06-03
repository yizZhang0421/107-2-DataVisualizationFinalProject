search_list=[
        'Japan',
        'Korea',
        'China',
        'Thailand',
        'Malaysia',
        'Singapore',
        'Indonesia',
        'Philippines',
        'Vietnam',
        'Cambodia',
        'Myanmar',
        'Laos',
        'United States',
        'Canada',
        'United Kingdom',
        'France',
        'Netherlands',
        'Belgium',
        'Luxembourg',
        'Germany',
        'Switzerland',
        'Austria',
        'Monaco',
        'Czech Republic',
        'Slovakia',
        'Hungary',
        'Croatia',
        'Poland',
        'Estonia',
        'Lithuania',
        'Latvia',
        'Bulgaria',
        'Romania',
        'Vatican',
        'Portugal',
        'Spain',
        'Greece',
        'Malta',
        'Sweden',
        'Finland',
        'Denmark',
        'Norway',
        'Iceland',
        'Russia',
        'Australia',
        'New Zealand',
        'India',
        'Nepal',
        'Maldives',
        'Sri Lanka',
        'Bhutan',
        'Turkey',
        'Egypt',
        'United Arab Emirates',
        'Iran',
        'Israel',
        'Kenya',
        'South Africa',
        'Swaziland',
        'Namibia',
        'Morocco',
        'Tunisia',
        'Taiwan'
        ]
import country_converter as coco
ISO_A3_code = coco.convert(names=search_list, to='ISO3')

import json, requests
contries_pologon=json.loads(requests.get('https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson').text)
needed_contries_pologon_data={
        "type": "FeatureCollection",
        "features": []
        }
for i in contries_pologon['features']:
    try:
        ISO_A3_code.index(i['properties']['ISO_A3'])
        needed_contries_pologon_data['features'].append(i)
    except:
        pass
print('Finished: '+str(len(needed_contries_pologon_data['features'])==len(ISO_A3_code)))

import folium

m = folium.Map(
        [52.237049, 21.017532], 
        zoom_start=2, 
        tiles='CartoDB positron', 
        max_bounds=False, 
        no_wrap = False)
m.choropleth(
        geo_data=needed_contries_pologon_data,
        line_color='#FC0000',
        fill_color='#EA5959',
        fill_opacity=0.5)

m.save('destination.html')

import webbrowser
webbrowser.open("destination.html")

