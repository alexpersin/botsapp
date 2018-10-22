FROM python:3.6-slim

WORKDIR /app

COPY . /app

RUN pip3 install -U -r /app/requirements.txt
RUN pip3 install -U -r /app/adapters/slack/requirements.txt

EXPOSE 3000

CMD ["python3", "run.py"]
