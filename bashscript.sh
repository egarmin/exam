#!/bin/bash

prefix=`date +%F`
path=/tmp/exam/
fname=$path/$prefix.dat
mkdir -p /tmp/exam
python manage.py allmodels 2>$fname
echo Log stderr in \"$fname\" file.