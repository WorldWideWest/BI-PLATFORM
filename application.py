import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from scripts.parser import Application

## Config ##
st.set_page_config(layout='wide')
app = Application()

pageOptions = ('Preview premade project', 'Add your own data')
pageSelector = st.sidebar.selectbox(
    "Select the site type",
    pageOptions
)

if pageSelector == pageOptions[0]:

    showData = st.checkbox('Preview data', value = True)
    ## Required data ## 

    data = app.Import('dataSet/rawData')
    date = app.DateSum(data, 'Date')


    if showData:
        st.dataframe(data)

    C1, C2, C3, C4 = st.beta_columns([1, 1, 1, 1])

    with C1:
        gender = app.PiePlot(data, 'Gender', ["#001024", "#FF800B"], 'Participation of Gender in the dataset')
        st.pyplot(gender)

    with C2:
        customer = app.PiePlot(data, 'Customer type', ["#001024", "#FF800B"], 'Types of Customers in the dataset')
        st.pyplot(customer)

    with C3:
        city = app.PiePlot(data, 'City', ["#001024", "#FF800B", "#840032"], 'Cities participation in sales')
        st.pyplot(city)

    with C4:
        payment = app.PiePlot(data, 'Payment', ["#001024", "#FF800B", "#840032"], 'Payment option')
        st.pyplot(payment)




