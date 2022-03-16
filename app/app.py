import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import streamlit as st
import pandas as pd
import plotly.express as px
from collections import OrderedDict
from categories.lawton_scale import LawtonScale

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

def get_min_max_value(dictionary):
    return (
        100
        * (dictionary["value"] - dictionary["min_value"])
        / (dictionary["max_value"] - dictionary["min_value"])
    )


categories = OrderedDict(
    [
        ("processing cost", {"type": "integer", "max_value": 10, "min_value": 1}),
        (
            "mechanical properties",
            {"type": "integer", "max_value": 50, "min_value": 20},
        ),
        ("chemical stability", {"type": "integer", "max_value": 5, "min_value": 0}),
        ("thermal stability", {"type": "integer", "max_value": 22, "min_value": 18}),
        ("device integration", {"type": "integer", "max_value": 15, "min_value": 3}),
    ]
)

with col1:
    for cat in categories:
        categories[cat]["value"] = st.slider(
            cat,
            min_value=categories[cat]["min_value"],
            max_value=categories[cat]["max_value"],
            value=None,
            step=1,
        )

    le = LawtonScale()
    le.render()

df = pd.DataFrame(
    {
        "r": [get_min_max_value(categories[cat]) for cat in categories] + [100* (le.value - le.min) / (le.max - le.min)],
        "real_values": [categories[cat]["value"] for cat in categories] + [le.value],
        "theta": list(categories.keys()) + ["lawton"],
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
