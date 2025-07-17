FROM python:3.11

# Instala certificados SSL si es necesario
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Aseguramos que el puerto expuesto coincide con el que la aplicación utilizará
EXPOSE 3001

# Iniciar el servidor en el puerto correcto
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "3001"]


