FROM python:3.5-slim
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

CMD ["python", "main.py", "--log info"]