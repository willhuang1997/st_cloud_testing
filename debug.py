import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe("https://docs.streamlit.io/en/latest")
st.write("---")
components.iframe("https://streamlit-demo-self-driving-streamlit-app-8jya0g.streamlit.app/?embed=true")
st.write("---")
components.iframe("https://resolve-labs-feed-back-feedback-input-lv24tg.streamlit.app/?embed=true", height = 1000)
