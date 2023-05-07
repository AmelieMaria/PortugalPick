import pandas as pd
import numpy as np 
import streamlit as st 
import time
from PIL import Image


st.set_page_config(
    page_title="Portugl Pick",
    page_icon="💌",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: black;'>Feedback corner</h1>", unsafe_allow_html=True)
st.write("<h3 style='text-align: center;'>💌</h3>", unsafe_allow_html=True)

st.write("#")

st.markdown(
    """
    <div style='text-align: center;'>
    
    What is the shortest word in English language that contains the letters: abcdef?
    
    Feedback!
    
    Don´t forget that feedback is one of the essential elements of good services.


    
    </div>
""",
    unsafe_allow_html=True
)

st.write("#")

st.markdown(
    """
    <div style='text-align: center;'>
    
    **Start the feedback journey**
    
    </div>
""",
    unsafe_allow_html=True
)

st.write("#")

options = st.multiselect(
    'Which city/ cities did you visit?',
    ['Evora', 'Braga', 'Coimbra', 'Aveiro'])

st.write("#")

options = st.multiselect(
    'Which type/ types did you search for?',
    ['Restaurant', 'Hotel', 'Attraction'])

st.write("#")

left, right = st.columns(2)
with left:
    
    st.radio('Did you actually visit the recommended place(s)?', options=['Yes', 'No', 'I don´t want to share'], horizontal=True)
with right:
    st.radio('Did you like the recommendation(s)?', options=['Yes', 'No', 'I don´t want to share'], horizontal=True)

st.write("#")
st.write("#")

nps = st.slider('How likely would you use our recommendation system again?', 0, 10, 0)
st.write(nps)
st.write("#")

txt = st.text_area('Anything you want to add?', '''

    ''')
st.write('Thanks for your comment:', (txt))
st.write("#")
st.write("#")

def simulate_computation():
    progress_text = "Submission in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text=progress_text)

    # Display "submitted" message.
    st.success('Submitted!')
    st.write("#")
    st.write("<p style='text-align: center;'><b>THANK YOU! We will carefully check your feedback in order to improve our processes.</b></p>", unsafe_allow_html=True)
    st.balloons()

# Add a submit button.
if st.button('Submit'):
    # Simulate computation.
    simulate_computation()
    time.sleep(0.5)
    obrigado = Image.open('obrigado.jpg')
    st.image(obrigado, use_column_width=True)
