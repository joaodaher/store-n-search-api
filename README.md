[![Build Status](https://travis-ci.org/joaodaher/store-n-search-api.svg?branch=master)](https://travis-ci.org/joaodaher/store-n-search-api)
[![Coverage Status](https://coveralls.io/repos/github/joaodaher/store-n-search-api/badge.svg)](https://coveralls.io/github/joaodaher/store-n-search-api)
[![python](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/)
[![django](https://img.shields.io/badge/django-1.11-green.svg)](https://www.djangoproject.com/)
# Python API Biolerplate
API boilerplate for boosting creation of new Python APIs.


## Setup
  - clone this project
  - setup [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)
  - create a virtualenv (`mkvirtualenv eduk-api --python=python3`)
  - install dependencies (`pip install -r requirements.txt`)

## Running the app
  - sync your database (if needed): `python manage.py migrate`
  - fire up the server: `python manage.py runserver`
  

## Tests
To run tests, run `manage.py test --settings=settings.test`.

  The minimum code coverage is set to 90%.
  To get a better code coverage report, you can generate an HTML file with
  `coverage run --source='.' manage.py test  --settings=settings.test && coverage html`
  and opening the `html-coverage/index.html` file in your browser.
> Assure `COVERALLS_SERVICE_NAME` and `COVERALLS_REPO_TOKEN` are defined in Travis's environment variables to enable coverage integration.

## Lint
To check the code style, run `flake8`.
> If you do not have Flake installed, run: `pip install flake8`

## APM Monitoring
New Relic can be configured using [environment vars](https://docs.newrelic.com/docs/agents/python-agent/installation-configuration/python-agent-configuration#environment-variables).
