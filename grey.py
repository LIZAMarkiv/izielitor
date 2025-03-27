from PIL import Image
with Image.open('img.png')as pic_original:
    pic_grey = pic_original.convert('L')
    pic_grey.save('grey.png')
    pic_grey.show()