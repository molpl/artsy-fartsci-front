# fastapi_app.py
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io

app = FastAPI()

@app.post("/flip_image/")
async def flip_image(image: UploadFile):
    image_data = await image.read()
    img = Image.open(io.BytesIO(image_data))
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

    # Instead of returning a file, return a JSON response with a string message
    response_data = {"message": "Image flipped successfully!"}
    return JSONResponse(content=response_data)