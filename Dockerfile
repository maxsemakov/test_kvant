# Используем официальный образ tensoflow как базовый для архитектуры x86_64
#FROM tensorflow/tensorflow:latest
# Используем  образ от bitnami как базовый для архитектуры ARM и x86_64
FROM bitnami/tensorflow:latest




COPY notebooks  /app/notebooks
COPY texts  /app/texts
COPY tmp  /app/tmp
COPY train_1st  /app/train_1st
COPY train_2nd  /app/train_2nd
COPY fonts  /app/fonts

COPY main.py  /app
COPY requirements.txt /app

EXPOSE 8888





