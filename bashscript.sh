#!/bin/bash

prefix=`date +%F`
fname=/tmp/$prefix.dat
#chmod +rx manage.py
manage.py allmodels 2>$fname
echo Log stderr in \"$fname\" file.