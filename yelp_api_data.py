# Client ID
# mim29haSx_7q21-2sAnzzw
#BevehA3zM_xfK9R10g9nzHv6w8USEUYjMvyixIa7VYMfsFaS41tuANxHZdJ4vtH7F7WZ3syUwpua-kv2lwskCFw2Sj783uDMxZDeEQWoGGyOi_4D8cObVp5S38YuYHYx
# API Key
import requests
import json
import pandas as pd
df = pd.read_csv("smallbusinessesHALI.csv")
# print(df.columns)

df1 = df.drop_duplicates(subset=["NS Small Business"])
df2 = df1['NS Small Business']
df22 = df1
df3 = df2.head(20)
df33 = df1.head(20)

#api stuff
API_KEY = 'BevehA3zM_xfK9R10g9nzHv6w8USEUYjMvyixIa7VYMfsFaS41tuANxHZdJ4vtH7F7WZ3syUwpua-kv2lwskCFw2Sj783uDMxZDeEQWoGGyOi_4D8cObVp5S38YuYHYx'
#ENDPOINT = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(business_id)
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

names_list = []
lat_list = []
long_list = []
address_list = []


for i, val in enumerate(df2):
    PARAMETERS = {'term': val,
                 'limit': 1,
                 'radius': 40000,
                 'location': 'Halifax, Nova Scotia'}
    response = requests.get(url=ENDPOINT,
                            params=PARAMETERS,
                            headers=HEADERS)
    business_data = response.json()
    #object2 = json.dumps(business_data, indent=3)
    busi = business_data["businesses"]
    print(busi)
    #print(busi)
    if not busi:
        name = "NaN"
        cords = "NaN"
        lat = "NaN"
        lon = "NaN"
        addy_list = "NaN"
        names_list.append(name)
        lat_list.append(lat)
        long_list.append(lon)
        address_list.append(addy_list)
        #print("NOT FOUND")
        next
    elif busi[0]['name'] == val:
        name = busi[0]['name']
        cords = busi[0]['coordinates']
        lat = cords['latitude']
        lon = cords['longitude']
        addy_list = busi[0]['location']['display_address']
        names_list.append(name)
        lat_list.append(lat)
        long_list.append(lon)
        address_list.append(addy_list)
    else:
        name = "NaN"
        lat = "NaN"
        lon = "NaN"
        addy_list = "NaN"
        names_list.append(name)
        lat_list.append(lat)
        long_list.append(lon)
        address_list.append(addy_list)
        #print("Names dont match")



# print(names_list)
# print(lat_list)
# print(long_list)
# print(address_list)

df22.insert(0, "Name", names_list, True)
df22.insert(0, "lon", long_list, True)
df22.insert(0, "lat", lat_list, True)
df22.insert(0, "Address", address_list, True)
df22.to_csv('output.csv', index=False)

# chloro_data = df22.dropna(0, how='any')




