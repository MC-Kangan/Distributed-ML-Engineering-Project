#/usr/bin/bash

for COUNT in 1 2 3 4 5
do
 echo "Creating $COUNT"
 echo $COUNT > file_$COUNT.txt
 value=$(cat file_$COUNT.txt)
 value=$(($value*5))
 echo "$value"
done
