# Используем официальный образ Jupyter Notebook как базовый
FROM tensorflow/tensorflow:latest

# Устанавливаем дополнительные библиотеки, которые вам могут понадобиться
RUN pip install pandas numpy matplotlib seaborn
RUN pip install --upgrade keras keras_cv tensorflow
RUN pip install tensorflow-metal