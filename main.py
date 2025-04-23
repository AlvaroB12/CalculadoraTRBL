import sys

def mostrar_menu():
    print("""
🚀 CALCULADORA CIENTÍFICA AVANZADA
Selecciona un modo:

1. Consola interactiva estilo Wolfram Alpha
2. Interfaz gráfica PyQt5
3. Salir
""")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1/2/3): ")

        if opcion == "1":
            from console.interactiva import consola_interactiva
            consola_interactiva()
        elif opcion == "2":
            try:
                from gui.pyqt_gui import CalculadoraGUI
                from PyQt5.QtWidgets import QApplication
                app = QApplication(sys.argv)
                ventana = CalculadoraGUI()
                ventana.show()
                sys.exit(app.exec_())
            except ImportError:
                print("❌ PyQt5 no está instalado. Instálalo con: pip install pyqt5")
        elif opcion == "3":
            print("👋 Cerrando calculadora.")
            break
        else:
            print("❌ Opción no válida. Elige 1, 2 o 3.")

if __name__ == "__main__":
    main()
 