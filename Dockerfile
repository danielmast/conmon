FROM python:3.8-alpine
RUN pip install speedtest-cli
COPY main.py /
COPY ping.py /
CMD ["python", "-u", "main.py"]
