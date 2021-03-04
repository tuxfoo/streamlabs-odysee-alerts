# streamlabs-odysee-alerts
A bash script that will push alerts about LBC donation's to streamlabs.

This script will convert the current value of LBC into USD and send an alert to streamlabs.

At the moment Odysee live streaming is in testing and I do not have an invite to help test it. I have no idea what chat system it is using to create the bot component for this.

This is a bash script, so it will only work on Linux and maybe Mac and BSD.

If you would like to test it, you will need to generate an access token for streamlabs (see https://github.com/stream-labs/streamlabs-api-demo) I plan to have the bash script generate the token in a future release.

The chat-listener.sh script will monitor a chat log for a string and execute a command. This is intended to be used to listen for tips but could be used for lots of other things too such as skipping a song that is playing on stream.

USAGE
./streamlabs-odysee-alert.sh LBC_AMOUNT DONOR_NAME
./streamlabs-odysee-alert.sh 54 Billy


