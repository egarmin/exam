# Makefile for project testing

install:

	virtualenv --no-site-packages .virtexam
	.virtexam/bin/pip install -r requirements.txt
	.virtexam/bin/python2 manage.py syncdb --noinput
	.virtexam/bin/python2 manage.py runserver 127.0.0.1:8000

test:

	@echo Test in progress...
	@django-nosetests.py -v -exe.
