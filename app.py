import requests
import streamlit as st
import numpy as np



# url=''

user_input = st.file_uploader(
    "Select a piece of artwork that you enjoy (png or jpg only)"
    , type=['png','jpg','jpeg']
    ,accept_multiple_files=False
    )

if user_input is not None:
    query_h=st.text_input('height')
    
if user_input is not None:
    query_w=st.text_input('width')

response=requests.get(f'http://127.0.0.1:8000/flip?height={query_h}&width={query_w}')
st.write(response.json())   


response2 = requests.post(user_input)
st.write(response2)