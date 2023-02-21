import time

import altair as alt
import graphviz
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import pydeck as pdk
import streamlit as st
from bokeh.plotting import figure

st.title("MEGA APP")
st.write("This app exists to test out all the st commands we possibly can in one go.")

st.write("# input tests")
text_input = st.text_input("textbox")
st.write(f"Your text input is {text_input}!")
number_input = st.number_input("number")
st.write(f"Your number input is {number_input}!")

slider_input = st.slider("slider")
st.write(f"Your slider input is {slider_input}!")
button_input = st.button("button")
if button_input:
    st.write("You pressed the button!")
checkbox_input = st.checkbox("checkbox")
st.write(f"Your checkbox input is {checkbox_input}!")
radio_input = st.radio("radio", ["cat", "dog"])
st.write(f"Your radio input is {radio_input}!")
selectbox_input = st.selectbox("selectbox", ["cat", "dog"])
st.write(f"Your selectbox input is {selectbox_input}!")
multiselectbox_input = st.multiselect("multiselect", ["cat", "dog"])
st.write(f"Your multiselectbox input is {multiselectbox_input}!")
select_slider_input = st.select_slider("select slider", ["cat", "dog"])
st.write(f"Your select_slider input is {select_slider_input}!")
text_area_input = st.text_area("text area")
st.write(f"Your text_area input is {text_area_input}!")
date_input = st.date_input("date input")
st.write(f"Your date input is {date_input}!")
time_input = st.time_input("time input")
st.write(f"Your time input is {time_input}!")
file_input = st.file_uploader("file input")
st.write(f"Your file input is {file_input}!")
color_input = st.color_picker("color picker")
st.write(f"Your color input hex {color_input}!")
text_contents = """This is some text"""
st.download_button("Download some text", text_contents)
st.write("Below is the camera input, give camera access to the app to test it out!")
cam_input = st.camera_input("cam input")
st.write(f"Your cam input is {cam_input}!")

st.write("# text elements")
st.write("This next section tests out all the text elements in Streamlit")
st.markdown("hello markdown")
st.header("hello header")
st.subheader("hello subheader")
st.caption("hello caption")
st.code("a = 1234")
st.text("hello text")
st.latex("\int a x^2 \,dx")
"""
hello magic
"""

st.write("# data display elements")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.write("st.dataframe test")
st.dataframe(chart_data)
st.write("st.table test")
st.table(chart_data)
st.metric("Metric", 42, 2)
st.write("st.json test")
st.json(chart_data.head().to_dict())


st.write("# chart elements")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.write("testing built in charts")
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write("testing altair chart")
st.altair_chart(c, use_container_width=True, theme="streamlit")

st.write("testing vega lite chart")
st.vega_lite_chart(
    chart_data,
    {
        "mark": {"type": "circle", "tooltip": True},
        "encoding": {
            "x": {"field": "a", "type": "quantitative"},
            "y": {"field": "b", "type": "quantitative"},
            "size": {"field": "c", "type": "quantitative"},
            "color": {"field": "c", "type": "quantitative"},
        },
    },
)


# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ["Group 1", "Group 2", "Group 3"]

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])

# Plot!
st.write("testing plotly chart")
st.plotly_chart(fig, use_container_width=True)


x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="simple line example", x_axis_label="x", y_axis_label="y")

p.line(x, y, legend_label="Trend", line_width=2)
st.write("testing bokeh chart")
st.bokeh_chart(p, use_container_width=True)


df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.write("testing pydeck chart")
st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=df,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge("run", "intr")
graph.edge("intr", "runbl")
graph.edge("runbl", "run")
graph.edge("run", "kernel")
graph.edge("kernel", "zombie")
graph.edge("kernel", "sleep")
graph.edge("kernel", "runmem")
graph.edge("sleep", "swap")
graph.edge("swap", "runswap")
graph.edge("runswap", "new")
graph.edge("runswap", "runmem")
graph.edge("new", "runmem")
graph.edge("sleep", "runmem")

st.write("testing graphviz chart")
st.graphviz_chart(graph)

### MAP
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.write("testing map")
st.map(df)


st.write("# Media elements")
image_nums = np.random.randint(255, size=(144, 144), dtype=np.uint8)

st.write("st.image test (static image should appear)")
st.image(image_nums)
audio_video_data = np.random.uniform(-1, 1, 44100)
st.write("st.audio test (empty audio should appear)")
st.audio(audio_video_data)
st.write("st.video test (empty video should appear)")
st.video(audio_video_data)

st.write("# layouts and containers")

st.sidebar.write("sidebar test")

a, b = st.columns(2)
with b:
    st.write("col check, should be second column")

with a:
    st.write("col check, should be first column")

tab_a, tab_b = st.tabs(["tab a", "tab b"])
tab_b.write("tab b test")
tab_a.write("tab a test")

with st.expander("open to see expander"):
    st.write("works!")

c = st.container()
c.write("this writes to a container!")
a = st.empty()
a.write("this writes to a previously empty block!")

st.write("# display progress and status")

st.write("progress bar test")
my_bar = st.progress(0)
for percent_complete in range(100):
    my_bar.progress(percent_complete + 1)

spinner_test = st.button("start spinner")
if spinner_test:
    with st.spinner("Wait!"):
        time.sleep(3)
        st.write("spinner works if you saw it!")

st.error("st error")
st.warning("st warning")
st.info("st info")
st.success("st success")
st.exception(RuntimeError("example of error"))

test = st.button("Play balloons and snow")
if test:
    st.balloons()
    st.snow()

with st.form(key="tester"):
    st.write("This form just prints out the text input!")
    text_tester = st.text_input("Text To Print")
    st.form_submit_button("Submit")
st.write(text_tester)

clicked = st.button("Click me to rerun")
if clicked:
    st.experimental_rerun()


st.write("# Utilities")

with st.echo():
    st.write("st echo check")

st.write("st help check")
st.help(st.write)

st.write("experimental show check with the audio video data used earlier")
st.experimental_show(audio_video_data)

set_query_params = st.checkbox("Set tester value in query params?")
st.experimental_set_query_params(tester=set_query_params)

get_query_params = st.button("Get query params")
if get_query_params:
    st.write(st.experimental_get_query_params())

st.write("# State Management")

st.write(
    """Adds key = True to session state, then prints session state.
    The metrics app adds other work to session state as well"""
)
if "key" not in st.session_state:
    st.session_state["key"] = True
st.write(st.session_state)

st.stop()
st.write("if you see this, st.stop does not work")
