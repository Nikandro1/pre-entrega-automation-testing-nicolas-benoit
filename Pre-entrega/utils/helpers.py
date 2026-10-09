import os
from datetime import datetime

CARPETA_CAPTURAS = os.path.join("reports", "screenshots")


def tomar_captura(driver, nombre_test):
    """Guarda una captura en reports/screenshots y devuelve la ruta."""
    os.makedirs(CARPETA_CAPTURAS, exist_ok=True)
    nombre_limpio = "".join(c if c.isalnum() or c in "-_" else "_" for c in nombre_test)
    marca = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = os.path.join(CARPETA_CAPTURAS, f"{nombre_limpio}_{marca}.png")
    driver.save_screenshot(ruta)
    return ruta