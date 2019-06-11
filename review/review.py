import requests as req
res=req.get('https://www.tripresso.com/survey/agency')
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
soup = soup.findAll("section", {"class": "travelEvalList"})[0].findAll("div", {"class": "row"})[0]

name=[]
star=[]
comments_count=[]
bubble_color=[]
for company_div in soup.findChildren(recursive=False):
    company_data=company_div.findAll("div", {"rel": "for_schema"})[0].text.strip().split()
    name.append(company_data[0])
    star.append(float(company_data[1])/20)
    comments_count.append(int(company_data[4]))
    bubble_color.append('rgb(93, 164, 214)' if company_data[0]!='東南旅遊' else 'rgb(255, 144, 14)')

import plotly.graph_objs as go
import plotly.io as pio

test=[i/10 for i in comments_count]
trace0 = go.Scatter(
    x=name,
    y=star,
    mode='markers',
    marker=dict(
        color=bubble_color,
        size=test,
    )
)
data = [trace0]
fig = dict(data=data)
pio.write_image(dict(data=data), 'review.png')
