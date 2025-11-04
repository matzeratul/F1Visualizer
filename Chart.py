import streamlit as st
import Data
import plotly.graph_objects as go

def resultsTab(results:dict,driverData:dict,laps:dict):
    bestsLaps,bestDriver=Data.bestLap(laps)
    if "points" not in results[0].keys():
        if "country_code" in driverData[list(driverData.keys())[0]].keys():
            country = True
            position,numbers,flags,driver,team,durationTime = st.columns([0.19,0.19,0.1,0.16,0.16,0.2])
            flags.subheader("flags")
        else:
            country = False
            position,numbers,driver,team,durationTime = st.columns([0.19,0.19,0.1,0.16,0.16,0.2])
        ispoints = False
    else:
        if "country_code" in driverData[list(driverData.keys())[0]].keys():
            country = True
            position,numbers,flags,driver,team,durationTime,bestLap,points = st.columns([0.09,0.09,0.08,0.14,0.14,0.18,0.18,0.1])
            flags.subheader("flags")
        else:
            country = False
            position,numbers,driver,team,durationTime,bestLap,points = st.columns([0.09,0.09,0.18,0.18,0.18,0.18,0.1]) 
        ispoints = True
        points.subheader("Points")
        bestLap.subheader("BestsLaps")
    position.subheader("Po.")
    numbers.subheader("NO.")
    driver.subheader("Drivers")
    team.subheader("Teams")
    durationTime.subheader("Time")
    for result in results:
        driverNumber = str(result['driver_number'])
        if result['position']==None and result['dnf']==True:
            position.markdown("DNF")
        elif result['position']==None and result['dns']==True:
            position.markdown("DNS")
        elif result['position']==None:
            position.markdown("DSQ")
        else:
            if result['position'] <=10:
                position.markdown(f'<div style="color:{Data.PositionColor(result["position"])};font-size:100%;margin:0;padding:0;margin-bottom:1rem;line-height:1.6">{result["position"]}</div>', unsafe_allow_html=True)
            else:
                position.markdown(result['position'])
        numbers.markdown(driverNumber)
        if country:
            flags.html(f'''<div style="display:flex;align-items:center;height:100%"><img src="./app/static/{driverData[driverNumber]["country_code"]}.png" alt="{driverData[driverNumber]["country_code"]}" style="width:50px;height:1.6rem;vertical-align:middle;margin:0;padding:0"></div>''')
        driver.markdown(driverData[driverNumber]["full_name"])
        team.markdown(f'<div style="color:{driverData[driverNumber]["team_colour"]};font-size:100%;margin:0;padding:0;margin-bottom:1rem;line-height:1.6">{driverData[driverNumber]["team_name"]}</div>', unsafe_allow_html=True)
        if result['dnf'] == True:
            durationTime.markdown("DNF")
        elif result['dns'] == True:
            durationTime.markdown("DNS")
        elif result['duration']==None and type(result['gap_to_leader']) != str:
            durationTime.markdown("DSQ")
        elif result['duration']==results[0]['duration']:
            if ispoints:
                durationTime.markdown(Data.formatTime(result['duration']))
            else:
                durationTime.markdown(f":violet[{Data.formatTime(result['duration'])}]")
        elif type(result['gap_to_leader']) == float:
            durationTime.markdown('+'+str(result['gap_to_leader']))
        else:
            durationTime.markdown(result['gap_to_leader'])
        if ispoints:
            if driverNumber == bestDriver[0]:
                bestLap.markdown(f":violet[{bestsLaps[driverNumber]}]")
            elif driverNumber not in bestsLaps.keys():
                bestLap.markdown("No Data")
            else:
                bestLap.markdown(f"{bestsLaps[driverNumber]}")
            points.markdown(int(result['points']))

def resultsQualifying(results:dict,driverData:dict):
    position,number,flags,driver,team,q1,q2,q3 = st.columns([0.1,0.1,0.10,0.15,0.1,0.15,0.15,0.15])
    position.subheader("Position")
    number.subheader("Number")
    flags.subheader("Flags")
    driver.subheader("Driver")
    team.subheader("Teams")
    q1.subheader("Q1")
    q2.subheader("Q2")
    q3.subheader("Q3")
    for result in results:
        driverNumber = str(result['driver_number'])
        position.markdown(driverNumber)
        number.markdown(result['position'])
        flags.html(f'''<div style="display:flex;align-items:center;height:100%"><img src="./app/static/{driverData[driverNumber]["country_code"]}.png" alt="{driverData[driverNumber]["country_code"]}" style="width:50px;height:1.6rem;vertical-align:middle;margin:0;padding:0"></div>''')
        driver.markdown(driverData[driverNumber]['full_name'])
        team.markdown(f'<div style="color:{driverData[driverNumber]["team_colour"]};font-size:100%;margin:0;padding:0;margin-bottom:1rem;line-height:1.6">{driverData[driverNumber]["team_name"]}</div>', unsafe_allow_html=True)
        q1.markdown(Data.formatTime(result['duration'][0]))
        if result['duration'][1] != None:
            q2.markdown(Data.formatTime(result['duration'][1]))
        if result['duration'][2] != None:
            q3.markdown(Data.formatTime(result['duration'][2]))

def positionChart(driverData:dict,positionData:dict):
    fig = go.Figure(skip_invalid=True)
    colors=[]
    for i in driverData:
        if f"#{driverData[i]['team_colour']}" in colors:
            fig.add_trace(go.Scatter(
                x=list(positionData[i].keys()),
                y=list(positionData[i].values()),
                name=driverData[i]['name_acronym'],
                line=dict(color=driverData[i]['team_colour'],width=3,dash="dashdot"),
                hovertemplate=f"position n°%{{y}} at lap n°%{{x}} for {driverData[i]['full_name']} <extra></extra>"))
        else:
            colors.append(f"#{driverData[i]['team_colour']}")
            fig.add_trace(go.Scatter(
                x=list(positionData[i].keys()),
                y=list(positionData[i].values()),
                name=driverData[i]['name_acronym'],
                line=dict(color=driverData[i]['team_colour'],width=3),
                hovertemplate=f"position n°%{{y}} at lap n°%{{x}} for {driverData[i]['full_name']} <extra></extra>"))

    fig.update_layout(
        autosize=False,
        height=575,
        title=dict(text="driver positions throughout the Race"),
        xaxis=dict(title=dict(text="laps")),
        yaxis=dict(autorange='reversed'))
    st.plotly_chart(fig,config={'scrollZoom': False,'displayModeBar': False})

def tyreChart(tyreData:dict,driverData:dict):
    fig = go.Figure(skip_invalid=True)
    for driver in driverData:
        for i in tyreData[driver]:
            if i['new']:
                fig.add_trace(go.Bar(
                    y=[driverData[driver]['name_acronym']],
                    x=[i['endingLap']-i['startingLap']+1],
                    name='',
                    marker=dict(color=Data.tyreColor(i['compound'])),
                    orientation='h',
                    showlegend=False,
                    hovertemplate=f"{i['endingLap']-i['startingLap']} Laps in {i['compound']} {driverData[driver]['full_name']}<extra></extra>"))
            else:
                fig.add_trace(go.Bar(
                    y=[driverData[driver]['name_acronym']],
                    x=[i['endingLap']-i['startingLap']+1],
                    name='',
                    marker=dict(pattern=dict(shape='/', fgcolor=Data.tyreColor(i['compound']), size=8, solidity=0.5)),
                    orientation='h',
                    showlegend=False,
                    hovertemplate=f"{i['endingLap']-i['startingLap']} Laps in used {i['compound']} {driverData[driver]['full_name']}<extra></extra>"))
            fig.add_trace(go.Scatter(
                x=[i['endingLap']],
                y=[driverData[driver]['name_acronym']],
                mode='markers+text',
                marker=dict(symbol='circle', size=18, color='black'),
                text=[str(i['endingLap'])],
                textposition='middle center',
                textfont=dict(color='white', size=12),
                showlegend=False,
                hovertemplate=f"Lap {i['endingLap']}<extra></extra>"
            ))
    fig.update_layout(
        autosize=False,
        height=650,
        title=dict(text="tyres compounds throughout the session"),
        xaxis=dict(title=dict(text="laps")),
        yaxis=dict(autorange='reversed'),
        barmode='stack',
        margin=dict(b=140),
        legend=dict(
            orientation='h',
            yanchor='top',
            y=-0.18,
            x=0.5,
            xanchor='center',
            itemclick=False,
            itemdoubleclick=False)
        )
    # add custom legend entry for each compound
    fig.add_trace(go.Bar(
            x=[0],
            y=[0],
            marker=dict(color="gray", pattern=dict(shape='/', fgcolor='gray', size=16, solidity=0.5)),
            name="Used",
            showlegend=True,
            visible='legendonly',
            hoverinfo='skip'
        ))
    fig.add_trace(go.Scatter(
            x=[0],
            y=[0],
            mode='markers',
            marker=dict(size=16, color="gray", symbol='square'),
            name="New",
            showlegend=True,
            visible='legendonly',
            hoverinfo='skip'
        ))
    ledgend = ["SOFT","MEDIUM","HARD","INTERMEDIATE","WET"]
    for compound in range(len(ledgend)-1,-1,-1):
        fig.add_trace(go.Scatter(
            x=[0],
            y=[0],
            mode='markers',
            marker=dict(size=16, color=Data.tyreColor(ledgend[compound]), symbol='square'),
            name=ledgend[compound],
            showlegend=True,
            visible='legendonly',
            hoverinfo='skip'
        ))
    st.plotly_chart(fig,config={'scrollZoom': False,'displayModeBar': False})