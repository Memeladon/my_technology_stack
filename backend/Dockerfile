FROM python:3.11.0

COPY public/ public/
COPY src/ src/
COPY Pipfile .
COPY docker.env .env

RUN pip install pipenv
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

CMD ["sh", "-c", "pipenv run uvicorn src.server:app --host 0.0.0.0 --port 5000 --proxy-headers --forwarded-allow-ips=*"]
