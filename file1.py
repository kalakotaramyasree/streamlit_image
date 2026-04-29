import streamlit as st
import cv2 
st.title("Machine Learning")

st.write("Hello World")

st.write("Deep Learning")

a =st.number_input("Enter a number")

st.text(a)
img = cv2.imread("image 1.jpeg")

st.image(img)

st.write("Resize image")

Height  = st.slider("select the height",100,500)

Width  = st.slider("select the Width",100,500)

img1 =cv2.resize(img,(Width,Height))

st.image(img1)

