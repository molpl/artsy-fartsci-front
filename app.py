import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

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
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    # Check if an image was uploaded
    if uploaded_image is not None:
        # Display the user-uploaded image with a frame
        user_image = Image.open(uploaded_image)
        framed_user_image = add_frame(user_image)
        st.image(framed_user_image, caption="Where we started our journey", use_column_width=True)

    # Display 5 images from an API
    st.header("Here are five similar art pieces to explore")
    api_url = "http://127.0.0.1:8000"  # WHAT IS THE FASTAPI ENDPOINT
    response = requests.get(api_url)

# THIS RETURNS 5 IMAGES BUT I STILL KNOW FUCK ALL ABOUT API...  (UNCOMMENT IT)
    if response.status_code == 200:
        pass
        # api_images = response.json()
        # for i in api_imagereply:
            # api_image = Image.open(BytesIO(requests.get(api_image_url).content))\
            # st.image(api_image, caption=f'{image_title}', use_column_width=True)
            # st.text(
                
            #     # enter the text from the API????
                
            # )
        
    else:
        st.warning("Oops! Try again later.")

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
