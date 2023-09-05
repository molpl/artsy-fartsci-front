import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import pandas as pd
import base64
import requests


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

st.image("assets/Untitled_design-6-removebg-preview-removebg-preview.png")

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
    image=canvas_result.image_data
    st.image(canvas_result.image_data)



# # Do something interesting with the image data and paths
# if canvas_result.image_data is not None:
#     st.image(canvas_result.image_data)
# if canvas_result.json_data is not None:
#     objects = pd.json_normalize(canvas_result.json_data["objects"])
#     for col in objects.select_dtypes(include=["object"]).columns:
#         objects[col] = objects[col].astype("str")
#     st.dataframe(objects)