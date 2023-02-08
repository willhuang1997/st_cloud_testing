import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

df = px.data.gapminder()

fig_plotly = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)


df = pd.DataFrame()
with st.expander("Test"):
    st.dataframe(df, use_container_width=True)
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
    st.plotly_chart(fig_plotly, theme="streamlit", use_container_width=True)
    arr = np.random.normal(1, 1, size=100)
    fig_matplotlib, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.pyplot(fig_matplotlib)

st.plotly_chart(fig_plotly, theme="streamlit", use_container_width=True)

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    st.plotly_chart(fig_plotly, theme="streamlit", use_container_width=True)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
slider_val = st.slider("Form slider2")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
)

with st.sidebar.form(key="form1"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

# Using "with" notation
with st.sidebar.expander("Test"):
    st.dataframe(df, use_container_width=True)

