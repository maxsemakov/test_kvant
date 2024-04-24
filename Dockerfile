# Используем официальный образ tensoflow как базовый
FROM tensorflow/tensorflow:latest

COPY requirements.txt /
# Устанавливаем дополнительные библиотеки, которые могут понадобиться
RUN pip install --no-cache-dir --upgrade-strategy only-if-needed -r requirements.txt
COPY notebooks  /app/notebooks
COPY texts  /app/texts
COPY tmp  /app/tmp
COPY train_1st  /app/train_1st
COPY train_2nd  /app/train_2nd
COPY fonts  /app/fonts

COPY main.py  /app


