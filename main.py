import sys
import os
from uu import Error
os.environ["KERAS_BACKEND"] = "tensorflow"
import keras 
import tensorflow as tf 
from your_model_module import YourModel  # Импортируйте вашу модель здесь

def check_model_path(path):
    if not path.endswith('.keras'):
        print("Путь к модели должен оканчиваться на .keras")
        return False
    return True

if len(sys.argv) > 1:
    model_path = str(sys.argv[1])
    if check_model_path(model_path):
        print("Путь к модели", model_path)
        # Загрузите вашу модель здесь
    else:
        print("Путь к модели не найден, пожалуйста попробуйте еще раз")
        exit()
else:
    print("Путь к модели не найден, пожалуйста попробуйте еще раз")
    exit()

# Загрузите вашу модель здесь
try:
    model = YourModel.load(model_path)
except Exception as e:
    print(e)

while True:
    image_path = input("Введите путь до изображения (или 'q' для выхода): ")
    
    if image_path.lower() == 'q':
        break

    # Здесь вы можете использовать вашу модель для определения шрифта на изображении
    result = model.predict(image_path)

    print("Результат работы модели:", result)