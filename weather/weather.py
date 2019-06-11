from bs4 import BeautifulSoup
soup = BeautifulSoup(open('table.txt', 'r').read(), 'html.parser')

# https://www.accuweather.com/en/jp/konohana-ku/219599/june-weather/219599?monyr=6/1/2019&view=table
open('table.txt', 'w').write(soup.prettify())
datas=soup.find_all('tbody')[0]

hi_list=[]
lo_list=[]
day_list=[]
precip_list=[]

day=1
for i in datas.findChildren(recursive=False):
    HiLo=i.findChildren(recursive=False)[1].text.split('/')
    hi=float(HiLo[0].replace('°', '').replace('\n', '').replace(' ', ''))
    lo=float(HiLo[1].replace('°', '').replace('\n', '').replace(' ', ''))
    hi_list.append(hi)
    lo_list.append(lo)
    day_list.append(day)
    day+=1
for i in datas.findChildren(recursive=False):
    precip=float(i.findChildren(recursive=False)[2].text.replace('\n', '').replace(' ', '').replace('mm', ''))
    precip_list.append(precip)
    
import plotly.graph_objs as go
import plotly.io as pio

#===== temperature =====#
trace0 = go.Scatter(
    x = day_list,
    y = hi_list,
    name = 'High',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
trace1 = go.Scatter(
    x = day_list,
    y = lo_list,
    name = 'Low',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
data = [trace0, trace1]
layout = dict(title = 'June temperature of Konohana-ku in Japan.',
              xaxis = dict(title = 'Day', tickmode='linear'),
              yaxis = dict(title = 'Temperature (degrees C)'),
              )
fig = dict(data=data, layout=layout)
pio.write_image(fig, 'temperature.png')



#===== precipitation =====#
trace1 = go.Scatter(
    x = day_list,
    y = precip_list,
    name = 'Precip',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
data = [trace1]
layout = dict(title = 'June mm of precipitation of Konohana-ku in Japan.',
              xaxis = dict(title = 'Day', tickmode='linear'),
              yaxis = dict(title = 'Quantity (mm)'),
              )
fig = dict(data=data, layout=layout)
pio.write_image(fig, 'precipitation.png')

