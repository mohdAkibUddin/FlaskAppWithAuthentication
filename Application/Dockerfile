FROM python:3.8

EXPOSE 5000

WORKDIR /app
ENV FLASK_RUN_HOST=localhost
COPY requirements.txt /app
RUN pip install  -r requirements.txt --upgrade pip

COPY . /app

CMD python app.py