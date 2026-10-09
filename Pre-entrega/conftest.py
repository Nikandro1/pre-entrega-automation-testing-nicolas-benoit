import logging

import pytest
from selenium import webdriver

from utils.helpers import tomar_captura

logger = logging.getLogger(__name__)


@pytest.fixture
def driver(request):
    logger.info("Iniciando navegador")
    driver = webdriver.Chrome()
    driver.maximize_window()
    fallos_antes = request.session.testsfailed

    yield driver

    if request.session.testsfailed > fallos_antes:
        ruta = tomar_captura(driver, request.node.name)
        logger.error("Test fallido: %s | captura: %s", request.node.name, ruta)

    logger.info("Cerrando navegador")
    driver.quit()