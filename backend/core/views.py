import json
import urllib.request
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def driver_standings(request):
    response=urllib.request.urlopen("https://api.jolpi.ca/ergast/f1/2026/driverStandings.json")
    data=json.loads(response.read())
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
    


#API view for health check
@api_view(["GET"])
def health_check(request):
    return Response({
        "status": "ok",
        "message": "F1 Herum API is running"
    })

