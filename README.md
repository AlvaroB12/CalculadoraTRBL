# Calculadora Científica TRBL

🚀 **Calculadora Científica TRBL** es una aplicación que permite realizar cálculos matemáticos complejos, incluyendo derivadas, integrales, y conversiones entre grados y radianes. Ofrece tanto una consola interactiva como una interfaz gráfica basada en PyQt5.

## Características

- **Consola interactiva** estilo Wolfram Alpha.
- **Interfaz gráfica** con PyQt5.
- **Evaluación de expresiones matemáticas** con soporte para funciones personalizadas.
- **Historial de cálculos** con opciones para guardar y exportar.
- **Soporte para derivadas e integrales** usando SymPy.
- **Constantes científicas** predefinidas.


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