FROM python

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8015

CMD ["uvicorn", "api_handler:app", "--host=0.0.0.0", "--port=8015", "--reload"]