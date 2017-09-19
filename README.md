[![Build Status](https://travis-ci.org/joaodaher/store-n-search-api.svg?branch=master)](https://travis-ci.org/joaodaher/store-n-search-api)
[![Coverage Status](https://coveralls.io/repos/github/joaodaher/store-n-search-api/badge.svg)](https://coveralls.io/github/joaodaher/store-n-search-api)
[![python](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/)
[![django](https://img.shields.io/badge/django-1.11-green.svg)](https://www.djangoproject.com/)
[![elasticsearch](https://img.shields.io/badge/elasticsearch-5.5-orange.svg)](https://www.elastic.co/products/elasticsearch)
# Store 'n Search API
API for storing events and searching them.


## Usage

### Store Event

Save a new event by performing a POST request with the event's name and timestamp.

`curl -H "Content-Type: application/json" -X POST -d '{"name":"buy","timestamp":"2016­09­22T13:57:31.2311892­04:00"}' http://localhost:8000/v1/events/`


### Search Event

Use the query parameter `q` with an URL encoded string to perform an autocomplete in event names.

`curl -H "Content-Type: application/json" -X GET 'http://localhost:8000/v1/events/?q=bu`


### List Events

Get a paginated list of all events.

`curl -H "Content-Type: application/json" -X GET 'http://localhost:8000/v1/events/?page=0&pagination=10`


### Detail Event

Get more details about an event using its unique identifier.

`curl -H "Content-Type: application/json" -X GET 'http://localhost:8000/v1/events/1/`


## Setup
  - clone this project
  - setup [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)
  - create a virtualenv (`mkvirtualenv store-search-api --python=python3`)
  - install dependencies (`pip install -r requirements.txt`)

## Running the app
  - sync your database (if needed): `python manage.py migrate`
  - fire up the server: `python manage.py runserver`
  

## Tests
To run tests, run `manage.py test --settings=settings.test`.

  To get a better code coverage report, you can generate an HTML file with
  `coverage run --source='.' manage.py test  --settings=settings.test && coverage html`
  and opening the `html-coverage/index.html` file in your browser.
> Assure `COVERALLS_SERVICE_NAME` and `COVERALLS_REPO_TOKEN` are defined in Travis's configuration file to enable coverage integration.

## Lint
To check the code style, run `flake8`.
> If you do not have Flake installed, run: `pip install flake8`

## APM Monitoring
New Relic can be configured using [environment vars](https://docs.newrelic.com/docs/agents/python-agent/installation-configuration/python-agent-configuration#environment-variables).
