import requests
import json
import re

# Change this to your stream claim_id for each stream
# Basic script to listen for tips with a valid signing channel on stream and activate a stream alert.
claim_id = "edf63b41a82a93bad1d53b159af2e7e1fe119a5e"
received = "true"
tips = []

def alert(name, amount):
    url = 'http://localhost:9090/simple-alerts/alert'
    amount = round(float(amount), 2)
    #Default Alert name, change this to your alert name if you are using simple-alerts
    alertName = "tada"
    #different donation amounts trigger differnt alerts
    if amount == 8.25:
        alertName = "tada825"
    elif amount == 9.27:
        alertName = "tada927"
    elif amount == 5.40:
        alertName = "tada54"
    elif amount == 4.20:
        alertName = "tada420"
    elif amount >= 30:
        alertName = "tada30"
    elif amount >= 15:
        alertName = "tada15"
    #print(req)
    alert = {"name":alertName, "message":"(" + name + ") tipped (" + str(amount) + ") LBC"}
    req = requests.post(url, data=alert)
    return

def get_channel(id):
    url = "http://localhost:5279/"
    payload = '{"method": "claim_search", "params": {"claim_id": "' + id + '"}}'
    response = requests.post(url, data=payload)
    result = json.loads(response.text)
    return result["result"]["items"][0]["name"]

while True:
    url = "http://localhost:5279/"
    payload = '{"method": "support_list", "params": {"claim_id": "' + claim_id + '", "received": ' + received + '}}'
    header = "{'content-type': 'applicati1on/json', 'Accept-Charset': 'UTF-8'}"
    response = requests.post(url, data=payload)
    result = json.loads(response.text)

    #check if comment is new
    for tip in result["result"]["items"]:
        if tip["height"] not in tips:
            tips.append(tip["height"])
            try:
                channel = get_channel(tip["signing_channel"]["channel_id"])
                print(channel + ": " + tip["amount"])
                alert(channel, tip["amount"])
            except:
                print("No signing channel")
