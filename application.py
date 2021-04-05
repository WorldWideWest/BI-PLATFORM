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
    sales = app.LineData(data, 'cogs')

    if showData:
        st.dataframe(data)
        
    ## Page Layout declaration ##
    C1, C2, C3, C4 = st.beta_columns([1, 1, 1, 1])
    
    C5, C6 = st.beta_columns([1, 4]) # Heading row
    C7, C8 = st.beta_columns([1, 4])
    
    C9, C10 = st.beta_columns([1, 4]) # Heading row
    C11, C12 = st.beta_columns([1, 4])

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
    
    with C5:
        st.header("Data")
    with C6:
        st.header("Total Sales per Day")
    with C7:
        st.dataframe(sales)
    with C8:
        st.line_chart(sales, use_container_width = True)

    with C9:
        st.header("Filters")
    with C10:
        st.header(f"") # Auto generated header based on the filters applyed

    with C11:
        city = st.selectbox(
            'Select the City',
            (app.GetUnique(data, 'City')))
        
        customer = st.selectbox(
            'Select the type of the Customer',
            (app.GetUnique(data, 'Customer type')))

        gender = st.selectbox(
            'Select the Gender',
            (app.GetUnique(data, 'Gender')))

        product = st.selectbox(
            'Select Product Line',
            (app.GetUnique(data, 'Product line')))

        payment = st.selectbox(
            'Select the type of Payment',
            (app.GetUnique(data, 'Payment')))

        with C12:
            st.dataframe(app.Filter(data, city, customer, gender, product, payment))



