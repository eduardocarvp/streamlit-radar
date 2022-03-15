import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import streamlit as st
import pandas as pd
import plotly.express as px
from collections import OrderedDict


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

for cat in categories:
    categories[cat]["value"] = st.slider(
        cat,
        min_value=categories[cat]["min_value"],
        max_value=categories[cat]["max_value"],
        value=None,
        step=1,
    )


df = pd.DataFrame(
    {
        "r": [get_min_max_value(categories[cat]) for cat in categories],
        "real_values": [categories[cat]["value"] for cat in categories],
        "theta": categories.keys(),
    }
)

template = st.selectbox("Select graph template", ["plotly_dark", "seaborn"])

fig = px.line_polar(
    df,
    r="r",
    theta="theta",
    line_close=True,
    template=template,
    range_r=[0, 100],
    hover_data=["real_values"],
)


st.plotly_chart(fig)
st.write(df)
