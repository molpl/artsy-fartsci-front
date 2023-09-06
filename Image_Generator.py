# import streamlit as st
# import requests
# from PIL import Image
# import io
# import base64

# # Set the page title and icon
# st.set_page_config(
#     page_title="Artsy-FartSci: A Data Science Project",
# )

# # Define a function to add a frame to an image
# def add_frame(image):
#     # Add a frame around the image
#     frame_color = (70, 33, 252)  # Yellow
#     frame_width = 10
#     framed_image = Image.new("RGB", (image.width + 2 * frame_width, image.height + 2 * frame_width), frame_color)
#     framed_image.paste(image, (frame_width, frame_width))
#     return framed_image

# # Streamlit app
# def main():
#     # # Set the title and header
#     # st.title("Artsy-FartSci: A Data Science Project")
#     st.header("Upload your image here")

#     # Upload a user image
#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

#     if uploaded_file:
#         st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

#     # Send the image to FastAPI endpoint for flipping
#         fastapi_url = "http://localhost:8086/flip_image/"
#         files = {"image": uploaded_file}
#         response = requests.post(fastapi_url, files=files)

#         if response.status_code == 200:
#             response_data = response.json()
#             st.success(response_data["message"])
#         else:
#             st.error("An error occurred while processing the image.")
            
   

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )

# add_bg_from_local('assets/img1.wallspic.com-sky-water-blue-azure-watercolorpainting-4000x6000.jpg')


# st.image("assets/Untitled_design-6-removebg-preview-removebg-preview.png")


# # Run the Streamlit app
# if __name__ == "__main__":
#     main()

import streamlit as st
import requests
from PIL import Image
import io
import base64
from google.cloud import storage
from utils import load_image_jpg

# Set the page title and icon
st.set_page_config(
    page_title="Artsy-FartSci: A Data Science Project",
)

# Define a function to add a frame to an image
def add_frame(image):
    # Add a frame around the image
    frame_color = (70, 33, 252)  # Yellow
    frame_width = 10
    framed_image = Image.new("RGB", (image.width + 2 * frame_width, image.height + 2 * frame_width), frame_color)
    framed_image.paste(image, (frame_width, frame_width))
    return framed_image

# Streamlit app
def main():
    # # Set the title and header
    # st.title("Artsy-FartSci: A Data Science Project")
    st.header("Upload your image here")

    # Upload a user image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

    # Send the image to FastAPI endpoint for flipping
        fastapi_url = "http://localhost:8000/top_5_similar"
        files = {"image": uploaded_file}
        response = requests.post(fastapi_url, files=files)

        if response.status_code == 200:
            response_data = response.json()
            st.success(response_data["top_5"])
            images_to_display = []
            for i in response_data['top_5']:
                images_to_display.append(load_image_jpg(i))
            image = Image.open(images_to_display[0])
            st.image(image, caption='first image')

        else:
            st.error("An error occurred while processing the image.")



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


# Run the Streamlit app
if __name__ == "__main__":
    main()