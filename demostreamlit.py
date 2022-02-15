import streamlit as st
import pandas as pd
import altair as alt


st.title("Hello World - Lesson 4")
st.text("In the lession, we go through a demo of using the package streamlit to build webapps.")

#st.image('build.jpg')

st.sidebar.write('Please select your interests')

st.write("This is some text")

#df = pd.read_csv('happiness_data_clean.csv')
#st.dataframe(df)

show_df = st.sidebar.checkbox("Show dataframe")

if show_df:
    st.dataframe(df)


    import streamlit as st
from helpers import read_markdown

import page_introduction as pi
import page_distances as pd
import page_documentation as doc


# Page settings

st.set_page_config(page_title='CosmΩracle')

#Sidebar settings

#logo, name = st.sidebar.columns(2)
#with logo:
#    image = 'https://github.com/nikosarcevic/CosmOracle/blob/main/images/LogowName.png?raw=true'
#    st.image(image, use_column_width=True)

st.sidebar.write(" ")

pages = {
        "Introduction": pi,
        "Cosmological Distances": pd,
        "Definitions": doc,
    }

st.sidebar.title("Main options")

# Radio buttons to select desired option
page = st.sidebar.radio("", tuple(pages.keys()))

pages[page].show_page()
        
# About
about = read_markdown("docs/markdown/about.md")
st.sidebar.markdown(about)
