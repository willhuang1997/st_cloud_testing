import streamlit as st
import plotly.figure_factory as ff
import numpy as np

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

import plotly.express as px
df = px.data.iris()
fig2 = px.scatter(df, title="TITLE", x="sepal_width", y="sepal_length", color='petal_length')

st.plotly_chart(fig2, use_container_width=True)

# df = px.data.tips()
# fig3 = px.scatter(df, x="total_bill", y="tip", color="size",
#                  title="Numeric 'size' values mean continuous color")

# st.plotly_chart(fig3, use_container_width=True)
df = px.data.gapminder().query("continent=='Oceania'")
fig4 = px.line(df, x="year", y="lifeExp", color='country')

st.plotly_chart(fig4, use_container_width=True)


fruits = ["apples", "oranges", "bananas"]
fig11 = px.line(x=fruits, y=[1,3,2], color=px.Constant("This year"),
             labels=dict(x="Fruit", y="Amount", color="Time Period"))
fig11.add_bar(x=fruits, y=[2,1,3], name="Last year")
st.plotly_chart(fig11, use_container_width=True)

# z = [[.1, .3, .5, .7, .9],
#      [1, .8, .6, .4, .2],
#      [.2, 0, .5, .7, .9],
#      [.9, .8, .4, .2, 0],
#      [.3, .4, .5, .7, 1]]

# fig6 = px.imshow(z, text_auto=True)
# st.plotly_chart(fig6, use_container_width=True)

df = px.data.gapminder().query("country == 'Canada'")
fig7 = px.bar(df, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp', template="seaborn",
             labels={'pop':'population of Canada'}, height=400)

st.plotly_chart(fig7, use_container_width=True)   


fig8 = px.imshow([[1, 20, 30],
                 [20, 1, 60],
                 [30, 60, 1]])
st.plotly_chart(fig8, use_container_width=True)

import plotly.express as px
df = px.data.tips()
fig9 = px.scatter(df, x="total_bill", y="tip", color="smoker",
                 title="String 'smoker' values mean discrete colors")

st.plotly_chart(fig9, use_container_width=True)

import plotly.graph_objects as go

# Create random data with numpy
import numpy as np
np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# Create traces
fig12 = go.Figure()
fig12.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines',
                    name='lines'))
fig12.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers'))
fig12.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='markers', name='markers'))

st.plotly_chart(fig12, use_container_width=True)

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 2, 3, 1])

fig13 = go.Figure()
fig13.add_trace(go.Scatter(x=x, y=y, name="linear",
                    line_shape='linear'))
fig13.add_trace(go.Scatter(x=x, y=y + 5, name="spline",
                    text=["tweak line smoothness<br>with 'smoothing' in line object"],
                    hoverinfo='text+name',
                    line_shape='spline'))
fig13.add_trace(go.Scatter(x=x, y=y + 10, name="vhv",
                    line_shape='vhv'))
fig13.add_trace(go.Scatter(x=x, y=y + 15, name="hvh",
                    line_shape='hvh'))
fig13.add_trace(go.Scatter(x=x, y=y + 20, name="vh",
                    line_shape='vh'))
fig13.add_trace(go.Scatter(x=x, y=y + 25, name="hv",
                    line_shape='hv'))

fig13.update_traces(hoverinfo='text+name', mode='lines+markers')
fig13.update_layout(legend=dict(traceorder='reversed', font_size=16))
st.plotly_chart(fig13, use_container_width=True)

import plotly.express as px
# This dataframe has 244 lines, but 4 distinct values for `day`
df = px.data.tips()
fig14 = px.pie(df, values='tip', names='day')
st.plotly_chart(fig14, use_container_width=True)

df = px.data.gapminder()

fig15 = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
	         size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
st.plotly_chart(fig15, use_container_width=True)

df = px.data.iris()
df["e"] = df["sepal_width"]/100
fig16 = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 error_x="e", error_y="e")
st.plotly_chart(fig16, use_container_width=True)

import pandas as pd
data = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(dict(
    linear=data,
    inclusive=data,
    exclusive=data
)).melt(var_name="quartilemethod")


fig17 = px.box(df, y="value", facet_col="quartilemethod", color="quartilemethod",
             boxmode="overlay", points='all')

fig17.update_traces(quartilemethod="linear", jitter=0, col=1)
fig17.update_traces(quartilemethod="inclusive", jitter=0, col=2)
fig17.update_traces(quartilemethod="exclusive", jitter=0, col=3)
st.plotly_chart(fig17, use_container_width=True)

x0 = np.random.randn(2000)
x1 = np.random.randn(2000) + 1

fig18 = go.Figure()
fig18.add_trace(go.Histogram(x=x0))
fig18.add_trace(go.Histogram(x=x1))

# The two histograms are drawn on top of another
fig18.update_layout(barmode='stack')

st.plotly_chart(fig18, use_container_width=True)

df = px.data.tips()
fig19 = px.histogram(df, x="total_bill", y="tip", color="sex",
                   marginal="box", # or violin, rug
                   hover_data=df.columns)
st.plotly_chart(fig19, use_container_width=True)

df = px.data.tips()

fig20 = px.density_heatmap(df, x="total_bill", y="tip")
st.plotly_chart(fig20, use_container_width=True)

st.title("NOTE: THIS STILL NEEDS MORE EXAMPLES! PLEASE BE AWARE.")
st.title("IN ADDITION, I AM STILL LOOKING INTO TOOLTIPS BUT IT LOOKS LIKE WE CANNOT MAKE MANY CHANGES: https://plotly.com/javascript/reference/layout/#layout-hoverlabel")
