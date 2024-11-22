import streamlit as st
from datetime import datetime
import pandas as pd
import requests



'''
# TaxiFareModel front
'''


d = st.date_input("Pickup date")
t = st.time_input("Pickup time")
# date_and_time = datetime.combine(d, t)
date_and_time = f'{d} {t}'

p_lat = st.number_input("Pickup latitude", format="%.6f", step=1e-6)
p_lon = st.number_input("Pickup longitude", format="%.6f", step=1e-6)

d_lat = st.number_input("Dropoff latitude", format="%.6f", step=1e-6)
d_lon = st.number_input("Dropoff longitude", format="%.6f", step=1e-6)

p = st.selectbox("Number of passengers", [i for i in range(1, 11)])


url = 'https://taxifare.lewagon.ai/predict'

api_dict = dict(
    pickup_datetime=[date_and_time],
    pickup_longitude=[p_lon],
    pickup_latitude=[p_lat],
    dropoff_longitude=[d_lon],
    dropoff_latitude=[d_lat],
    passenger_count=[p]
)
response = requests.get(url, api_dict)
fare = response.json()['fare']
st.write(f"Price of the ride is ${fare:.2f}")
