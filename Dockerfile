FROM python:3.10.9-slim
WORKDIR /flask_auth
COPY prod.env .env
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir
COPY /flask_auth .
CMD ["gunicorn", "wsgi_app:app", "--bind", "0.0.0.0:5000", "--reload"]
