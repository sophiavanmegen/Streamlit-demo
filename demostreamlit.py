
import streamlit as st
import pandas as pd
import altair as alt


st.title("Relationship between google search results and stock price")
st.text("In the past few weeks, we completed a Python course where we investigated the relationship between Google search results and the stock price.")

#st.image('build.jpg')

st.sidebar.title('Contents')
    
st.write("This is some text")


#df = pd.read_csv('happiness_data_clean.csv')
#st.dataframe(df)

show_intro = st.sidebar.checkbox("Introduction")
show_method = st.sidebar.checkbox("Methodology")
show_result = st.sidebar.checkbox("Results")

if show_intro:
    st.title('Introduction') 
    st.write('For our Python project we investigated the relationship between Google search results and the stock price.')

if show_method:
    st.title('Methodology')
    st.write('For our Python project we investigated the relationship between Google search results and the stock price.')
    
if show_result:
    st.title('Results')
    st.write('For our Python project we investigated the relationship between Google search results and the stock price.')
