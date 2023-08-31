from fastapi import FastAPI
import cv2
# from imageflip import flip

app = FastAPI()

@app.get("/")
def table_flip():
    return {'hello'}

@app.get("/flip")
def table_flip(height,width):
    return {int(height) * int(width)}

@app.post("/imageflip")
async def flip_trying(file):
# contents = await file.read()
    image = cv2.imread(file)
    return cv2.flip(image)



# async def root():
#     return {"message": "Hello World"}