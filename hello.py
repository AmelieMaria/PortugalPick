import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image


st.set_page_config(
    page_title="Portugl Pick",
    page_icon="🏖",
)


#selected = option_menu(
    #menu_title=None,
    #options= ["Home", "Get recommends", "Weather checker", "Map me", "Feedback"],
    #icons= ["house","book","brightness-high", "globe","envelope"],
    #default_index=0,
    #orientation="horizontal",)

st.markdown("<h1 style='text-align: center; color: black;'>☀️☀️☀️</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>🇵🇹 Welcome at Portugal Pick 🇵🇹</h1>", unsafe_allow_html=True)
st.write("#")
image_porti = Image.open('Porti_love.jpg')
st.image(image_porti, use_column_width=True)
st.write("#")
st.markdown(
    """
    <div style='text-align: center;'>
    
    Welcome to our Portugal travel guide! 
    If you're planning a trip around Portugal, you've come to the right place. 
    Our website is your one-stop-shop for all things travel in Portugal.
    
    **Let us be your travel guide and unlock the coolest hotel, restaurant, and attraction recommendations in Portugal!** ☀️
    </div>
""",
unsafe_allow_html=True
)

st.write("#")
st.markdown("<h3 style='text-align: center; color: black;'>What we offer:</h3>", unsafe_allow_html=True)
st.write("#")
st.markdown("<p style='text-align: center; color: black;'>A guide through Evora, Aveiro, Braga and Coimbra for:</p>", unsafe_allow_html=True)
st.write("#")

left, right = st.columns(2)
with left:
    st.markdown("<p style='text-align: center; color: black;'>Hotel recommendations 🏩</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black;'>Attractions/ adventures 🏰</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black;'>Checking the weather of the location before going</p>", unsafe_allow_html=True)

with right:
    st.markdown("<p style='text-align: center; color: black;'>Dinner/ lunch and breakfast spots 🍝</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black;'>Checking distances to your preferred restaurant, hotel or attraction</p>", unsafe_allow_html=True)

st.write("#")
st.write("#")
st.markdown("<h3 style='text-align: center; color: black;'>Get started 🛫</h3>", unsafe_allow_html=True)

# pastel bild will be hidden
#left, right = st.columns(2)
#with left:
    #st.write("#")
#with right:
    #image_p = Image.open('pastel.jpg')
    #st.image(image_p, width = 40)
