FROM python:3.8-slim

WORKDIR /code

RUN pip install falcon==3.0.1

COPY src/ .

CMD ["python", "main.py"]