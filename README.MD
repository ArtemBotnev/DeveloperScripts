## adb util scripts
### connect.sh
Runs adb command "adb connect url:port" for certain device from list.
You should modify ulrs and port for your devices: 
``` sh
url=10.10.21
port=2111

mode5addr=84
mode72addr=88
mode73addr=89
mode10addr=47
```
#### *Usage examples:*
connect to device with mode5addr (adb connect 10.10.21.46:2111)
```sh
./connect.sh 5
```
adb kill-server
```sh
./connect.sh -r
```
kill server and connect to device with mode5addr (kill-server $$ adb connect 10.10.21.46:2111)
```sh
./connect.sh -r 5
```
### imei.sh
Just returns imei of single device connected by adb
