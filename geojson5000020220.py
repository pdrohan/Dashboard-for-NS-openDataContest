import pandas as pd
from geojson import Point, Feature, FeatureCollection, dump
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import json


with open(r'C:\Users\Owner\opendatacontest\canada_provinces.geojson') as f:
    data = json.load(f)

df = pd.read_csv("output.csv", header=0)

df2 = df.dropna(axis=0, how='any')
print(type(df2))
print(df2.columns())
# print(df.columns())
#dff2 = dff1.dropna('Address', how='any')

# print(dff2.columns())
# print(type(dff2))

# print(dff2['lat'])
# choro = px.choropleth(dff2, lat='lat', lon='lon',
#                       geojson=data,
#                         # locations='fips',
#                        color="Impact Grant",
#                        # projection='natural earth',
#                        title='Impact Grants',
#                        color_continuous_scale=px.colors.sequential.Plasma)
#
# choro.show()
# test = px.choropleth(dff2, lat='lat')