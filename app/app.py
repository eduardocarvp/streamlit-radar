import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import streamlit as st
import pandas as pd
import plotly.express as px
from collections import OrderedDict
from categories.lawton_scale import LawtonScale
from categories.edg_15 import EDG
from categories.barthel import Barthel

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    scales = [LawtonScale(), EDG(), Barthel()]
    for scale in scales:
        scale.render()

df = pd.DataFrame(
    {
        "r": [100* (scale.value - scale.min) / (scale.max - scale.min) for scale in scales],
        "real_values": [scale.value for scale in scales],
        "theta": [scale.name for scale in scales],
    }
)

with col2:
    fig = px.line_polar(
        df,
        r="r",
        theta="theta",
        line_close=True,
        template="plotly_dark",
        range_r=[0, 100],
        hover_data=["real_values"],
    )
    fig.update_traces(fill='toself')

    st.plotly_chart(fig)
    st.write(df)
