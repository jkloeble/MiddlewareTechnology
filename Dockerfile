# Anleitung fürs Image 
# Haus -> Muss gegeben sein um an Backen zu denken 
FROM python:3.10

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ /app

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80", "--reload"]