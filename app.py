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
st.write("Turn your images into beautiful pencil sketch masterpieces")

img_file = st.sidebar.file_uploader("Upload image", type=["jpg", "jpeg", "png", "gif"])

if img_file is None:
    st.write("Please upload image")
else:
    input_img = Image.open(img_file)
    final_sketch = get_img(np.array(input_img))
    st.write("**Upload image**")
    st.image(input_img, use_column_width=True)
    st.write("**Pencil Sketch**")
    st.image(final_sketch, use_column_width=True)



st.sidebar.subheader("About")
st.sidebar.write("Sketchit converts any image into a pencil sketch drawing using Computer Vision")