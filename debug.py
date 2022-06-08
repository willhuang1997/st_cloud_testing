from cgitb import text
import streamlit as st
import matplotlib.pyplot as plt, mpld3
import numpy as np
import pandas as pd
import streamlit.components.v1 as components
import json

#SIMPLE FIG
simple_fig = plt.figure(figsize=(3.5,3.5))
plt.plot([1, 2, 3, 4], marker="X")

#FORMAT STRING FIG
format_string_fig = plt.figure(figsize=(3.5,3.5))
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

#DOLLAR TICKS
# Fixing random state for reproducibility
np.random.seed(19680801)

dollar_ticks_fig, ax = plt.subplots()
dollar_ticks_fig.set_size_inches((3.5,3.5))
plt.plot(100*np.random.rand(20), marker='o')

# Use automatic StrMethodFormatter
ax.yaxis.set_major_formatter('${x:1.2f}')

ax.yaxis.set_tick_params(which='major', labelcolor='green',
                         labelleft=False, labelright=True)

#PIE CHART
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

pie_chart_fig, ax1 = plt.subplots()
pie_chart_fig.set_size_inches((3.5,3.5))
# pie_chart_fig.
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# pie_chart_fig.set_size_inches(3.5)

#TWO SUBPLOT
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

two_subplot_fig = plt.figure(figsize=(3.5,3.5))
plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker='o')
plt.plot(t2, f(t2), color='black', marker='8')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--', marker='.')
plt.show()

#TEXT BOXES FIG
np.random.seed(19680801)

text_boxes_fig, ax = plt.subplots()
text_boxes_fig.set_size_inches((3.5,3.5))
x = 30*np.random.randn(10000)
mu = x.mean()
median = np.median(x)
sigma = x.std()
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (sigma, )))

ax.hist(x, 50)
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)


#DATE FORMATS
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
# Load a numpy structured array from yahoo csv data with fields date, open,
# close, volume, adj_close from the mpl-data/example directory.  This array
# stores the date as an np.datetime64 with a day unit ('D') in the 'date'
# column.
data = cbook.get_sample_data('goog.npz', np_load=True)['price_data']

date_format_fig, axs = plt.subplots(3, 1, figsize=(6.4, 7), constrained_layout=True)
date_format_fig.set_size_inches((5,5))
# common to all three:
for ax in axs:
    ax.plot('date', 'adj_close', data=data, marker='.')
    # Major ticks every half year, minor ticks every month,
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.grid(True)
    ax.set_ylabel(r'Price [\$]')

# different formats:
ax = axs[0]
ax.set_title('DefaultFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')

ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(
    mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02,
             fontsize='medium')
# Text in the x axis will be displayed in 'YYYY-mm' format.
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
# Rotates and right-aligns the x labels so they don't crowd each other.
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')

#PLACING COLOR BARS

# Fixing random state for reproducibility
np.random.seed(19680801)

color_bars_fig, axs = plt.subplots(2, 2)
color_bars_fig.set_size_inches((3.5,3.5))
cmaps = ['RdBu_r', 'viridis']
for col in range(2):
    for row in range(2):
        ax = axs[row, col]
        pcm = ax.pcolormesh(np.random.random((20, 20)) * (col + 1),
                            cmap=cmaps[col])
        color_bars_fig.colorbar(pcm, ax=ax)

from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.cm as cm

# Fixing random state for reproducibility
np.random.seed(19680801)
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

image_demo_fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
               origin='lower', extent=[-3, 3, -3, 3],
               vmax=abs(Z).max(), vmin=-abs(Z).max())


#3d fig
from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
import numpy as np

dem = cbook.get_sample_data('jacksboro_fault_dem.npz', np_load=True)
z = dem['elevation']
nrows, ncols = z.shape
x = np.linspace(dem['xmin'], dem['xmax'], ncols)
y = np.linspace(dem['ymin'], dem['ymax'], nrows)
x, y = np.meshgrid(x, y)

region = np.s_[5:50, 5:50]
x, y, z = x[region], y[region], z[region]

threed_fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
threed_fig.set_size_inches((2,2))

ls = LightSource(270, 45)
# To use a custom hillshading mode, override the built-in shading and pass
# in the rgb colors of the shaded surface calculated from "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

col1, col2 = st.columns(2)

with col1:
    st.header('This is not interactive!')
    st.pyplot(simple_fig, interactive=False)
    st.pyplot(format_string_fig, interactive=False)
    st.pyplot(dollar_ticks_fig, interactive=False)
    st.pyplot(pie_chart_fig, interactive=False)
    st.pyplot(two_subplot_fig, interactive=False)
    st.pyplot(text_boxes_fig, interactive=False)
    st.pyplot(date_format_fig, interactive=False)
    st.pyplot(color_bars_fig, interactive=False)
    st.pyplot(image_demo_fig, interactive=False)
    st.pyplot(threed_fig, interactive=False)

with col2:
    st.header('This is interactive!')
    st.pyplot(simple_fig, interactive=True)
    st.pyplot(format_string_fig, interactive=True)
    st.pyplot(dollar_ticks_fig, interactive=True)
    st.pyplot(pie_chart_fig, interactive=False)
    st.pyplot(two_subplot_fig, interactive=True)
    st.pyplot(text_boxes_fig, interactive=True)
    st.pyplot(date_format_fig, interactive=True)
    st.pyplot(color_bars_fig, interactive=True)
    st.pyplot(image_demo_fig, interactive=True)
    st.pyplot(threed_fig, interactive=True)


