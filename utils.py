import os
import numpy as np
import pandas as pd
from google.cloud import bigquery
from google.cloud import storage
from google.oauth2 import service_account
import streamlit as st
import json

# function to get image data from index
def load_image_data(image_index):
    credentials = service_account.Credentials.from_service_account_info(json.loads(st.secrets["credentials"]))

    # get table name
    full_table_name = f'{st.secrets["gcp_project"]}.{st.secrets["bq_dataset"]}.image_data_balanced_new_index'
    index_string = ','.join([str(i) for i in image_index])
    #index_string = '1,2,3'
    # write query
    query = f'''
            SELECT
                image_index,
                artwork_id,
                title,
                category
            FROM {full_table_name}
            WHERE image_index IN({index_string})
            '''
    # instantiate client
    client = bigquery.Client(project=st.secrets["gcp_project"],credentials=credentials)
    # set up query job
    query_job = client.query(query)
    # run query
    df = query_job.result().to_dataframe()
    return df


if __name__ == '__main__':
    print(load_image_data([2,3]))



# function to get images from index
def load_image_jpg(image_index):

    credentials = service_account.Credentials.from_service_account_info(json.loads(st.secrets["credentials"]))

    client = storage.Client(project=st.secrets["gcp_project"], credentials=credentials)

    #client = storage.Client.from_service_account_json(json_credentials_path=st.secrets["credentials"])
    bucket = client.get_bucket(st.secrets["bucket_name"])
    blobs = list(client.get_bucket(st.secrets["bucket_name"]).list_blobs(prefix="balanced"))
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
