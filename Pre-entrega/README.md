# Pre-entrega Automation Testing - SauceDemo

Proyecto de automatización de pruebas funcionales sobre [SauceDemo](https://www.saucedemo.com/), una tienda online de práctica. Los casos de prueba están escritos con Selenium y Pytest.

**Autor:** Nicolás Benoit ([@Nikandro1](https://github.com/Nikandro1))

## Propósito del proyecto

Automatizar y validar los flujos principales del sitio:

- **Login:** ingreso con credenciales válidas y redirección al inventario.
- **Navegación y catálogo:** título de la página, presencia de productos, datos del primer producto y elementos de la interfaz (menú y filtros).
- **Carrito:** agregar un producto, verificar el contador y comprobar que el producto aparece en el carrito.

Cada validación es específica para su paso y los tests son **independientes entre sí**: cada uno abre su propio navegador, hace su propio login y no comparte estado con los demás, por lo que la falla de uno no afecta al resto.

## Tecnologías utilizadas

| Herramienta | Uso |
|---|---|
| Python 3 | Lenguaje del proyecto |
| Selenium WebDriver | Automatización del navegador |
| Pytest | Framework de ejecución de tests |
| pytest-html | Generación del reporte HTML |
| Google Chrome | Navegador de las pruebas |

## Estructura del proyecto

```
pre-entrega-automation-testing-nicolas-benoit/
├── conftest.py            # fixture del driver y captura de pantalla en fallos
├── pytest.ini             # configuración de pytest (reporte HTML y logs)
├── requirements.txt       # dependencias
├── README.md
├── pages/                 # Page Objects
│   ├── login.py
│   ├── inventory.py
│   └── carrito.py
├── tests/                 # casos de prueba
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_carrito.py
├── utils/                 # funciones y constantes auxiliares
│   ├── __init__.py
│   └── helpers.py
└── reports/               # evidencias de la ejecución
    ├── reporte.html
    ├── ejecucion.log
```

## Instalación de dependencias

**Requisitos previos:** Python 3 y Google Chrome instalados.

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Nikandro1/pre-entrega-automation-testing-nicolas-benoit.git
   cd pre-entrega-automation-testing-nicolas-benoit
   ```


2. Instalar las dependencias:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Ejecución de las pruebas

Todas las pruebas, generando el reporte HTML y los logs:

```bash
python -m pytest
```

El archivo `pytest.ini` ya incluye las opciones necesarias. El comando equivalente, escrito completo, es:

```bash
python -m pytest -v --html=reports/reporte.html --self-contained-html
```

Otras formas de ejecutar:

```bash
# Un archivo puntual
python -m pytest tests/test_carrito.py

# Un test puntual
python -m pytest tests/test_carrito.py::test_verificar_item_en_carrito

# Mostrar los print() en consola
python -m pytest -s
```

## Casos de prueba

| Archivo | Test | Qué valida |
|---|---|---|
| `test_login.py` | `test_login_exitoso` | Login con `standard_user`, redirección a `/inventory.html`, título `Swag Labs` y encabezado `Products` |
| `test_inventory.py` | `test_inventory` | Título de la página, productos visibles, nombre y precio del primer producto, menú y filtro presentes |
| `test_carrito.py` | `test_agregar_producto_al_carrito` | Al agregar el primer producto, el contador del carrito muestra `1` |
| `test_carrito.py` | `test_verificar_item_en_carrito` | El producto agregado aparece en el carrito con el mismo nombre |

Los tests usan esperas explícitas (`WebDriverWait`) y no dependen del orden de ejecución.

## Evidencias

Después de cada ejecución se generan en la carpeta `reports/`:

- **`reporte.html`:** reporte de Pytest con el resultado de cada test. Se puede abrir directamente en el navegador.
- **`ejecucion.log`:** registro paso a paso de la ejecución.
- **`screenshots/`:** capturas de pantalla automáticas cuando un test falla. La carpeta solo aparece si hubo algún fallo.

## Estructura de un test

Cada test sigue el mismo orden: se instancian las páginas, se navega al sitio, se ejecuta el flujo con los métodos de las clases y se validan los resultados con `assert`. La lógica de interacción con la página vive en `pages/`, y los tests solo orquestan y validan.
