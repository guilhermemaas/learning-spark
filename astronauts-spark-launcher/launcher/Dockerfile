FROM python:3.10-slim

WORKDIR /app

# Copia e instala dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia a API
COPY api /app/api

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"] 