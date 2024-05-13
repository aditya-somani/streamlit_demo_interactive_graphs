import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
# import scipy as sp -> see last

st.header("Altair Scatter Plot")
chart_data=pd.DataFrame(np.random.randn(100,5),columns=['a','b','c','d','e'])
chart=alt.Chart(chart_data).mark_circle().encode(x="a",y="b",size="c",tooltip=["a","b","c","d","e"])
st.altair_chart(chart)

st.header("Interactive Charts")
st.subheader("Line Chart")
df=pd.read_csv("lang_data.csv")
lang_list=df.columns.tolist()
lang_choices=st.multiselect("Choose Languages for Comparison ", lang_list)
new_df=df[lang_choices]
st.line_chart(new_df)

st.subheader("Area Chart with same choices")
st.area_chart(new_df)

st.header("Data visualization using plotly")
st.subheader("Displaying the datasets")
df=pd.read_csv("tips.csv")
st.dataframe(df.head())

st.subheader("Pie Chart")
fig=px.pie(df,values="total_bill",names="size")
st.plotly_chart(fig)

st.subheader("Pie Chart with modification")
fig=px.pie(df,values="total_bill",names="day",opacity=.8,color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

# This was running alright on localhost but is giving error on stream lit 

#Here is the traceback :-

# File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 600, in _run_script
#     exec(code, module.__dict__)
# File "/mount/src/streamlit_demo_interactive_graphs/plot.py", line 45, in <module>
#     fig=ff.create_distplot(hist_data,grp_labels,bin_size=[.1,.25,.5])
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# File "/home/adminuser/venv/lib/python3.11/site-packages/plotly/figure_factory/_distplot.py", line 178, in create_distplot
#     validate_distplot(hist_data, curve_type)
# File "/home/adminuser/venv/lib/python3.11/site-packages/plotly/figure_factory/_distplot.py", line 47, in validate_distplot
#     raise ImportError("FigureFactory.create_distplot requires scipy")

#So, it's telling it did not find scipy due to which i am absolutely clueless

st.subheader("Histogram")
x1=np.random.randn(100)
x2=np.random.randn(100)
x3=np.random.randn(100)
hist_data=[x1,x2,x3]
grp_labels=["Grp-1","Grp-2","Grp-3"]
fig=ff.create_distplot(hist_data,grp_labels,bin_size=[.1,.25,.5])
st.plotly_chart(fig)
