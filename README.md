# Calculadora Científica Avanzada

🚀 **Calculadora Científica Avanzada** es una aplicación que permite realizar cálculos matemáticos complejos, incluyendo derivadas, integrales, y conversiones entre grados y radianes. Ofrece tanto una consola interactiva como una interfaz gráfica basada en PyQt5.

## Características

- **Consola interactiva** estilo Wolfram Alpha.
- **Interfaz gráfica** con PyQt5.
- **Evaluación de expresiones matemáticas** con soporte para funciones personalizadas.
- **Historial de cálculos** con opciones para guardar y exportar.
- **Soporte para derivadas e integrales** usando SymPy.
- **Constantes científicas** predefinidas.

## Estructura del Proyecto

```bash
calculadora_cientifica/
├── [main.py](http://_vscodecontentref_/1)                     # Lanza la app desde consola
├── gui/
│   └── pyqt_gui.py             # Interfaz gráfica con PyQt5
├── console/
│   └── interactiva.py          # Consola estilo Wolfram Alpha
├── core/
│   ├── parser.py               # Evalúa expresiones matemáticas
│   ├── funciones.py            # Funciones personalizadas
│   ├── constantes_maths.py     # Constantes científicas
│   ├── simbolico.py            # Derivadas e integrales (SymPy)
│   └── historial.py            # Historial con guardado/exportación
├── data/
│   ├── historial.txt           # Historial exportado como texto
│   └── historial.json          # Historial exportado como JSON
├── launcher/                   # Lanzadores para Windows, Linux y Mac
│   ├── IniciarCalculadora.bat  # Lanzador para Windows
│   ├── IniciarCalculadora.sh   # Lanzador para Linux/Mac
│   └── Instalar.sh             # Script para permisos en Linux/Mac
├── tests/                      # Pruebas unitarias
│   ├── test_parser.py          # Pruebas del parser
│   ├── test_funciones.py       # Pruebas de funciones personalizadas
│   ├── test_constantes_maths.py # Pruebas de constantes científicas
│   ├── test_simbolico.py       # Pruebas de derivadas e integrales
│   └── test_historial.py       # Pruebas del historial
├── [README.md](http://_vscodecontentref_/2)                   # Documentación del proyecto
└── [requirements.txt](http://_vscodecontentref_/3)            # Dependencias del proyecto

```

## Instalacion

1. Clona este repositorio:

```bash
git clone https://github.com/usuario/calculadora_cientifica.git
cd calculadora_cientifica
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. **(Opcional)** En Linux/Mac, da permisos de ejecucion al lanzador:

```bash
bash launcher/Instalar
```

## Uso 

### Desde la Consola Interactiva:

Ejecuta el siguiente comando:

```bash
python [main.py] (http://vscodecontentref_/1)
```

Selecciona la opcion **1** para usar la consola interactiva.

### Desde la Interfaz Grafica:

Selecciona la opcion **2** en el menu principal o ejecuta directamente: 

```bash
python [pyqt_gui.py](http://_vscodecontentref_/2)
```

### Para Salir:

Selecciona la opcion 3 en el menu principal.


### Lanzadores:
 - **Windows:** Ejecuta  ```launcher/IniciarCalculadora.bat

 - **Linux/Mac:** Ejecuta ```launcher/IniciarCalculadora.sh

## Dependencias

- [SymPy](https://www.sympy.org/) - Biblioteca para matemáticas simbólicas.
- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) - Biblioteca para interfaces gráficas.
- [pytest](https://docs.pytest.org/) - Framework para pruebas unitarias.


## Pruebas

Ejecuta las pruebas unitarias con: 

```bash
pytest tests/

```

## Licencia

Este proyecto esta bajo la licencia [CC BY-ND 4.0](https://creativecommons.org/license/by-nd/4.0/) . 

Puedes usarlo y compartirlo libremente, siempre y cuando des credito y **no modifiques ni redistribuyas versiones alteradas del codigo**.

Consulta el archivo **LICENSE** para mas detalles.


## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envia un pull request.


## Creditos

Hecho con cariño por AlvaroB12 (TRBL)