FROM python:3.6

RUN adduser --disabled-password --gecos '' ss

RUN mkdir -p /usr/src/ss
WORKDIR /usr/src/ss

ADD requirements.txt /usr/src/ss/
RUN pip install --no-cache-dir -r requirements.txt

ADD docker/web/run_web.sh /usr/src/

RUN mkdir /var/log/ss
RUN chown -R ss:ss /var/log/ss

ADD store_search_api /usr/src/ss
WORKDIR /usr/src/ss