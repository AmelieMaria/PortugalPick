import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import requests
import streamlit.components.v1 as components
import json
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import folium_static


st.set_page_config(
    page_title="Portugl Pick",
    page_icon="🌍",
)

st.sidebar.subheader("Notes")
notes = st.sidebar.text_area("Enter your notes here")

st.markdown("<h1 style='text-align: center; color: black;'>Mapping you around</h1>", unsafe_allow_html=True)

st.write("#")
st.write("<h3 style='text-align: center;'>🌎     🌍      🌏</h3>", unsafe_allow_html=True)
st.write("#")

st.markdown(
    """
    <div style='text-align: center;'>
    
    We've created a map that not only shows you where to find the best restaurants and hotels, but also how far away they are. 
    No more guessing games or endless walking...unless you're into that sort of thing. 
    So get your walking shoes ready and start exploring!
    
    **Check the distance to your preferred location**  
    
    </div>
""",
unsafe_allow_html=True
)
st.write("#")

def get_lat_long_from_address(address):
   locator = Nominatim(user_agent='myGeocoder')
   location = locator.geocode(address)
   return location.latitude, location.longitude

# Create a form for the user to input the starting address
st.markdown("<h3 style='text-align: center; color: black;'>Starting address</h3>", unsafe_allow_html=True)
address1 = st.text_input("Enter your starting address:")
if st.button("Submit 1", key="submit1"):
    if address1:
        # Call the get_lat_long_from_address function with the user's starting address
        lat1, long1 = get_lat_long_from_address(address1)

        # Display the latitude and longitude on the app
        st.write("Latitude:", lat1)
        st.write("Longitude:", long1)
    else:
        st.write("Please enter a starting address.")

st.write("#")

# Create a form for the user to input the destination address
st.markdown("<h3 style='text-align: center; color: black;'>Destination address</h3>", unsafe_allow_html=True)
address2 = st.text_input("Enter your destination address:")
if st.button("Submit 2", key="submit2"):
    if address2:
        # Call the get_lat_long_from_address function with the user's destination address
        lat2, long2 = get_lat_long_from_address(address2)

        # Display the latitude and longitude on the app
        st.write("Latitude:", lat2)
        st.write("Longitude:", long2)
    else:
        st.write("Please enter a destination address.")

st.write("#")

st.markdown("<h3 style='text-align: center; color: black;'>Insert data</h3>", unsafe_allow_html=True)

st.write("#")

origin_lat = st.number_input("Enter the latitude of the origin point:")
origin_lon = st.number_input("Enter the longitude of the origin point:")
destination_lat = st.number_input("Enter the latitude of the destination point:")
destination_lon = st.number_input("Enter the longitude of the destination point:")

url = f"https://api.mapbox.com/directions/v5/mapbox/driving-traffic/{origin_lon},{origin_lat};{destination_lon},{destination_lat}?access_token=pk.eyJ1IjoiYW1lbGllbWFyeSIsImEiOiJjbGVtcmRqZWkweHh1M29vZGI2cmNqbmNvIn0.YF6OiMX4dNLNF3XLr2x3qA"
response = requests.get(url)
data = response.json()

if "routes" not in data:
    st.error("No route found. Please try again with different locations.")
else:
    duration = data["routes"][0]["duration"] / 60.0
    hours, minutes = divmod(duration, 60)
    if int(hours) > 0:
        st.write(f"**Estimated travel time: {int(hours)} hour{'s' if int(hours) > 1 else ''} and {int(minutes)} minute{'s' if int(minutes) > 1 else ''}**")
    else:
        st.write(f"**Estimated travel time: {int(minutes)} minute{'s' if int(minutes) > 1 else ''}**")


def get_directions_response(origin_lat, origin_lon, destination_lat, destination_lon, mode='drive'):
    url = "https://route-and-directions.p.rapidapi.com/v1/routing"
    key = "2389c5e548msheede94ba7f10e89p1f6ad3jsn064f94a9779d"
    host = "route-and-directions.p.rapidapi.com"
    headers = {"X-RapidAPI-Key": key, "X-RapidAPI-Host": host}
    querystring = {"waypoints":f"{str(origin_lat)},{str(origin_lon)}|{str(destination_lat)},{str(destination_lon)}","mode":mode}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def create_map(response):
    # use the response
    mls = response.json()['features'][0]['geometry']['coordinates']
    points = [(i[1], i[0]) for i in mls[0]]
    m = folium.Map()
    # add marker for the start and ending points
    for point in [points[0], points[-1]]:
        folium.Marker(point, icon=folium.Icon(color="green", icon="flag")).add_to(m)
    # add the lines
    folium.PolyLine(points, weight=3, opacity=1).add_to(m)
    # create optimal zoom
    df = pd.DataFrame(mls[0]).rename(columns={0:'Lon', 1:'Lat'})[['Lat', 'Lon']]
    sw = df[['Lat', 'Lon']].min().values.tolist()
    ne = df[['Lat', 'Lon']].max().values.tolist()
    m.fit_bounds([sw, ne])
    return m


response = get_directions_response(origin_lat, origin_lon, destination_lat, destination_lon)
m = create_map(response)
st.markdown("**This is the way to follow:**")
folium_static(m)

# download map as a picture: m.save("filename.png")
# also connect to print and download output!
# make customer input easier