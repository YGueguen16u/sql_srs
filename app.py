import streamlit as st
import pandas as pd
import duckdb


tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
data = {"a" : [1, 2, 3], "b" : [4, 5, 6], "c" : [7, 8, 9]}
with tab1:
    sql_query = st.text_area(label = "write tour input")
    result = duckdb.query(sql_query)
    st.write(f"your query : {sql_query}")
    st.dataframe(result)

