import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time
import base64
timestr = time.strftime("%Y%m%d-%H%M%S")

from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

final_portugal_dates = pd.read_csv('tripadvisornearbysearch.csv')


st.set_page_config(
    page_title="Portugl Pick",
    page_icon="🧳",
)
# due to download: notes bar not necessary anymore
#st.sidebar.subheader("Notes")
#notes = st.sidebar.text_area("Enter your notes here")

st.markdown("<h1 style='text-align: center; color: black;'>✨ Recommendations ✨</h1>", unsafe_allow_html=True)

st.write("#")


st.markdown(
    """
    <div style='text-align: center;'>
        <p><strong>Welcome to our wacky world of restaurant, trip, and hotel recommendations!</strong></p>
        <p>Our team of expert goofballs have traveled far and wide to personally review each and every recommendation we provide. 
        So you can trust that our suggestions are of the highest quality.</p>
        <p>So buckle up and get ready for a wild ride. 
        Let us help you plan your next adventure!</p>
    </div>
""",
    unsafe_allow_html=True
)

st.write("#")

st.write("<h3 style='text-align: center;'>Let´s get started</h3>", unsafe_allow_html=True)

st.write("#")

city_data = {
    'Evora': {'image_path': 'evora_temple.jpg', 'text': 'Watch the old Roman temple in Evora'},
    'Coimbra': {'image_path': 'Coimbra_Igreja.jpg', 'text': 'Do you agree that that\'s a stunning church in the middle of Coimbra?'},
    'Braga': {'image_path': 'Braga_view.jpg', 'text': 'Imagine enjoying a glass of wine at this viewpoint in Braga'},
    'Aveiro': {'image_path': 'Aveiro_boat.jpg', 'text': 'No need to go to Venice when you can have a boat tour through Aveiro'},
}

# Get the selected city from the user
city = st.selectbox('Where do you want to go?', list(city_data.keys()))

# Display the picture and text for the selected city
image_path = city_data[city]['image_path']
image = Image.open(image_path)
st.image(image, caption=city_data[city]['text'])

# Filter the dataframe based on the selected city and types
filtered_df = final_portugal_dates[(final_portugal_dates['city'] == city.title()) &
                                    (final_portugal_dates['type'].isin(['attraction', 'restaurant', 'hotel']))]

# Calculate the number of attractions, hotels, and restaurants
num_attractions = filtered_df[filtered_df['type'] == 'attraction']['name'].nunique()
num_hotels = filtered_df[filtered_df['type'] == 'hotel']['name'].nunique()
num_restaurants = filtered_df[filtered_df['type'] == 'restaurant']['name'].nunique()

# Display the results in a box with bold text
st.write("**Great choice!**")
st.success(f"We found **{num_attractions}** attractions to recommend in {city}.")
st.success(f"{city} has **{num_hotels}** hotels that would be a great fit.")
st.success(f"Eating out is not a problem with **{num_restaurants}** restaurants in {city}.")
filtered_df = final_portugal_dates[(final_portugal_dates['city'] == city.title()) &
                                    (final_portugal_dates['type'].isin(['attraction', 'restaurant', 'hotel']))]

st.write("#")

type = st.selectbox('What do you want to find first?', ['attraction', 'restaurant', 'hotel'])

filtered_data = final_portugal_dates[(final_portugal_dates['city'] == city) & (final_portugal_dates['type'] == type)]

st.write("#")
st.write("<p style='text-align: center;'><b>Wise idea...</b></p>", unsafe_allow_html=True)
st.write("#")

st.write("<h3 style='text-align: center;'>Our recommendations are:</h3>", unsafe_allow_html=True)

#st.dataframe(filtered_data)

st.write("#")


if len(filtered_data) == 0:
    st.write('No results found.')
else:
    #for index, row in filtered_data.head(5).iterrows():
        #st.write(f"**{row['name']}**\n, {row['complete_address']}")
    
    unique_names = set()  # keep track of unique names that have been written
    count = 0  # keep track of number of outputs
    for index, row in filtered_data.sample(5).iterrows():
        if row['name'] not in unique_names:
            # write the row to the output
            st.write(f"**{row['name']}**, \n{row['complete_address']}\n")
            unique_names.add(row['name'])  # add the name to the set of unique names
            count += 1
            if count == 5:  # break the loop after 5 outputs
                break
st.write("#")
st.write("<p style='text-align: center;'><b>What about anything else?</b></p>", unsafe_allow_html=True)

st.write("#")
st.write("#")
def text_downloader(raw_text):
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = "new_text_file_{}_.txt".format(timestr)
    st.markdown("#### Download tips ###")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'
    st.markdown(href, unsafe_allow_html=True)

my_text = st.text_area("Save your recommends here")
if st.button("Save"):
    st.write(my_text)
    text_downloader(my_text)

st.write("#")

st.write("<h3 style='text-align: center;'>We wish you a safe travel!</h3>", unsafe_allow_html=True)
#image_leo = Image.open('happy-holidays.jpg')
#st.image(image_leo, caption='Enjoy your day 🎉', width=250, use_column_width=True)
st.write("<h3 style='text-align: center;'>🚗 🚌 🛵</h3>", unsafe_allow_html=True)
st.write("#")
st.write("<p style='text-align: center;'><b>P.S.:</b> You can check the way to your destination or the weather in the following pages</p>", unsafe_allow_html=True)


# if its a restaurant: make an appointment and chose the date?
# add reviews from Tripadvisor
# print output on a map