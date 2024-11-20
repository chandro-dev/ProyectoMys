# Usar una imagen base ligera
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY ./app /app/

# Configurar el PYTHONPATH para que incluya el directorio actual (./)
ENV PYTHONPATH=/app

# Exponer el puerto en el que la app va a correr (por ejemplo, 8000)
EXPOSE 8000

# Comando para ejecutar la app usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]