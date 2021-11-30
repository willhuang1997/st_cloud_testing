import streamlit as st

#st.set_page_config(layout="wide")

st.write("Hello World")
st.text_input('Hello World')
screenshot = st.camera_input('Hello World', 'Testing1')

if screenshot:
    st.image(screenshot)

