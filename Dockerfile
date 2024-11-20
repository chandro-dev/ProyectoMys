# Usar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo requirements.txt y luego instalar las dependencias
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código de la aplicación al contenedor
COPY . .

# Establecer el PYTHONPATH a /app para que Python pueda encontrar los módulos
ENV PYTHONPATH=/app

# Exponer el puerto en el que la app va a correr
EXPOSE 8000

# Comando para ejecutar la app usando uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
