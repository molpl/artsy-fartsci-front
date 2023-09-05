import streamlit as st
import os
import random
from PIL import Image
import base64

# Define the folder paths
base_folder = "/Users/kamran1998/code/CheekyMonkeyCoder/artsy-fartsci-front/"  # Replace with your folder path
categories = ["modern_art", "impressionist", "renaissance"]

# Create a Streamlit app
st.title("Pick a category and check out these cool pieces ! 👩🏽‍🎨 ")

st.text('There are thousands of amazing pieces you can find but here are just a few!')

# Add a dropdown to select the art category
selected_category = st.selectbox("SELECT ART CATEGORY", categories)

# Get the list of image files in the selected category folder
category_folder = os.path.join(base_folder, selected_category)
image_files = os.listdir(category_folder)

# Randomly select two images from the folder
random.shuffle(image_files)
selected_images = image_files[:2]
print(selected_images)

# Display the selected images
for image_file in selected_images:
    image_path = os.path.join(category_folder, image_file)
    print(image_path)
    st.image(Image.open(image_path), caption=image_file, use_column_width=True)


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


st.image("assets/Untitled_design-6-removebg-preview-removebg-preview.png")
