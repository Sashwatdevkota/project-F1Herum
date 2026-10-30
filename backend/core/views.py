import json
import urllib.request
from rest_framework.decorators import api_view
from rest_framework.response import Response

def get_f1_standings():
    url = "https://api.jolpi.ca/ergast/f1/2026/driverStandings.json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data


@api_view(["GET"])
def driver_standings(request):
    data=get_f1_standings()
    standings_list = data["MRData"]["StandingsTable"]["StandingsLists"]
    if not standings_list:
        return Response({
            "status":"Error",
            "message":"No data could be found"
        })
    driver_standings = standings_list[0]["DriverStandings"] 
    return Response({
        "status": "success",
        "Total Driver": len(driver_standings),
        "drivers": driver_standings
    })
    
    
@api_view(["GET"])
def first_driver_name(request):
    data=get_f1_standings()
    given_name = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["givenName"]
    return Response({
        "status": "success",
        "Driver Name": given_name,
    })
    


#API view for health check
@api_view(["GET"])
def health_check(request):
    return Response({
        "status": "ok",
        "message": "F1 Herum API is running"
    })

