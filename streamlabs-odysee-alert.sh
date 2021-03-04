#!/bin/bash
dir=$(pwd)
source $dir/settings.sh

LBC=$1
Donor=$2

#You can leave this as is,
REDIRECT_URI=http://localhost:8080/auth
STREAMLABS_API_BASE=https://www.streamlabs.com/api/v1.0

if [[ -z $CLIENT_ID ]] || [[ -z $CLIENT_SECRET ]]; then
  echo "You have not set a client id and secret"
  echo "To set one up, register a new app in streamlabs."
  echo "Make sure to use http://localhost:8080/auth as the redirect"
  echo "Make sure to whitelist yourself."
  echo "Then copy the id and secret into settings.sh"
  echo "Do not show these on stream!"
  exit 1
fi
if [ -z $Token ]; then
  echo "You do not have an API Token"
  echo "Do not show these tokens on stream!"
  echo "To set one up go to the following URL and Authorize the App."
  echo "$STREAMLABS_API_BASE/authorize?client_id=$CLIENT_ID&redirect_uri=http://localhost:8080/auth&response_type=code&scope=donations.read+donations.create"
  echo "Paste the code from the URL"
  read code
  ACCESS=$(curl --request POST --url "$STREAMLABS_API_BASE/token" \
  -d "grant_type=authorization_code&client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET&redirect_uri=http://localhost:8080/auth&code=$code" \
  2>/dev/null | jq -r '.access_token')
  if [[ -z $ACCESS ]]; then
    echo "Something went wrong when attempting to get your access token. Try revoking access under the Connected apps settings in streamlabs."
    exit 1
  fi
  echo "Paste the following access token into settings.sh"
  echo "$ACCESS"
  exit 1
fi
if [[ -z $1 ]] || [[ -z $2 ]]; then
  echo "Missing donor name or amount"
  exit 1
fi
LBC_USD=$(curl -X GET "https://api.coingecko.com/api/v3/simple/price?ids=lbry-credits&vs_currencies=USD" \
-H  "accept: application/json" 2>/dev/null | jq -r '.["lbry-credits"].usd')

USD=$(echo "scale=2; ($LBC_USD*$LBC)" | bc -l)
#Narrow to 2 decimal places
USD=$(printf "%.2f\n" $USD)

echo $Donor just donated \$$USD\USD worth of LBC

curl --request POST --url "$STREAMLABS_API_BASE/donations" \
-d "name=$Donor&identifier=$Donor&amount=$USD&currency=USD&access_token=$Token&skip_alert=no"
printf "\n"
