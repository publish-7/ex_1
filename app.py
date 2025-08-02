import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header("Car Advertisement Data Dashboard")

# Car prices
fig1 = px.histogram(df, x='price')
st.plotly_chart(fig1)

# Price vs Year relationship
# Two columns: one for x-axis, one for y-axis
fig2 = px.scatter(df, x='model_year', y='price', 
                 title='Price vs Year')
st.plotly_chart(fig2)

show_expensive_cars = st.checkbox('Show only cars above $20,000')

if show_expensive_cars:
    clean_df = df[df['price'] > 20000]
    fig3 = px.histogram(clean_df, x='price')
else:
    fig3 = px.histogram(df, x='price')

st.plotly_chart(fig3)

