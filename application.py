import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from scripts.parser import Import, Mapper

data = Import('dataSet/rawData')

st.dataframe(data)

C1, C2 = st.beta_columns([1,1])

with C1:
    gender = (data[data['Gender'] == 'Male'].count()[0],
              data[data['Gender'] == 'Female'].count()[0])

    fig, ax = plt.subplots()
    plt.pie(gender, colors =["#001024", "#FF800B"], explode = (0.01, 0),
        autopct = '%1.2f%%', shadow = True, startangle = 90, textprops = {'color': 'white'})

    fig.patch.set_facecolor('blue')
    fig.patch.set_alpha(0)

    plt.title(f'Participation of Gender in the dataset', fontdict = {
        'fontsize': 14, 
        'fontweight': 'bold',
        'color': 'white'
    })

    plt.legend(['Male', 'Female'])
    st.pyplot(fig)
    