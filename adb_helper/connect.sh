#!/bin/bash

# Created by Artem Botnev on 05/05/2019
# adb connect fast helper

# example of usage:

# ./connect.sh 5
# will run -> adb connect 10.10.21.46:2111

# ./connect.sh -r
# will run -> adb kill-server

# ./connect.sh -r 5
# will run -> adb kill-server $$ adb connect 10.10.21.46:2111

# ./connect.sh -a 90
# will run -> adb connect 10.10.21.90:2111

# ./connect.sh -ra 90
# will run -> adb kill-server $$ adb connect 10.10.21.90:2111

# url, port, mode{your_device_name}addr must be specified for devices

url=10.10.21
port=2111

mode5addr=46
mode72addr=88
mode73addr=89
mode10addr=47

connect_to () {
    adb connect ${url}.$1:${port}
    exit 0
}

connect_by_mode () {
    case $1 in
    5) connect_to $mode5addr
    ;;
    10) connect_to $mode10addr
    ;;
    72) connect_to $mode72addr
    ;;
    73) connect_to $mode73addr
    ;;
    *) echo found no devices with such address
    esac
}

check_arg_and_connect() {
    if [[ $1 =~ ^[0-9]+$ ]] 
        then connect_by_mode $1 
    else
        exit 0
    fi
}
 
while getopts "a:r" opt
do
    case $opt in
        r) adb kill-server
        ;;
        a) connect_to $2
    esac
done

if [[ $# -eq 1 ]]
    then check_arg_and_connect $1
    else check_arg_and_connect $2
fi
