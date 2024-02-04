import requests, json, datetime,pytz
from requests.auth import HTTPBasicAuth
#URL de l'API Prochains Passages de source IDFM - requête unitaire
url = "https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=STIF%3AStopArea%3ASP%3A43122%3A&LineRef=STIP%3ALine%3A%3AC01743%3A"
#Le header doit contenir la clé API : apikey, veuillez remplacer #VOTRE CLE API par votre clé API
headers = {"Accept": "application/json","apikey": "rrQPwOvQUnqinvU1De0sgLnl9NDmo2uj"}

def get_horaire(type, num, stop):
	req = requests.get(url, headers=headers)
	req=req.json()
	list_passage=[]
	count=0
	for i in req["Siri"]["ServiceDelivery"]["StopMonitoringDelivery"][0]["MonitoredStopVisit"]:
		tmp=i["MonitoredVehicleJourney"]["MonitoredCall"]["DestinationDisplay"][0]["value"]
		if stop==0 and (tmp=="Robinson" or tmp=="Saint-Rémy-Lès-Chevreuse"):
				timed=datetime.datetime.fromisoformat(i["MonitoredVehicleJourney"]["MonitoredCall"]["AimedDepartureTime"].replace("Z", "+01:00"))
				timed=timed.astimezone(pytz.utc).replace(tzinfo=None)
				if timed>=datetime.datetime.now():
					list_passage.append(timed.strftime("%H:%M"))
		elif stop==1 and (tmp=="Aéroport CDG 2 TGV"):
				timed=datetime.datetime.fromisoformat(i["MonitoredVehicleJourney"]["MonitoredCall"]["AimedArrivalTime"].replace("Z", "+01:00"))
				timed=timed.astimezone(pytz.utc).replace(tzinfo=None)
				if timed>=datetime.datetime.now():
					list_passage.append(timed.strftime("%H:%M"))	
		count+=1
	return list_passage

