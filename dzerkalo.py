from PIL import Image
with Image.open('img.png') as pic_original:
    pic_original = pic_original.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    pic_original.save('color.png')
    pic_original.show()