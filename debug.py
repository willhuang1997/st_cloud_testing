import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.markdown("""
    Here are all the options that we can support for vega embed: \n
        bind?: HTMLElement | string;
        actions?: boolean | Actions;
        mode?: Mode;
        theme?: 'excel' | 'ggplot2' | 'quartz' | 'vox' | 'dark';
        defaultStyle?: boolean | string;
        logLevel?: number;
        loader?: Loader | LoaderOptions;
        renderer?: R;
        tooltip?: TooltipHandler | TooltipOptions | boolean;
        patch?: S | PatchFunc | Operation[];
        width?: number;
        height?: number;
        padding?: number | {left?: number; right?: number; top?: number; bottom?: number};
        scaleFactor?: number;
        config?: S | Config;
        sourceHeader?: string;
        sourceFooter?: string;
        editorUrl?: string;
        hover?: boolean | Hover;
        i18n?: Partial<typeof I18N>;
        downloadFileName?: string;
        formatLocale?: Record<string, unknown>;
        timeFormatLocale?: Record<string, unknown>;
        expressionFunctions?: ExpressionFunction;
        ast?: boolean;
        expr?: typeof expressionInterpreter;
        viewClass?: typeof View;
""")

st.write("""Here are the ones I suggest we support and we can support others later easily if need be:
```
actions?: boolean | Actions;
i18n?: Partial<typeof I18N>; // I18N is the text that shows up in the actions dropdown
formatLocale?: Record<string, unknown>;
timeFormatLocale?: Record<string, unknown>;
```
""")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

with st.expander("Code for disabling actions in chart below"):
    st.code("""
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.altair_chart(c, use_container_width=True, theme='streamlit', actions=False)
    """)
st.altair_chart(c, use_container_width=True, theme='streamlit', actions=False)

#   CLICK_TO_VIEW_ACTIONS: 'Click to view actions',
#   COMPILED_ACTION: 'View Compiled Vega',
#   EDITOR_ACTION: 'Open in Vega Editor',
#   PNG_ACTION: 'Save as PNG',
#   SOURCE_ACTION: 'View Source',
#   SVG_ACTION: 'Save as SVG',

with st.expander("Code for changing the text in actions in chart below"):
    st.code("""
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.altair_chart(c, use_container_width=True, theme='streamlit', i18n={'EDITOR_ACTION' : 'Hello World!', "COMPILED_ACTION": "Hello World!"})
    """)
st.altair_chart(c, theme='streamlit', i18n={'EDITOR_ACTION' : 'Hello World!', "COMPILED_ACTION": "Hello World!"})

with st.expander("Code for changing the locale format and the time format"):
    st.code("""
import altair as alt
import pandas as pd
from urllib import request
import json

# fetch & enable a German format & timeFormat locales.
with request.urlopen('https://raw.githubusercontent.com/d3/d3-format/master/locale/de-DE.json') as f:
  de_format = json.load(f)
with request.urlopen('https://raw.githubusercontent.com/d3/d3-time-format/master/locale/de-DE.json') as f:
  de_time_format = json.load(f)

df = pd.DataFrame({
    'date': pd.date_range('2020-01-01', freq='M', periods=6),
    'revenue': [100000, 110000, 90000, 120000, 85000, 115000]
})

chart1 = alt.Chart(df).mark_bar().encode(
    y='month(date):O',
    x=alt.X('revenue:Q', axis=alt.Axis(format='$,r'))
)
st.altair_chart(chart1,formatLocale=de_format, timeFormatLocale=de_time_format)
    """)

import altair as alt
import pandas as pd
from urllib import request
import json

# fetch & enable a German format & timeFormat locales.
with request.urlopen('https://raw.githubusercontent.com/d3/d3-format/master/locale/de-DE.json') as f:
  de_format = json.load(f)
with request.urlopen('https://raw.githubusercontent.com/d3/d3-time-format/master/locale/de-DE.json') as f:
  de_time_format = json.load(f)

df = pd.DataFrame({
    'date': pd.date_range('2020-01-01', freq='M', periods=6),
    'revenue': [100000, 110000, 90000, 120000, 85000, 115000]
})

chart1 = alt.Chart(df).mark_bar().encode(
    y='month(date):O',
    x=alt.X('revenue:Q', axis=alt.Axis(format='$,r'))
)
st.altair_chart(chart1,formatLocale=de_format, timeFormatLocale=de_time_format)
# st.altair_chart(c, theme='streamlit', scaleFactor=100)
# st.altair_chart(c, theme='streamlit', scaleFactor=100)



