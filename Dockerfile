FROM python:3.11-slim

# Instala dependências de sistema necessárias para o mysqlclient funcionar
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Instala as dependências Python
RUN pip install --upgrade pip
RUN pip install flask flask-mysqldb

CMD ["python", "app.py"]
