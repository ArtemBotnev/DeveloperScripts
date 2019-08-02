#!/bin/bash

# Created by Artem Botnev on 01/18/2019
# script for build Spring Boot project .jar and deploy it on local machine

location_path=/home/user/java_apps/servers # local file path
external_files=csv_source # additional files

./gradlew clean bootJar
if [[ $# -eq 0 ]]
then
  jar_name=$(ls build/libs | grep .jar)
  jar_path=$(pwd)/build/libs/${jar_name}
  external_files_path=$(pwd)/${external_files}

  cp  ${jar_path} ${location_path}/
  cp  -R ${external_files_path}/. ${location_path}/${external_files}/
  java -jar ${location_path}/${jar_name}
  
fi