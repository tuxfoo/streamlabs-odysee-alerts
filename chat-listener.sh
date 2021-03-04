#!/bin/bash

# Need a way to save Odysee chat to a log file in real time,
# This script will monitor the chat for tips.
# The backend for the live chat is not yet known nor is what is output to
# the chat when someone tips. When we have this information then we can use
# regex (grep, sed or awk) to listen for these events and execute a command
# such as pushing a alert to streamlabs or doing something locally such as
# playing the next song in a playlist.

tail -fn0 chat.log | \
while read line ; do
        echo "$line" | grep "Tip"
        if [ $? = 0 ]
        then
                #./streamlabs-odysee-alert.sh $amount $donor
                echo "Match"
        fi
done
