import os

from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import*
from PIL import Image, ImageFilter, ImageEnhance

app = QApplication([])
window = QWidget()

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap




app.setStyleSheet("""
   QWidget {
            background: #FFB6C1;
            color: #FFFFF0;
            font-family: Arial;
            font-size: 17px;
        }
        
        QLabel {
            font-weight: bold;
        }
        
        QPushButton {
            background-color: #FFB6C1;
            color: white;
            border-radius: 10px;
            padding: 17px;
    """)



main_lain = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
knopka1 = QPushButton("Папка")
photo_list = QListWidget()
der = QPixmap("img.png")
der = der.scaledToWidth(300)
kart = QLabel("ggg")
kart.setPixmap(der)
knopka2 = QPushButton("Вліво")
knopka3 = QPushButton("Вправо")
knopka4  = QPushButton("Дзеркало")
knopka5 = QPushButton("Різкізть")
knopka6 = QPushButton("Ч/Б")
knopka7 = QPushButton("Деталі")
knopka8 = QPushButton("Нерізкість")
knopka9 = QPushButton("Розмивання")
knopka10 = QPushButton("Тиснення")
knopka11 = QPushButton("Згладжування")
knopka12 = QPushButton("Насиченість")
knopka13 = QPushButton("Контур")
knopka14 = QPushButton("Контрастність")


v1.addWidget(knopka1)
v1.addWidget(photo_list)
v2.addWidget(kart)
h1.addWidget(knopka2)
h1.addWidget(knopka3)
h1.addWidget(knopka4)
h1.addWidget(knopka5)
h1.addWidget(knopka6)
h2.addWidget(knopka7)
h2.addWidget(knopka8)
h2.addWidget(knopka9)
h2.addWidget(knopka10)
h2.addWidget(knopka11)
h3.addWidget(knopka12)
h3.addWidget(knopka13)
h3.addWidget(knopka14)
v2.addLayout(h1)
v2.addLayout(h2)
v2.addLayout(h3)
main_lain.addLayout(v1)
main_lain.addLayout(v2)


class ImageProcessor:
    def __init__(self):
        self.folder = ""
        self.filename = ""
        self.image = ""

    def load(self):
        img_path = os.path.join(self.folder, self.filename)
        self.image = Image.open(img_path)
    def show(self):
        pix = pil2pixmap(self.image)
        pix = pix.scaledToWidth(300)
        kart.setPixmap(pix)

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.show()

    def dzerkalo(self):
        self.image = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.show()

    def rizkist(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.show()

    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.show()

    def black_white(self):
        self.image = self.image.convert("L")
        self.show()
    def detal(self):
        self.image = self.image.filter(ImageFilter.DETAIL  )
        self.show()

    def dn_rizkist(self):
        self.image = self.image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
        self.show()

    def blurring(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.show()

    def tusnenia(self):
        self.image = self.image.filter(ImageFilter.EMBOSS )
        self.show()

    def zgladg(self):
        self.image = self.image.filter(ImageFilter.SMOOTH   )
        self.show()

    def more_color(self):
        self.image = ImageEnhance.Color(self.image).enhance(1.5)
        self.show()

    def contur(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.show()

    def kontrast(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(1.5)
        self.show()


ip = ImageProcessor()
ip.filename = "color.png"
ip.load()
ip.show()

def open_folder():
    ip.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(ip.folder)
    photo_list.clear()
    for file in files:
        if file.endswith(".jpg"):
            photo_list.addItem(file)




knopka14.clicked.connect(ip.kontrast)
knopka13.clicked.connect(ip.contur)
knopka12.clicked.connect(ip.more_color)
knopka11.clicked.connect(ip.zgladg)
knopka10.clicked.connect(ip.tusnenia)
knopka9.clicked.connect(ip.blurring)
knopka8.clicked.connect(ip.dn_rizkist)
knopka7.clicked.connect(ip.detal)
knopka6.clicked.connect(ip.black_white)
knopka3.clicked.connect(ip.rotate_right)
knopka5.clicked.connect(ip.rizkist)
knopka4.clicked.connect(ip.dzerkalo)
knopka2.clicked.connect(ip.rotate_left)
knopka1.clicked.connect(open_folder)

def show_chosen_image():
    ip.filename = photo_list.currentItem().text()
    ip.load()
    ip.show()

photo_list.currentRowChanged.connect(show_chosen_image)
window.setLayout(main_lain)
window.show()
app.exec()