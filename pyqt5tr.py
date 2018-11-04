import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv) # uygulama oluşturuyoruz.

def yalin_pencere():
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Yalın Pencere Oluşturma")
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
    
#yalin_pencere()
    
def yazi_ekleme():
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Yazi Ekleme")
    pencere.setGeometry(100,100,500,500)
    
    yazi = QtWidgets.QLabel(pencere)
    yazi.setText("Yukarıdaki Kod Label Oluşturup Pencereye Sabitlemek İçin Yazılıyor.")
    
    pencere.show()
    sys.exit(app.exec_()) #pencereyi gösterip döngüye alma işlemlerini sona bırak
    
#yazi_ekleme()
  
  
def buton_ekleme():
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Sa")
    pencere.setGeometry(100,100,500,500)
    
    buton = QtWidgets.QPushButton(pencere)
    buton.setGeometry(100,100,100,100)
    buton.setText("Bas Bana")
    
    pencere.show()
    sys.exit(app.exec_())
    
#buton_ekleme()


def yatay_kutu():
    pencere = QtWidgets.QWidget()
    pencere.setGeometry(100,100,500,500)
    pencere.setWindowTitle("Yatay Kutu")
    h_box = QtWidgets.QHBoxLayout(pencere) # horizontal kutu oluşturuyoruz
    
    yazi = QtWidgets.QLabel()
    yazi.setText("Bas Ona")
    
    
    buton = QtWidgets.QPushButton()
    buton.setText("BAS BANA")
    
    h_box.addWidget(yazi)
    h_box.addWidget(buton)
     
    pencere.setLayout(h_box)
    
    pencere.show()
    sys.exit(app.exec_())
    
#yatay_kutu()
    
def dikey_kutu():
    pencere = QtWidgets.QWidget()
    pencere.setGeometry(100,100,500,500)
    
    buton = QtWidgets.QPushButton()
    yazi = QtWidgets.QLabel()
    
    buton.setText("Bas Bana")
    yazi.setText("Bas Ona")
    
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(yazi)
    v_box.addWidget(buton)
    pencere.setLayout(v_box)
    
    pencere.show()
    sys.exit(app.exec_())
    
#dikey_kutu()

def dikey_yatay_icice():
    pencere = QtWidgets.QWidget()
    butong = QtWidgets.QPushButton()
    butonr = QtWidgets.QPushButton()
    
    butong.setText("Onayla")
    butonr.setText("Reddet")
    
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(butong)
    h_box.addWidget(butonr)
    
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    
    pencere.setLayout(v_box) # Burada addWidget değil addLayout methodunu kullanıyoruz!
    
    pencere.show()
    sys.exit(app.exec_())
    
#dikey_yatay_icice()

