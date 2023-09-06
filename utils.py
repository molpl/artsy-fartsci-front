import os
import numpy as np
import pandas as pd
#from google.cloud import bigquery
from google.cloud import storage
import streamlit as st

# function to get image data from index
def load_image_data(image_index):
    pass

# function to get images from index
def load_image_jpg(image_index):
    client = storage.Client()
    bucket = client.get_bucket(st.secrets["BUCKET_NAME"])
    blobs = list(client.get_bucket(st.secrets["BUCKET_NAME"]).list_blobs(prefix="balanced"))
    blob_name = False
    for blob in blobs:
        if int(blob.name.replace('balanced/','').split('_')[0]) == image_index:
            blob_name = blob.name
    if blob_name:
        blob = bucket.get_blob(blob_name)
        blob.download_to_filename(f'{image_index}.jpg')
        return f'{image_index}.jpg'
    else:
        return 'image not found'