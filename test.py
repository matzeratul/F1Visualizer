import streamlit as st
import Data
import Chart

#python -m streamlit run test.py


def initRace(sessionProperties):
    results = Data.resultsData(sessionProperties)
    driversData = Data.drivers(sessionProperties,results)
    Chart.resultsTab(results,driversData,Data.lapsData(sessionProperties))
    positionsData = Data.positions(sessionProperties)
    Chart.positionChart(driversData,positionsData)
    tyreData = Data.tyres(sessionProperties,driversData)
    Chart.tyreChart(tyreData,driversData)

st.set_page_config(layout="wide")
sessionProperties=Data.session()
st.write(sessionProperties)
initRace(sessionProperties)