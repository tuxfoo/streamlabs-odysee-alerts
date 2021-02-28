# streamlabs-odysee-alerts
A shell script that will push alerts about LBC donation's to streamlabs.

This script will convert the current value of LBC into USD and send an alert to streamlabs.

At the moment Odysee live streaming is in testing and I do not have an invite to help test it. I have no idea what chat system it is using to create the bot component for this.

This is a bash script, so it will only work on Linux and maybe Mac and BSD.

If you would like to test it, you will need to generate an access token for streamlabs (see https://github.com/stream-labs/streamlabs-api-demo)

USAGE
./streamlabs-odysee-alert.sh LBC_AMOUNT DONOR_NAME
./streamlabs-odysee-alert.sh 54 Billy
