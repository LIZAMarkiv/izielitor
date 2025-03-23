from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import*
app = QApplication([])
window = QWidget()

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
knopka1 = QPushButton("Папка")
list = QListWidget()
der = QPixmap("img.png")
der = der.scaledToWidth(300)
kart = QLabel("ggg")
kart.setPixmap(der)
knopka2 = QPushButton("Вліво")
knopka3 = QPushButton("Вправо")
knopka4  = QPushButton("Дзеркало")
knopka5 = QPushButton("Різкізть")
knopka6 = QPushButton("Ч/Б")




v1.addWidget(knopka1)
v1.addWidget(list)
v2.addWidget(kart)
h1.addWidget(knopka2)
h1.addWidget(knopka3)
h1.addWidget(knopka4)
h1.addWidget(knopka5)
h1.addWidget(knopka6)
v2.addLayout(h1)
main_lain.addLayout(v1)
main_lain.addLayout(v2)



window.setLayout(main_lain)
window.show()
app.exec()