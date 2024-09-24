from PIL import Image
import pytesseract

# Загрузите изображение
image = Image.open('0002.jpg',)

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Распознавание текста
text = pytesseract.image_to_string(image)

# Вывод результата
print(text)
