import streamlit as st
import time

start_time = time.time()

#@st.experimental_memo
def method1():
    y = 0
    for x in range(1,1000000):
        y += x
    return y 

menu_items = {'Get Help': "https://www.streamlit.io", "Report a bug": "https://www.google.com/help", "About" : "Hello. This App was built by William Huang. As a software Engineer, I have been working for a few years as a software engineer at different companies. One of the companies that I have worked at is Cisco. Another company that I have worked at is LogMeIn. These companies are different in size and in culture. Currently, I work at Streamlit and Streamlit is the best! Here, I am doing some testing for this Streamlit feature called Hamburger Menu. I hope it is working with the scrollability. *PLEASE* Hello. This App was built by William Huang. As a software Engineer, I have been working for a few years as a software engineer at different companies. One of the companies that I have worked at is Cisco. Another company that I have worked at is LogMeIn. These companies are different in size and in culture. Currently, I work at Streamlit and Streamlit is the best! Here, I am doing some testing for this Streamlit feature called Hamburger Menu. I hope it is working with the scrollability. PLEASE Hello. This App was built by William Huang. As a software Engineer, I have been working for a few years as a software engineer at different companies. One of the companies that I have worked at is Cisco. Another company that I have worked at is LogMeIn. These companies are different in size and in culture. Currently, I work at Streamlit and Streamlit is the best! Here, I am doing some testing for this Streamlit feature called Hamburger Menu. I hope it is working with the scrollability. PLEASE Hello. This App was built by William Huang. As a software Engineer, I have been working for a few years as a software engineer at different companies. One of the companies that I have worked at is Cisco. Another company that I have worked at is LogMeIn. These companies are different in size and in culture. Currently, I work at Streamlit and Streamlit is the best! Here, I am doing some testing for this Streamlit feature called Hamburger Menu. I hope it is working with the scrollability. PLEASE Hello. This App was built by William Huang. As a software Engineer, I have been working for a few years as a software engineer at different companies. One of the companies that I have worked at is Cisco. Another company that I have worked at is LogMeIn. These companies are different in size and in culture. Currently, I work at Streamlit and Streamlit is the best! Here, I am doing some testing for this Streamlit feature called Hamburger Menu. I hope it is working with the scrollability. PLEASE"}
st.set_page_config(menu_items=menu_items)
st.markdown(" # HELLO WORLD")

# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = method1()

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = method1()

# Reads
st.write(st.session_state.key)

# Outputs: value

st.session_state.key = method1()    # Attribute API
st.session_state['key'] = method1()  # Dictionary like API

st.write(st.session_state)
diff_time = time.time() - start_time
st.write(f"--- {diff_time} seconds ---")
