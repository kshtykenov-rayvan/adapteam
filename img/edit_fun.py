from PIL import Image, ImageEnhance


# Функция для обработки изображения
def process_image(input_path, output_path, brightness_factor=0.5, contrast_factor=3, exposure_steps=1):
    # Открываем изображение
    image = Image.open(input_path)

    # Увеличиваем яркость
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)  # Коэффициент яркости (1.0 - оригинал)

    # Увеличиваем четкость
    sharpness_enhancer = ImageEnhance.Sharpness(image)
    image = sharpness_enhancer.enhance(2.0)  # Коэффициент увеличения четкости

    # Преобразуем изображение в черно-белое
    image = image.convert("L")

    # Увеличиваем контраст
    contrast_enhancer = ImageEnhance.Contrast(image)
    image = contrast_enhancer.enhance(contrast_factor)  # Коэффициент увеличения контраста

    # Увеличиваем экспозицию
    # Экспозиция может быть реализована через изменение значения пикселей
    if exposure_steps > 0:
        image = image.point(lambda p: min(p * (2 ** exposure_steps), 255))

    # Сохраняем обработанное изображение
    image.save(output_path)


# Пример использования функции
input_image_path = 'original/0001.jpg'  # путь к исходному изображению
output_image_path = 'edit/0001.jpg'  # путь для сохранения обработанного изображения

# Пример параметров
brightness_factor = 0.5  # Яркость +20%
contrast_factor = 3  # Контраст +25%
exposure_steps = 1  # Экспозиция +1 ступень

process_image(input_image_path, output_image_path, brightness_factor, contrast_factor, exposure_steps)
