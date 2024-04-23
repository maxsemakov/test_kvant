# Используем официальный образ tensoflow как базовый
FROM tensorflow/tensorflow:latest

COPY requirements.txt /
# Устанавливаем дополнительные библиотеки, которые могут понадобиться
RUN pip install --no-cache-dir --upgrade-strategy only-if-needed -r requirements.txt

RUN apt-get update && apt-get install -y git

COPY fonts  /app/fonts
COPY notebooks  /app/notebooks
COPY texts  /app/texts
COPY tmp  /app/tmp
COPY train_1st  /app/train_1st
COPY train_2nd  /app/train_2nd
#COPY .gitattributes  /app
#COPY .gitignore  /app
COPY task.txt  /app


CMD ["jupyter", "notebook", "--notebook-dir=/app/notebooks", "--ip=0.0.0.0", "--port=8888", "--allow-root"]

