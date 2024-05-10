FROM python:3.9-alpine

ADD main.py .
ADD it-IT.txt .

RUN pip install telethon

CMD ["python", "./main.py"]