
import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64



# Set the page title and icon

# st.image('assets/MAGIC-2-removebg-preview.png')

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

st.subheader('Why choose us?')

st.text( '''
        If you are already a part of the artsy community or are looking
        for some brilliant artworks, we can provide you with a fresh new 
        set of images to complete your dreams of a home gallery or just a 
        beautiful painting to hang in your corridor. With artsy-fartsci you 
        can unlock your 'arts desire.
        '''
)

st.subheader('How does our model work?')

st.text( '''
    Our model uses the most efficient machine learning technologies to
    procure your five similar images. With 10000 images scraped from the
    artsy API, equal parts prints, paintings, and drawings, we have trained our 
    model using an autoencoder to identify multiple features that make 
    up your image, and then produce five more. The process your image goes through 
    once uploaded is that it is sent to our API which pre-processes 
    and encodes your image to extrapolate the images features in a latent
    space, and then computes the five nearest images based on these 
    similar features. We then lay out these images for you below your input 
    to allow you to see how similar the images are as well as giving you
    information on the new similar images.
      ''')

st.image('assets/Screenshot_2023-09-06_at_10.54.26-removebg-preview.png', caption='Input Journey', width=700)