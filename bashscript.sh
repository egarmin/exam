#!/bin/bash

prefix=`date +%F`
fname=$prefix.dat
#chmod +rx manage.py
manage.py allmodels 2>$fname
echo Log stderr in \"$fname\" file.