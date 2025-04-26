from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton
from calculadora.parser import evaluar_expresion
from calculadora.historial import Historial
import sys

class CalculadoraGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Científica PyQt5")
        self.setGeometry(100, 100, 500, 400)
        self.historial = Historial()

        self.layout = QVBoxLayout()
        self.entrada = QLineEdit()
        self.salida = QTextEdit()
        self.boton = QPushButton("Calcular")
        self.boton.clicked.connect(self.calcular)

        self.layout.addWidget(self.entrada)
        self.layout.addWidget(self.boton)
        self.layout.addWidget(self.salida)
        self.setLayout(self.layout)

    def calcular(self):
        expr = self.entrada.text()
        try:
            resultado = evaluar_expresion(expr)
            self.historial.agregar(expr, resultado)
            self.salida.append(f"> {expr}\n= {resultado}\n")
        except Exception as e:
            self.salida.append(f"> {expr}\n❌ Error: {e}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CalculadoraGUI()
    ventana.show()
    sys.exit(app.exec_())
