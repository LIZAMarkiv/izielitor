from PIL import Image, ImageFilter

with Image.open('img.png')as pic_original:
    pic_original = pic_original.filter(ImageFilter.CONTOUR)
    pic_original.save('contur.png')
    pic_original.show()
