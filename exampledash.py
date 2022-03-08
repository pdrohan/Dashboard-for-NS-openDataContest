import pandas as pd
from geojson import Point, Feature, FeatureCollection, dump
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

dff1 = pd.read_csv("canada_provinces.csv")
print(dff1.columns)

#https://geoffboeing.com/2015/10/exporting-python-data-geojson/

# def df_to_geojson(df, properties, lat='lat', lon='lon'):
#     geojson = {'type':'FeatureCollection', 'features':[]}
#     for _, row in df.iterrows():
#         feature = {'type':'Feature',
#                    'properties':{},
#                    'geometry':{'type':'Point',
#                                'coordinates':[]}}
#         feature['geometry']['coordinates'] = [row[lon],row[lat]]
#         for prop in properties:
#             feature['properties'][prop] = row[prop]
#         geojson['features'].append(feature)
#     return geojson
#
# cols = ['Address', 'lat', 'lon']
# geojson = df_to_geojson(dff2, cols)
#
# with open(r'C:\Users\Owner\opendatacontest\testerr.geojson', 'w') as f:
#    dump(geojson, f)
#
#    choro = px.choropleth(dff2, lat=dff2['lat'], lon=dff2['lon'],
#                        color="Impact Grant",
#                        # projection='natural earth',
#                        title='Life Expectancy by Year',
#                        color_continuous_scale=px.colors.sequential.Plasma)
#
#    choro.show()