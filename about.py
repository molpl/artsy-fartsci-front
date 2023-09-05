
import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64



# Set the page title and icon



st.image("assets/Untitled_design-6-removebg-preview-removebg-preview.png")

st.header('About Artsy-Fartsci')



# Provide the path to your logo image file within quotation marks



# st.set_page_config(
#     page_title="Artsy-FartSci: A Data Science Project"
# )

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('assets/img1.wallspic.com-sky-water-blue-azure-watercolorpainting-4000x6000.jpg')




# with st.sidebar.container():
#     st.image("image/Artsy Fartsci.png")


# st.image("assets/Untitled_design-6-removebg-preview-removebg-preview.png")


# link css

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


st.subheader('What does artsy fartsci do?')
             
