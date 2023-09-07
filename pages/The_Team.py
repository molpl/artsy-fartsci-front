
import streamlit as st
import base64

st.image("assets/Untitled_design-6-removebg-preview-removebg-preview.png")

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
st.header('Meet the Artsy-Fartsci Team')

st.image('assets/Alex-circle.png')
st.text('Alex Sweetman')
st.markdown('http://github.com/Sweetmanco')

st.image('assets/Molly-circle.png')
st.text('Molly Lister')
st.markdown('https://github.com/molpl')

st.image('assets/Kamran-circle.png')
st.text('Kamran Ardabili')
st.markdown('https://github.com/CheekyMonkeyCoder')

st.image('assets/Eve-circle.png')
st.text('Eve Jacob')
st.markdown('https://github.com/Evej2000')
