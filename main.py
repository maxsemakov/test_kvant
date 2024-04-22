import os
os.environ["KERAS_BACKEND"] = "tensorflow"  
import sys
import keras_cv
import keras
#from tensorflow import keras
from keras import ops
import tensorflow as tf
from PIL import Image
import numpy as np




LABEL2NAME = {0: 'BrassMono-BoldItalic',
 1: 'GhastlyPanicCyr',
 2: 'ambidexter_regular',
 3: 'GaneshaType-Regular',
 4: 'AlumniSansCollegiateOne-Italic',
 5: 'AlumniSansCollegiateOne-Regular',
 6: 'BrassMono-Italic',
 7: 'better-vcr-5.2',
 8: 'ArefRuqaaInk-Bold',
 9: 'Aguante-Regular',
 10: 'BrassMono-Bold',
 11: 'ArefRuqaaInk-Regular',
 12: 'Realest-Extended',
 13: 'BrassMono-Regular',
 14: 'TanaUncialSP'}

def check_model_path(path):
    if not path.endswith('.keras'):
        print("Путь к модели должен оканчиваться на .keras")
        return False
    return True

def check_image_path(path):
    if not any(path.endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
        print("Путь к изображению должен оканчиваться на .jpg, .jpeg или .png")
        return False
    return True

def prepare_image(img_array, target_size=(128, 256)):
    if len(img_array.shape) == 2:
        color_mode = 'grayscale'
    elif len(img_array.shape) == 3:
        color_mode = 'rgb'
    else:
        print("Неверный формат изображения")
        return None
    if color_mode == 'grayscale':
        img_array = np.tile(img_array[:, :, np.newaxis], (1, 1, 3))
    new_img = img_array.astype('float32') / 255.0
    return new_img

def main():
    if len(sys.argv) > 1:
        model_path = str(sys.argv[1])
        if check_model_path(model_path):
            print("Путь к модели", model_path)
            try:
                model = keras.saving.load_model(model_path, custom_objects=None, compile=True, safe_mode=True)
            except Exception as e:
                print('загрузка модели не удалась')
                print(e)
                exit()
        else:
            print("Путь к модели не найден, пожалуйста попробуйте еще раз")
            exit()
    else:
        print("Путь к модели не найден, пожалуйста попробуйте еще раз")
        exit()

    while True:
        image_path = input("Введите путь до изображения (или 'q' для выхода): ")
        if image_path.lower() == 'q':
            break
        if check_image_path(image_path):
            try:
                img = Image.open(image_path)
                img_array = np.array(img)
                print("Image was loaded")
                img_array = prepare_image(img_array)
                img_batch = np.expand_dims(img_array, axis=0)
                predict = model.predict(img_batch)
                print(LABEL2NAME[np.argmax(predict, axis=1)[0]], predict[0][np.argmax(predict, axis=1)[0]])
            except Exception as e:
                print(e)
                print('Try more')

if __name__ == "__main__":
    main()
