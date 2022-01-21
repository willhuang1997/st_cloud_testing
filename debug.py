"""
# NYC Uber Ridesharing Data
Examining how Uber pickups vary over time in New York City's and at its major regional
airports.  By sliding the slider on the left you can view different slices of time and
explore different transportation trends.
"""

import altair as alt
import pandas as pd
import pydeck as pdk
import streamlit as st

# Set the page config to widemoe.
st.set_page_config(layout="wide")
st.expander = st.expander
URL = "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"


@st.cache(persist=True)
def load_data(nrows):
    """Load `nrows` rows of Uber ride pickup data."""
    data: pd.DataFrame = pd.read_csv(URL, nrows=nrows)  # type: ignore
    date_time = pd.to_datetime(data["Date/Time"])  # type: ignore
    data["hour"] = date_time.dt.hour
    data["minute"] = date_time.dt.minute
    return data


def map(data, lat, lon, zoom) -> pdk.Deck:
    """Returns a nice looking PyDeck map focused on one part of the data."""
    MAP_STYLE = "mapbox://styles/mapbox/light-v9"
    view_state = dict(latitude=lat, longitude=lon, zoom=zoom, pitch=40)
    data_config = dict(data=data, get_position=["Lon", "Lat"])
    hex_config = dict(radius=75, elevation_scale=5, elevation_range=[0, 1000])
    mouse_config = dict(pickable=False, extruded=True)
    layer = pdk.Layer("HexagonLayer", **data_config, **hex_config, **mouse_config)
    return pdk.Deck(map_style=MAP_STYLE, initial_view_state=view_state, layers=[layer])


maps = {
    "New York City": (40.7359, -73.9780, 12),
    "La Guardia Airport": (40.7900, -73.8700, 12),
    "JFK Airport": (40.6650, -73.7821, 12),
    "Newark Airport": (40.7090, -74.1805, 12),
}

# Layout the top section of the app
col1, col2 = st.columns(2)
col1.write(__doc__)
col2.subheader("")
hour_selected = col2.slider("Select hour of pickup", 0, 23)
# minute_selected = col2.slider("Select minute of pickup", 0, 59)
# names = ["New York City"] + [col2.selectbox("Location", list(maps)[1:])]
names = ["New York City"] + col2.multiselect("Location", list(maps)[1:])
st.write("---")

# Display the maps
data = load_data(50000)
data = data[data.hour == hour_selected]
# data = data[data.minute == minute_selected]
for name, col in zip(names, st.columns(len(names))):
    lat, lon, zoom = maps[name]
    with col:
        st.write(f"**{name}**", map(data, lat, lon, zoom))

# Display the histogram
# CHANGETO: st.expander("Show histogram").altair_chart(
st.altair_chart(
    alt.Chart(data)
    .mark_area(interpolate="step-after", line=True)
    .encode(
        x=alt.X("minute:Q", title="Minute", scale=alt.Scale(nice=False)),
        y=alt.Y("count()", title="Rides"),
        tooltip=["minute", "count():Q"],
    )
    .configure_mark(opacity=1, color="lightcoral"),
    use_container_width=True,
)
