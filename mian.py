from PIL import Image, ImageEnhance
import numpy as np


# Функция для обработки изображения
def process_image(input_path, output_path):
    # Открываем изображение
    image = Image.open(input_path)

    # Увеличиваем четкость
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(2.0)  # 2.0 - коэффициент увеличения четкости

    # Преобразуем изображение в черно-белое
    image = image.convert("L")

    # Увеличиваем контраст
    contrast_enhancer = ImageEnhance.Contrast(image)
    image = contrast_enhancer.enhance(1.5)  # 1.5 - коэффициент увеличения контраста

    # Сохраняем обработанное изображение
    image.save(output_path)


# Пример использования функции
input_image_path = '0002.jpg'  # путь к исходному изображению
output_image_path = 'output.jpg'  # путь для сохранения обработанного изображения
process_image(input_image_path, output_image_path)
