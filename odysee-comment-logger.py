import requests
import json
import re

# Change this to your stream claim_id for each stream
claim_id = "e78621e7ea5ddb580147f8be5cd8abf8fee35d2d"
include_replies = "false"
skip_validation = "false"
is_channel_signature_valid = "false"
visible = "false"
hidden = "false"
comments = []

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

def isCommentEvent(comment):
    test = "@Billy Tipped 5.40 LBC"
    #Still need to find out how tips are displayed in comments for this regex
    tip = "^@(.+?[^:])\sTipped\s(.+?)\sLBC"
    reg = re.search(tip, comment)
    if reg:
        #print("isTIP")
        alert(reg.group(1), reg.group(2))
    return False

while True:
    url = "http://localhost:5279/"
    payload = '{"method": "comment_list", "params": {"claim_id": "' + claim_id + '", "include_replies": ' + include_replies + ', "skip_validation": ' + skip_validation + ', "is_channel_signature_valid": ' + is_channel_signature_valid + ', "visible": ' + visible + ', "hidden": ' + hidden +'}}'
    header = "{'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}"
    response = requests.post(url, data=payload)
    result = json.loads(response.text)

    #check if comment is new
    for comment in result["result"]["items"]:
        if comment["comment_id"] not in comments:
            comments.append(comment["comment_id"])
            print(comment["channel_name"] + ": " + comment["comment"])
            with open("chat.log", "a") as myfile:
                myfile.write(comment["channel_name"] + ": " + comment["comment"] + "\n")
            #Trigger events
            isCommentEvent(comment["comment"])
