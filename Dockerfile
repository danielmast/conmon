FROM python:3.8-alpine
RUN pip install speedtest-cli
RUN mkdir /data
COPY main.py /
COPY ping.py /
CMD ["python", "-u", "main.py", "/data/log.csv"]
