from PIL import Image
with Image.open('img.png') as pic_original:
    print('Зображення відкрито')
    print('Розмір:', pic_original.size)
    print('Формат:', pic_original.mode)
    pic_original.show()