from fastapi import APIRouter, UploadFile, HTTPException
from PIL import Image
from io import BytesIO
import numpy as np

emo_router = APIRouter() #for routing info. from here to main.py

@emo_router.post("/detect")
def detect (im: UploadFile): #it is for uploading file

    if im. filename. split(". ")[-1] in ("jpg", "jpeg", "png"):
        pass 
    else: 
        raise HTTPException (
        status_code=415,detail="Not an image") #raise exception if file not in proper format

    image=Image.open(BytesIO(im.file.read())) #for reading the image
    image=np.array(image)

    return emotion_detector(image)