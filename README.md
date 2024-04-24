Реализация whatsthefont

notebooks/data_generation.ipynb - ноутбук для генерации данных, не успел сделать рефакторинг генерации данных для train
notebooks/kvant-train-classifer-efficientnet_1st.ipynb - тетрадка обучения 1 модели, тренировочные данные из dataset_1st_train (128x128px)
notebooks/kvant-train-classifer-efficientnet_2nd.ipynb - тетрадка обучения на основе весов 1 модели, тренировочные данные из dataset (128x256) расширил кол-во кеглей используемых шрифтов, для генерации текста использовал первый том Гарри Поттера
notebooks/infern.ipynb - тестирование модели на тестовом наборе данных test_dataset, 128x256 c генерированы на Harry Potter and the Chamber of Secrets


train_1st - модель из первой тетрадки, плюс логи обучения и графики
train_2nd - модель из второй тетрадки, плюс логи обучения и графики
Обучение проводил на tesla t4.

main.py - скрипт при запуске, требует path  в качестве второго аргумента. Далее запрашивает путь к изображению.

python main.py train_2nd/best_model.keras
