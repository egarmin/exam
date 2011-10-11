#!/bin/bash

prefix=`date +%F`
fname=$prefix.dat
python manage.py allmodels 2>$fname
