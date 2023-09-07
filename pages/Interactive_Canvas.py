import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import pandas as pd
import base64
import requests
from utils import load_image_jpg, load_image_data
import time

st.image("assets/Untitled_design-6-removebg-preview-removebg-preview.png")

# comment
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

st.header('  On your marks, get set... paint!')

# Specify canvas parameters in application
drawing_mode = "freedraw"
stroke_width = 3
# if drawing_mode == "point":
#     point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = "#eee"
realtime_update = False

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    height=600,
    drawing_mode=drawing_mode,
    # point_display_radius= point_display_radius if drawing_mode == "point" else 0,
    display_toolbar=st.sidebar.checkbox("Display toolbar", True),
    key="full_app",
)



if canvas_result.image_data is not None:
    drawing = Image.open(canvas_result.image_data)
    # Send the image to FastAPI endpoint for flipping
    fastapi_url = "https://artstyfartsci-5fhi7unvja-ew.a.run.app/top_5_similar"
    files = {"image": drawing}
    response = requests.post(fastapi_url, files=files)
    #st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    progress_text1 = ":rainbow[Going to Art School]"
    progress_text2 = ":rainbow[Unpacking Paint and Brushes]"
    progress_text3 = ":rainbow[Painting Your New Artistic World]"

    my_bar = st.progress(0, text="loading")
    for percent_complete in range(100):
        time.sleep(0.5)
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
            st.image(drawing, caption="Your input.", use_column_width=True)

        df = load_image_data(response_data["top_5"])

        with col2:
            for i in range(5):
                title = df[df['image_index'] == response_data["top_5"][i]].iloc[0,2]
                image = Image.open(images_to_display[i])
                st.image(image, caption=title)

    else:
        st.error("An error occurred while processing the image.")
        st.write(response.status_code)




# # Do something interesting with the image data and paths
# if canvas_result.image_data is not None:
#     st.image(canvas_result.image_data)
# if canvas_result.json_data is not None:
#     objects = pd.json_normalize(canvas_result.json_data["objects"])
#     for col in objects.select_dtypes(include=["object"]).columns:
#         objects[col] = objects[col].astype("str")
#     st.dataframe(objects)
