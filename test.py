import streamlit as st
import requests
import json


drivers = {}
maxi = 0
intervals = json.loads(requests.get("https://api.openf1.org/v1/intervals?session_key=latest").text)
for interval in intervals:
  if f"{interval['driver_number']}" not in drivers.keys():
    drivers[f"{interval['driver_number']}"] = []
  if interval['interval'] == None:
    drivers[f"{interval['driver_number']}"].append(0.0)
  elif type(interval['interval']) == str:
    drivers[f"{interval['driver_number']}"].append(90.0)
  else:
      drivers[f"{interval['driver_number']}"].append(interval['interval'])

st.dataframe(drivers)
#python -m streamlit run test.py

