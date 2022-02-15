import streamlit as st
import pandas as pd
import altair as alt


st.title("Hello World - Lesson 4")
st.text("In the lession, we go through a demo of using the package streamlit to build webapps.")

#st.image('build.jpg')

st.sidebar.title('Contents')

pages = {
        "Introduction": intro,
        "Methodology": method,
        "Results": result,
    }



# Radio buttons to select desired option
page = st.sidebar.radio("", tuple(pages.keys()))

pages[page].show_page()


st.write("This is some text")

#df = pd.read_csv('happiness_data_clean.csv')
#st.dataframe(df)

show_df = st.sidebar.checkbox("Show dataframe")

if show_df:
    st.dataframe(df)


