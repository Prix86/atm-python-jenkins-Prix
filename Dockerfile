FROM python:3.13-slim

WORKDIR /app

COPY atm.py .
COPY test_atm.py .

CMD ["python", "atm.py"]
