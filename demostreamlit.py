
import streamlit as st
import pandas as pd
import altair as alt


st.title("Relationship between google search results and stock price")
st.text("In the past few weeks, we completed a Python course where we investigated the relationship between google search results and the stock price.")

#st.image('build.jpg')

st.sidebar.title('Contents')


def home():
    st.title("Home")
    st.markdown("Please find help **here**")

def info():
    st.title("Info")

def myhelp():
    st.title("Help")

menu = {
    "Home": home,
    "Info": info,
    "Help": myhelp
}

def main():
    menu_item = st.sidebar.radio(
        "Navigation",
        ["Home", "Info", "Help"]
    )

    menu[menu_item]()
    
st.write("This is some text")


#df = pd.read_csv('happiness_data_clean.csv')
#st.dataframe(df)

show_df = st.sidebar.checkbox("Show dataframe")

if show_df:
    st.dataframe(df)


