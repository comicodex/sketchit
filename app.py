import cv2
import numpy as np
from PIL import Image
import streamlit as st 

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def get_img(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_bitwise = cv2.bitwise_not(img_gray)
    img_blur = cv2.GaussianBlur(img_bitwise, (21, 21), sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_blur)
    return final_img


st.title("Sketchit")
st.write("Turn your images into captivating pencil-sketch masterpieces")

img_file = st.sidebar.file_uploader("Upload image here", type=["jpg", "jpeg", "png", "gif"])

if img_file is None:
    st.write("_Instructions:_ please upload your image on the left-side menu")
else:
    input_img = Image.open(img_file)
    final_sketch = get_img(np.array(input_img))
    st.write("**Uploaded image**")
    st.image(input_img, use_column_width=True)
    st.write("**Pencil Sketch**")
    st.image(final_sketch, use_column_width=True)

st.write("&copy;comicodex2021 - All rights reserved.")


st.sidebar.write("Converting your images into pencil-sketches using Computer Vision")

st.sidebar.image("static\img\sketch.jpeg", width=80, use_column_width=True)

