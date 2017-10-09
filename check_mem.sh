#!/bin/bash


total=`free -m | grep Mem | awk '{print $2}'`
used=`free -m | grep buf | awk '{print $3}' | tail -n 1`
perc=`echo $total $used | awk '{ print $2*100/$1}'| cut -f 1 -d .`



if [ $perc -ge 0 ]; then


if [ $perc -lt $2 ]; then #CRIT
    if [ $perc -lt $1 ]; then #WARN
        echo "Memory OK - $perc% used"
        exit 0
            else echo "Memory WARNING - $perc% used"
            exit 1
                fi
                else echo "Memory CRITICAL - $perc% used"
                exit 2
                fi

                else echo "Memory CRITICAL - !!!"
                exit 2

fi
