#!/bin/bash

#shows screen size in density-independent pixels (dp) of device connected via adb

density=$(adb shell wm density)
dens_num=$(echo $density | tr -dc '0-9')
ratio=$(bc<<<"scale=2;$dens_num/160")

screen_size=$(adb shell wm size)
screen_size=${screen_size##*: }
width=${screen_size%x*}
height=$(echo ${screen_size##*x} | tr -dc '0-9')

dp_width=$(bc<<<"$width/$ratio")
dp_height=$(bc<<<"$height/$ratio")

echo Screen size in dp: ${dp_width}x$dp_height
