# conmon
Simple Dockerized connection monitor in Python

To get it started:
```
docker build -t conmon .
docker run -d -v ~/conmon_logs:/data --restart=always conmon
```
