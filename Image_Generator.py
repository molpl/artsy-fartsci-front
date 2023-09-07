import streamlit as st
import requests
from PIL import Image
import io
import base64
import time
from google.cloud import storage
from utils import load_image_jpg, load_image_data

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

    #st.write(st.secrets['bucket_name'])

    # Upload a user image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        # Send the image to FastAPI endpoint for flipping
        fastapi_url = "https://artstyfartsci-5fhi7unvja-ew.a.run.app/top_5_similar"
        files = {"image": uploaded_file}
        response = requests.post(fastapi_url, files=files)
        #st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        progress_text1 = ":grey[Going to Art School]:artist:"
        progress_text2 = ":grey[Unpacking Paint and Brushes]:lower_left_paintbrush::art:"
        progress_text3 = ":grey[Painting Your New Artistic World]:frame_with_picture:"

        my_bar = st.progress(0, text="loading")
        for percent_complete in range(100):
            time.sleep(1.2)
            if percent_complete <= 30:
                my_bar.progress(percent_complete + 1, text=progress_text1)

            if percent_complete <= 65 and percent_complete > 30:
                my_bar.progress(percent_complete + 1, text=progress_text2)

            if percent_complete <= 100 and percent_complete > 65:
                my_bar.progress(percent_complete + 1, text=progress_text3)

        my_bar.empty()
        #response_data = response.json()
        #st.write(response.status_code)
        if response.status_code == 200:
            response_data = response.json()

            images_to_display = []
            for i in response_data['top_5']:
                images_to_display.append(load_image_jpg(i))

            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded_file, caption="Your input.", use_column_width=True)

            df = load_image_data(response_data["top_5"])

            with col2:
                for i in range(5):
                    title = df[df['image_index'] == response_data["top_5"][i]].iloc[0,2]
                    image = Image.open(images_to_display[i])
                    st.image(image, caption=title)

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
