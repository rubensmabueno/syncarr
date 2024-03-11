FROM python:3.11-slim

ENV APP_HOME /opt/syncarr

RUN apt-get update && \
    apt-get install -y ffmpeg redis-server gcc && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p $APP_HOME

WORKDIR $APP_HOME

COPY . /syncarr
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY start.sh start.sh

RUN chmod +x $APP_HOME/start.sh

EXPORT PYTHONPATH=$APP_HOME:$PYTHONPATH

EXPOSE 5000

CMD ["$APP_HOME/start.sh"]
