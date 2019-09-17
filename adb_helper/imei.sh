#!/bin/bash

# Created by Artem Botnev on 05/12/2019
# shows imei of device connected via adb

imei=$(adb shell service call iphonesubinfo 1 | awk -F "'" '{print $2}' | sed '1 d' | tr -d '.' | awk '{print}' ORS=)
echo device imei\: $imei 
