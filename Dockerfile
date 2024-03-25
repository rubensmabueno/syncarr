FROM python:3.11-slim

ENV APP_HOME /opt/syncarr

RUN apt-get update && \
    apt-get install -y ffmpeg redis-server gcc && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p $APP_HOME

WORKDIR $APP_HOME

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY syncarr syncarr
COPY standalone.sh standalone.sh

ENV PYTHONPATH=$APP_HOME:$PYTHONPATH

EXPOSE 5000

CMD ["/opt/syncarr/standalone.sh"]
