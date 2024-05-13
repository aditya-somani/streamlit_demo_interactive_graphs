import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff

st.header("Altair Scatter Plot")
chart_data=pd.DataFrame(np.random.randn(100,5),columns=['a','b','c','d','e'])
chart=alt.Chart(chart_data).mark_circle().encode(x="a",y="b",size="c",tooltip=["a","b","c","d","e"])
st.altair_chart(chart)

st.header("Interactive Charts")
st.subheader("Line Chart")
df=pd.read_csv(r"C:\Users\H.P\Desktop\Python\Learning\Libraries\Streamlit\Ref\lang_data.csv")
lang_list=df.columns.tolist()
lang_choices=st.multiselect("Choose Languages for Comparison ", lang_list)
new_df=df[lang_choices]
st.line_chart(new_df)

st.subheader("Area Chart with same choices")
st.area_chart(new_df)

st.header("Data visualization using plotly")
st.subheader("Displaying the datasets")
df=pd.read_csv(r"C:\Users\H.P\Desktop\Python\Learning\Libraries\Streamlit\Ref\tips.csv")
st.dataframe(df.head())

st.subheader("Pie Chart")
fig=px.pie(df,values="total_bill",names="size")
st.plotly_chart(fig)

st.subheader("Pie Chart with modification")
fig=px.pie(df,values="total_bill",names="day",opacity=.8,color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader("Histogram")
x1=np.random.randn(100)
x2=np.random.randn(100)
x3=np.random.randn(100)

hist_data=[x1,x2,x3]
grp_labels=["Grp-1","Grp-2","Grp-3"]
fig=ff.create_distplot(hist_data,grp_labels,bin_size=[.1,.25,.5])
st.plotly_chart(fig)