FROM python:3

# Establecer el directorio de trabajo
WORKDIR /usr/src/app

# Copiar los archivos del proyecto
COPY requirements.txt ./
COPY ./src ./src

# Instalar dependencias
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Establecer PYTHONPATH para permitir imports absolutos desde src
ENV PYTHONPATH=/usr/src/app/src

EXPOSE 3001

# Ejecutar server.py como módulo dentro de src
CMD ["python", "-m", "src.server"]

