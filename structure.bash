calculadora_cientifica/
├── main.py                     # Lanza la app desde consola
├── gui/
│   └── pyqt_gui.py             # Interfaz gráfica con PyQt5
├── console/
│   └── interactiva.py          # Consola estilo Wolfram Alpha
├── core/
│   ├── parser.py               # Evalúa expresiones matemáticas
│   ├── funciones.py            # Funciones personalizadas
│   ├── constantes.py           # Constantes científicas
│   ├── simbolico.py            # Derivadas e integrales (SymPy)
│   └── historial.py            # Historial con guardado/exportación
├── data/
│   ├── historial.txt           # Historial exportado como texto
│   └── historial.json          # Historial exportado como JSON
├── structure.bash              # Estructura del proyecto
├── launcher/                   # Lanzador de la app desde windows, linux y mac
│   ├── InciciarCalculadora.bat  # Lanzador de la app desde windows
│   ├── IniciarCalculadora.sh    # Lanzador de la app desde linux/mac
│   └── Instalar.sh             # Lanzador del script de permisos para linux/mac
├── tests/                      # Pruebas unitarias
│   ├── test_parser.py          # Pruebas del parser
│   ├── test_funciones.py       # Pruebas de funciones personalizadas
│   ├── test_constantes.py      # Pruebas de constantes científicas
│   ├── test_simbolico.py       # Pruebas de derivadas e integrales
│   └── test_historial.py       # Pruebas del historial
├── README.md                   # Documentación del proyecto
└── requirements.txt            # Dependencias del proyecto
