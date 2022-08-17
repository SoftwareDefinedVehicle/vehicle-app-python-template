#!/bin/bash -x
declare -a arr=("seatadjuster" "vehicledatabroker" "mosquitto" "seatservice")

## now loop through the above array
for i in "${arr[@]}"
do
   echo "Building $i"
   docker build -t localhost:12345/$i-northstar -f northstar/$i/Dockerfile.northstar .
   docker create --name $i-temp localhost:12345/$i-northstar
   docker cp $i-temp:/tmp/northstar/target/northstar/repository ./npk/repository
   docker rm $i-temp
done

