import requests
import json
import streamlit as st
import pandas as pd

test=json.loads(requests.get("https://api.openf1.org/v1/session_result?session_key=7782").text)

st.write(test[0])
st.dataframe(pd.DataFrame(json.loads(requests.get("https://api.openf1.org/v1/session_result?session_key=7782").text)))


for i in range(19):
    st.write(json.loads(requests.get(f"https://api.openf1.org/v1/drivers?driver_number={test[i]['driver_number']}&session_key=9158").text)[0]['name_acronym'])