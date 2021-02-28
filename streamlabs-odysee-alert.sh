#!/bin/bash

LBC_USD=$(curl -X GET "https://api.coingecko.com/api/v3/simple/price?ids=lbry-credits&vs_currencies=USD" \
-H  "accept: application/json" 2>/dev/null | jq -r '.["lbry-credits"].usd')
LBC=$1
Donor=$2
#Place API token here
Token=

USD=$(echo "scale=2; ($LBC_USD*$LBC)" | bc -l)
#Narrow to 2 decimal places
USD=$(printf "%.2f\n" $USD)

echo $Donor just donated \$$USD\USD worth of LBC

curl --request POST --url 'https://streamlabs.com/api/v1.0/donations' \
-d "name=$Donor&identifier=$Donor&amount=$USD&currency=USD&access_token=$Token&skip_alert=no" &> /dev/null
