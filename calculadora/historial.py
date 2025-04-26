import json

class Historial:
    def __init__(self):
        self.items = []

    def agregar(self, expresion, resultado):
        self.items.append((expresion, str(resultado)))

    def mostrar(self):
        print("\n🧾 Historial:")
        if not self.items:
            print("No hay cálculos aún.")
        for i, (exp, res) in enumerate(self.items, 1):
            print(f"{i}. {exp} = {res}")
        print()

    def guardar_txt(self, nombre_archivo="historial.txt"):
        with open(nombre_archivo, 'w') as f:
            for exp, res in self.items:
                f.write(f"{exp} = {res}\n")

    def exportar_json(self, nombre_archivo="historial.json"):
        with open(nombre_archivo, 'w') as f:
            json.dump(self.items, f, indent=4)
