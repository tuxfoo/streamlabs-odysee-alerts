# odysee-tip-listener.py

A script that will query the lbry API for tips made on a odysee livestream. Once a tip is confirmed on the block chain, an alert will be pushed to the simple-alerts nodecg bundle. A tutorial can be found here https://odysee.com/@tuxfoo:e/simple-alerts:9

# streamlabs-odysee-alerts
A bash script that will push alerts about LBC donation's to streamlabs.

This script will convert the current value of LBC into USD and send an alert to streamlabs.

You will need to create a bot to activate the alerts, you could edit the odysee-tip-listener.py to work with this one.

This is a bash script, so it will only work on Linux and maybe Mac and BSD.

#### Instructions for testing:

You will need to register a new app in streamlabs (https://streamlabs.com/dashboard/#/apps/register)
Copy the client_id and client_secret into settings.sh
Make sure to whitelist yourself.
Set http://localhost:8080/auth as the redirect_URL

After you have registered a new app, you need to generate a access token. To do this simply run and follow the instructions:
`./streamlabs-odysee-alert.sh`

USAGE

```bash
./streamlabs-odysee-alert.sh LBC_AMOUNT DONOR_NAME
./streamlabs-odysee-alert.sh 54 Billy
```

The chat-listener.sh script will monitor a chat log for a string and execute a command. This is intended to be used to listen for tips but could be used for lots of other things too such as skipping a song that is playing on stream.
