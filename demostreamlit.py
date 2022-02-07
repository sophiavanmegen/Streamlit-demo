import streamlit as st
import pandas as pd
import altair as alt


st.title("Hello World - Lesson 4")
st.text("In the lession, we go through a demo of using the package streamlit to build webapps.")

st.image('build.jpg')

st.sidebar.write('Please select your interests')

st.write("This is some text")

df = pd.read_csv('happiness_data_clean.csv')
#st.dataframe(df)

show_df = st.sidebar.checkbox("Show dataframe")

if show_df:
    st.dataframe(df)

numeric_columns = df.select_dtypes('number').columns.tolist()
var_to_plot = st.sidebar.selectbox("Select a variable to explore", numeric_columns)

st.subheader(f'Plot of the distribution of {var_to_plot} see below:')
st.line_chart(df[var_to_plot])

fig2 = df.plot(var_to_plot, kind='hist', title='Happiness Score and normalized GDP').get_figure()
st.pyplot(fig2)

st.write(alt.Chart(df).mark_circle().encode(x='Freedom', y='Trust', size='GDP per capita', color='GDP per capita', tooltip=['Freedom', 'Trust', 'GDP per capita']))
