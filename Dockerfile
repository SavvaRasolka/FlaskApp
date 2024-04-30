FROM python:3.9

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD gunicorn --bind ${FLASK_RUN_HOST}:${FLASK_RUN_PORT} run:product_app