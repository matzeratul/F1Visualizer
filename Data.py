import requests
import json
from datetime import datetime

def meeting(year):
    yearData=json.loads(requests.get(f"https://api.openf1.org/v1/meetings?year={year}").text)
    meetings=[]
    for i in range(len(yearData)):
        meetings.append(yearData[i]['meeting_name'])
    return meetings

def sessions(sessionProperties,year):
    if sessionProperties['meeting']!=None:
        sessionsName={}
        sessionProperties['meetingKey']=json.loads(requests.get(f"https://api.openf1.org/v1/meetings?year={year}&meeting_name={sessionProperties['meeting']}").text)[0]['meeting_key']
        sessionsData=json.loads(requests.get(f"https://api.openf1.org/v1/sessions?meeting_key={sessionProperties['meetingKey']}").text)
        for i in range(len(sessionsData)):
            sessionsName[sessionsData[i]['session_name']]=sessionsData[i]['session_key']
        return sessionsName

def compare_iso8601(date1: str, date2: str) -> bool:
    """
    Return True if date1 < date2 for two ISO 8601 datetime strings.
    Handles offsets like "+00:00" and trailing "Z".
    """
    def _parse(d: str) -> datetime:
        if d.endswith('Z'):
            d = d[:-1] + '+00:00'
        return datetime.fromisoformat(d)
    return _parse(date1) < _parse(date2)

def formatTime(time:float) -> str:
    hours = str(int(time/3600.0))
    time = time%3600.0
    minutes = str(int(time/60.0))
    time = time%60.0
    seconds = str(int(time))
    milliseconds=str(time)[3:6]
    if hours == '0':
        return minutes+':'+seconds+':'+milliseconds
    else:
        return hours+':'+minutes+':'+seconds+':'+milliseconds

def driver(sessionProperties:dict,number:int):
    return json.loads(requests.get(f"https://api.openf1.org/v1/drivers?driver_number={number}&session_key={sessionProperties['sessions'][sessionProperties['type']]}").text)[0]['name_acronym']

def drivers(sessionProperties:dict,results:dict) -> dict:
    li={}
    for driver in results:
        li[f"{driver['driver_number']}"] = {}
    drivers=json.loads(requests.get(f"https://api.openf1.org/v1/drivers?session_key={sessionProperties['sessions'][sessionProperties['type']]}").text)
    for driver in drivers:
        li[f"{driver['driver_number']}"]['name_acronym'] = driver['name_acronym']
        li[f"{driver['driver_number']}"]['full_name'] = driver['full_name']
        li[f"{driver['driver_number']}"]['team_name'] = driver['team_name']
        li[f"{driver['driver_number']}"]['team_colour'] = f"#{driver['team_colour']}"
        li[f"{driver['driver_number']}"]['country_code'] = driver['country_code']
    return li

def teamColors(driverData:dict) -> dict:
    colors = {}
    for i in driverData.keys():
        colors[i] = driverData[i]['team_colour']
    return colors

def resultsData(sessionProperties:dict) -> dict:
    return json.loads(requests.get(f"https://api.openf1.org/v1/session_result?session_key={sessionProperties['sessions'][sessionProperties['type']]}").text)

def lapsData(sessionProperties:dict) -> dict:
    return json.loads(requests.get(f"https://api.openf1.org/v1/laps?session_key={sessionProperties['sessions'][sessionProperties['type']]}").text)

def GPgridData(sessionProperties:dict) -> dict:
    return json.loads(requests.get(f"https://api.openf1.org/v1/starting_grid?session_key={sessionProperties['sessions']['Qualifying']}").text)

def SprintGridData(sessionProperties:dict) -> dict:
    return json.loads(requests.get(f"https://api.openf1.org/v1/starting_grid?session_key={sessionProperties['sessions']['Sprint Qualifying']}").text)

def bestLap(laps:dict) -> tuple[dict,int]:
    bestLaps = {}
    for i in laps:
        if str(i['driver_number']) not in bestLaps.keys():
            if i['lap_duration']!=None:
                bestLaps[f"{i['driver_number']}"] = i['lap_duration']
        if i['lap_duration']!=None:
            if i['lap_duration']<bestLaps[f"{i['driver_number']}"]:
                bestLaps[f"{i['driver_number']}"] = i['lap_duration']
    bestDriver = None
    for i in bestLaps.keys():
        if bestDriver == None:
            bestDriver = (i,bestLaps[i])
        elif bestLaps[i]<bestDriver[1]:
            bestDriver = (i,bestLaps[i])
        bestLaps[i] = formatTime(bestLaps[i])
    return (bestLaps,bestDriver)

def positions(sessionProperties:dict) -> dict:
    positionsData = {}
    currentPosition = {}
    laps = lapsData(sessionProperties)
    if sessionProperties['type'] == "Sprint":
        grid = SprintGridData(sessionProperties)
    else:
        grid = GPgridData(sessionProperties)
    for i in grid:
        positionsData[f"{i['driver_number']}"] = {"1":i['position']}
    for i in laps:
        currentLap = i['lap_number']
        if not currentLap == 1:
            if f"{currentLap}" not in currentPosition.keys():
                currentPosition[f"{i['lap_number']}"] = 1
            position = currentPosition[f"{currentLap}"]
            positionsData[f"{i['driver_number']}"][f"{currentLap}"] = f"{position}"
            currentPosition[f"{currentLap}"] += 1
    return positionsData

def tyres(sessionProperties:dict,driverData:dict) -> list: 
    tyreData = {}
    stints = json.loads(requests.get(f"https://api.openf1.org/v1/stints?session_key={sessionProperties['sessions'][sessionProperties['type']]}").text)
    for driver in driverData:
        tyreData[driver] = []
    for stint in stints:
        if stint['tyre_age_at_start'] == 0:
            new = True
        else:
            new = False
        if stint['lap_start'] != None:
            tyreData[f"{stint['driver_number']}"].append({"startingLap":stint['lap_start'],"endingLap":stint['lap_end'],"compound":stint['compound'],"new":new})
        else:
            tyreData[f"{stint['driver_number']}"].append({"startingLap":1,"endingLap":1,"compound":stint['compound'],"new":new})
    return tyreData

def tyreColor(compound:str) -> str:
    match compound:
        case "SOFT":
            return"#B23E3B"
        case "MEDIUM":
            return"#DAC738"
        case "HARD":
            return"#D0D4DF"
        case "INTERMEDIATE":
            return"#54A641"
        case "WET":
            return"#2962C1"

def PositionColor(position:int) -> str:
    if int(position) == 1:
        return "#848128"
    elif int(position) == 2:
        return "#ABABAB82"
    elif int(position) == 3:
        return "#854a0e"
    elif int(position)<=10:
        return "#5bbc65"
    else:
        return "#ffffff"