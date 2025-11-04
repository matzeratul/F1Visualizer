import streamlit as st
import Data
import Chart

#python -m streamlit run main.py

def initPractice(sessionProperties):
    results = Data.resultsData(sessionProperties)
    driversData = Data.drivers(sessionProperties,results)
    tyreData = Data.tyres(sessionProperties,driversData)
    Chart.resultsTab(results,driversData,Data.lapsData(sessionProperties))
    Chart.tyreChart(tyreData,driversData)

def initQualifying(sessionProperties):
    results = Data.resultsData(sessionProperties)
    driversData = Data.drivers(sessionProperties,results)
    Chart.resultsQualifying(results,driversData)

def initRace(sessionProperties):
    results = Data.resultsData(sessionProperties)
    driversData = Data.drivers(sessionProperties,results)
    Chart.resultsTab(results,driversData,Data.lapsData(sessionProperties))
    positionsData = Data.positions(sessionProperties)
    Chart.positionChart(driversData,positionsData)
    tyreData = Data.tyres(sessionProperties,driversData)
    Chart.tyreChart(tyreData,driversData)

def initsession():
    st.header("Welcolme to F1Visualizer","center")
    st.markdown(
        'made by matzeratul with data from <a href="https://openf1.org/" target="_blank" style="text-decoration:none;">OpenF1</a> in python '
        '<a href="https://github.com/matzeratul/F1Visualizer" target="_blank" style="text-decoration:none;">'
        'F1Visualizer '
        '<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" '
        'style="height:18px; vertical-align:middle; margin-right:8px;">'
        '</a>',
        unsafe_allow_html=True
    )
    st.divider()
    sessionProperties = {}
    year, meeting = st.columns([0.3,0.7])
    year = year.selectbox("year:",(2023,2024,2025),index=None,placeholder="year",label_visibility="collapsed")
    meetings = Data.meeting(year)
    sessionProperties['meeting'] = meeting.selectbox("country:",meetings,index=None,placeholder="meeting",label_visibility="collapsed")
    sessionProperties['sessions'] = Data.sessions(sessionProperties,year)
    if sessionProperties['sessions'] == None:
        st.title("Please choose a meeting")
        return
    buttons = st.columns(len(list(sessionProperties['sessions'])))
    sessions = list(sessionProperties['sessions'].keys())
    for i in range(len(buttons)):
        if buttons[i].button(sessions[i],width="stretch"):
            sessionProperties['type'] = sessions[i]
    if 'type' not in sessionProperties.keys():
        st.header("Please choose a session")
        return
    match sessionProperties['type']:
        case "Race":
            initRace(sessionProperties)
        case "Sprint":
            initRace(sessionProperties)
        case "Qualifying":
            initQualifying(sessionProperties)
        case "Sprint Qualifying":
            initQualifying(sessionProperties)
        case _:
            initPractice(sessionProperties)

st.set_page_config(layout="wide")
initsession()