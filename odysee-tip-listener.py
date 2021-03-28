import requests
import json
import re
import time

# Basic script to listen for tips with a valid signing channel on stream and activate a stream alert using simple-alerts.
# Change this to your stream claim_id for each stream
claim_id = "e78621e7ea5ddb580147f8be5cd8abf8fee35d2d"

received = "true"
tips = []

# Make sure to change these to your alert names that you have set up in simple-alerts
# First do is equals too (special numbers for unique alerts such as 420)
# Then go by decending amount
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
    alert = {"name":alertName, "message":"(" + name + ") tipped (" + str(amount) + ") LBC"}
    req = requests.post(url, data=alert)
    return

# Function to get username/channel name of tipper
def get_channel(id):
    url = "http://localhost:5279/"
    payload = '{"method": "claim_search", "params": {"claim_id": "' + id + '"}}'
    response = requests.post(url, data=payload)
    result = json.loads(response.text)
    return result["result"]["items"][0]["name"]

while True:
    url = "http://localhost:5279/"
    payload = '{"method": "support_list", "params": {"claim_id": "' + claim_id + '", "received": ' + received + ', "page_size":' + '10' + '}}'
    header = "{'content-type': 'applicati1on/json', 'Accept-Charset': 'UTF-8'}"
    response = requests.post(url, data=payload)
    result = json.loads(response.text)
    #check if tip is new
    for tip in result["result"]["items"]:
        if tip["txid"] not in tips:
            tips.append(tip["txid"])
            timestamp = int(tip["timestamp"])
            # Ignore if tip is older than 2 hours
            if timestamp < int(time.time()) - 7200:
                try:
                    channel = get_channel(tip["signing_channel"]["channel_id"])
                    print(channel + ": " + tip["amount"])
                    alert(channel, tip["amount"])
                except:
                    print("No signing channel")
