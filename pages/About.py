
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

st.text(
    '''
    Artsy-fartsci is an app that allows you to find similar art to any 
    image you choose to upload. We take your beloved images and run them 
    through our pretrained model consisting of 10,000 images from the artsy 
    API. Whether you are in the market for paintings or prints we ensure 
    you are provided with five similar images.
    '''
)       

st.image('assets/MAGIC-2-removebg-preview.png')