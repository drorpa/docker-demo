FROM python:3.8-slim

WORKDIR /code
RUN mkdir data

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

CMD ["python", "main.py"]