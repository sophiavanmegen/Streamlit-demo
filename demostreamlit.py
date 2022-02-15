
import streamlit as st
import pandas as pd
import altair as alt

import pytrends as pt
from pytrends.request import TrendReq
import numpy as np
import yfinance as yf
import datetime as dt
import tweepy as tw
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import gtrend

import os
import seaborn as sns
import itertools
import collections  
import nltk
from nltk.corpus import stopwords
import re
import networkx

import warnings

st.title("Hello World - Lesson 4")
st.text("In the lession, we go through a demo of using the package streamlit to build webapps.")

#st.image('build.jpg')

st.sidebar.title('Contents')

st.write("This is some text")

df = pd.read_csv('happiness_data_clean.csv')
st.dataframe(df)

show_df = st.sidebar.checkbox("Show dataframe")

if show_df:
    st.dataframe(df)


