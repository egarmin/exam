#!/bin/bash

prefix=`date +%F`
#mypath=/tmp/exam
#curr=`pwd`
#echo curr = $curr
#echo old = $HOSTNAME
#fname=$curr$mypath/$prefix.dat
fname=/var/tmp/$prefix.dat
#mkdir -p $curr$mypath
#PATH=${PATH}:$curr
python manage.py allmodels 2>$fname
#echo Log stderr in \'$fname\' file.