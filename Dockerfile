FROM python:3
ADD main.py /
ADD ping.py /
RUN pip install speedtest-cli
CMD ["python", "-u", "main.py"]
