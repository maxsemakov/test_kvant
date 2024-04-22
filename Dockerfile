# Используем официальный образ tensoflow как базовый
FROM tensorflow/tensorflow:latest

# Устанавливаем дополнительные библиотеки, которые вам могут понадобиться
RUN pip install --no-cache-dir --upgrade-strategy only-if-needed -r requirements.txt

RUN apt-get update && apt-get install -y git

COPY fonts  /app
COPY notebooks  /app
COPY texts  /app
COPY tmp  /app
COPY train_1st  /app
COPY train_2nd  /app
COPY .gitattributes  /app
COPY .gitignore  /app
COPY main.py  /app
COPY requirements.txt  /app
COPY task.txt  /app