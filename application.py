import streamlit as st
from scripts.parser import Import

data = Import('dataSet/rawData')

st.dataframe(data)
