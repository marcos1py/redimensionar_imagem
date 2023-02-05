import sys
from novo.ESSE import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.botao_de_escolher_arquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimencionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            "abrir imagem",
            "\marco\Pictures",
            #options = QFileDialog.DontUseNativeDialog #isso e para quem ta dano problema com a aba do proprio windons
        )
        self.input_arquivo.setText(image)
        self.original_img= QPixmap(image)
        self.labelimg.setPixmap(self.original_img)
        self.inpuLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.inpuLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelimg.setPixmap(self.nova_imagem)
        self.inpuLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            "Salvar imagem",
            "\marco\Pictures",
        )
        self.nova_imagem.save(imagem, ".PNG")

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()