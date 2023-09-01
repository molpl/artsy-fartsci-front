from fastapi import FastAPI
from PIL import Image
# use PIL instead of CV2 - check uses

import tempfile
#add tempfile portion. must have an intermediary tempfile in order to serve back image. 

app = FastAPI()

@app.get("/")
def table_flip():
    return {'hello'}

@app.get("/flip")
def table_flip(height,width):
    return {int(height) * int(width)}

@app.post("/imageflip")
async def flip_image(image: UploadFile):

    image_data = await image.read()
    image = image.open(io,BytesIO(image_data)))
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

with tempFile.NamedTemporaryFile(suffix='.png', delete=False,) as temp_file:
    flipped_img.save(temp_file, format='PNG')




# async def root():
#     return {"message": "Hello World"}