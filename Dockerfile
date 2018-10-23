FROM python:3.6-slim

WORKDIR /app

COPY . /app

ENV SLACK_SIGNING_SECRET e434b217fae6874f93c344f9d6a63905
ENV SLACK_BOT_TOKEN xoxb-409446198770-413041972694-HcyK2RmB5GlcsGuKjwEUc3vV

RUN pip3 install -U -r /app/adapters/slack/requirements.txt

EXPOSE 3000

CMD ["python", "run.py"]
