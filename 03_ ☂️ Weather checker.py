import streamlit as st
import pandas as pd
import urllib.request
import sys
import requests
import time


st.set_page_config(
    page_title="Portugl Pick",
    page_icon="🌦",
)

st.markdown("<h1 style='text-align: center; color: black;'>Weather checker</h1>", unsafe_allow_html=True)

st.write("#")

st.markdown(
    """
    <div style='text-align: center;'>
    🌈🌈🌈🌈🌈🌈🌈
    
    The weather can be quite clever,
    Sometimes sunny, sometimes never,
    Raindrops falling, clouds so gray,
    Wind so strong it blows away.
    
    **Check it out**  
    
    </div>
""",
    unsafe_allow_html=True
)
st.write("#")

url = "https://weatherapi-com.p.rapidapi.com/current.json"
headers = {
    "X-RapidAPI-Key": "2389c5e548msheede94ba7f10e89p1f6ad3jsn064f94a9779d",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

# function to make the API request
def get_current_weather(location):
    querystring = {"q": location}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

# Define the Streamlit app
def app():
    # Create a text input for the user to enter their location
    location = st.text_input("Enter the location you want to go")
    st.write("#")
    # If the user has entered a location, make the API request and display the results
    if location:
        weather_data = get_current_weather(location)

        #st.write("Location:", weather_data["location"]["name"])
        temperature = st.slider("Current temperature (°C)", min_value=float(weather_data["current"]["temp_c"])-10, max_value=float(weather_data["current"]["temp_c"])+10, value=float(weather_data["current"]["temp_c"]))
        if temperature < 10:
            color = "blue"
            st.write("<p style='text-align: center;'><b>Seems cold, better take a jacket with you! 🥶</b></p>", unsafe_allow_html=True)
            st.write("<p style='text-align: center;'><b>Pack list:</b> warm jacket, scarf, closed shoes, beanie</p>", unsafe_allow_html=True)

        elif temperature < 20:
            color = "green"
            st.write("<p style='text-align: center;'><b>Not too hot and not too cold, the breeze is gentle, the sun's not bold 🌻</b></p>", unsafe_allow_html=True)
            st.write("<p style='text-align: center;'><b>Pack list:</b> soft jacket, hoodie, shirt, closed shoes</p>", unsafe_allow_html=True)

        else:
            color = "orange"
            st.write("<p style='text-align: center;'><b>Amazing weather, don´t forget your bathing clothes 🌴</b></p>", unsafe_allow_html=True)
            st.write("<p style='text-align: center;'><b>Pack list:</b> shirt, shorts, sun screen</p>", unsafe_allow_html=True)
        st.write("#")
        st.write("Location:", weather_data["location"]["name"])
        time.sleep(2.0)
        st.write("Current temperature:", weather_data["current"]["temp_c"], "°C")
        time.sleep(2.0)
        st.write("Condition:", weather_data["current"]["condition"]["text"])


# Run the Streamlit app
if __name__ == '__main__':
    app()


