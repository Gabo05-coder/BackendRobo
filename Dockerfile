# Usa la imagen base de Python
FROM python:3.10.6-alpine3.16

# Establece la variable de entorno para evitar la generación de archivos de bytecode (.pyc)
ENV PYTHONDONTWRITEBYTECODE 1
# Desactiva el búfer de salida de Python para que las salidas se muestren inmediatamente
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto al directorio de trabajo
COPY . /app/

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Ejecuta el comando para iniciar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
