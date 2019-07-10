#!/bin/bash

# adb connect fast helper

# example of usage:

# ./connect.sh 5
# will run -> adb connect 10.10.21.46:2111

# ./connect.sh -r
# will run -> adb kill-server

# ./connect.sh -r 5
# will run -> adb kill-server $$ adb connect 10.10.21.46:2111

# url, port, mode{your_device_name}addr must be specified for devices

url=10.10.21
port=2111

mode5addr=84
mode72addr=88
mode73addr=89
mode10addr=47

terminal_mode=0
condition="_"

args=("$@")
args_count=${#args[@]}

connect_to () {
    adb connect ${url}.$1:${port}
}
    
if [[ args_count -eq 2 ]]
    then terminal_mode=$2
        if [[ $1 -eq "-r" ]]
        then adb kill-server
    fi
    else terminal_mode=$1
fi

case $terminal_mode in
    5) connect_to $mode5addr
    ;;
    10) connect_to $mode10addr
    ;;
    72) connect_to $mode72addr
    ;;
    73) connect_to $mode73addr
    ;;
    -r) adb kill-server
    ;;
    *) echo found no devices with such address
esac