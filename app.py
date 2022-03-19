from pandas import DataFrame
import streamlit as st
from scraper import *

st.write('Hello World')

# Fetch the details of the restaurant
details = fetchRestaurantDetails(parent_table)

# Transform the details of the restaurant into a dataframe
data = transformToDataframe(details)

print(DataFrame)