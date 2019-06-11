#!/bin/bash

# nosetests --with-xunit --with-coverage --cover-package=app --cover-branches --cover-xml --cover-inclusive -I run.py -s

pytest test/test*.py --junitxml=nosetests.xml --cov=app  --cov-branch
coverage xml
