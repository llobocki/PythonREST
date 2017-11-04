#!/bin/bash

nosetests --with-xunit --with-coverage --cover-package=app --cover-branches --cover-xml --cover-inclusive -I run.py -s
