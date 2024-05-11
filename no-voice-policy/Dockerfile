FROM python:3.9-alpine

ADD main.py .
ADD it_IT.txt .
ADD en_US.txt .

RUN pip install telethon

CMD ["python", "./main.py"]
