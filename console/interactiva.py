from core.parser import evaluar_expresion
from core.historial import Historial

def consola_interactiva():
    historial = Historial()
    print("🔎 Consola Interactiva estilo Wolfram Alpha")
    print("Comandos: 'salir', 'historial', 'guardar', 'exportar'\n")

    while True:
        entrada = input("» ")
        if entrada.lower() == "salir":
            break
        if entrada.lower() == "historial":
            historial.mostrar()
            continue
        if entrada.lower() == "guardar":
            historial.guardar_txt()
            print("✅ Guardado como historial.txt")
            continue
        if entrada.lower() == "exportar":
            historial.exportar_json()
            print("✅ Exportado como historial.json")
            continue

        try:
            resultado = evaluar_expresion(entrada)
            historial.agregar(entrada, resultado)
            print("= ", resultado)
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    consola_interactiva()
# This code is a simple interactive console for evaluating mathematical expressions.
# It allows users to input expressions, view a history of inputs and outputs, and save or export that history. 