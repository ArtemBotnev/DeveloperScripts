#!/bin/bash

# Created by Artem Botnev on 01/26/2019
# script for build Spring Boot project .jar, move and deploy it on remote machine.

remote_name=pi # name of remote machine
remote_addr=192.168.0.13 # address of remote machine
remote_password=raspberrypi # password of remote machine user

remote_path=/home/${remote_name}/java_apps/servers # remote file path
external_files=csv_source # additional files

./gradlew clean bootJar
if [[ $# -eq 0 ]]
then
  jar_name=$(ls build/libs | grep .jar)
  jar_path=$(pwd)/build/libs/${jar_name}
  external_files_path=$(pwd)/${external_files}
  remote=${remote_name}@${remote_addr}

  sshpass -p ${remote_password} scp -r ${jar_path} ${external_files_path} ${remote}:${remote_path}
  if [[ $# -eq 0 ]]
  then
    sshpass -p ${remote_password} ssh -t ${remote} "java -jar ${remote_path}/${jar_name}"

  fi
fi
