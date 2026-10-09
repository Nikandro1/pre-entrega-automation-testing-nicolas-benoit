from pages.login import LoginPage
from pages.carrito import CarritoPage


def test_agregar_producto_al_carrito(driver):
    login = LoginPage(driver)
    carrito = CarritoPage(driver)

    driver.get("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")

    carrito.agregar_al_carrito()
    contador = carrito.obtener_contador()

    assert contador == "1"


def test_verificar_item_en_carrito(driver):
    login = LoginPage(driver)
    carrito = CarritoPage(driver)

    driver.get("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")

    nombre_agregado = carrito.agregar_al_carrito()
    carrito.ir_al_carrito()
    nombre_en_carrito = carrito.verificar_item_en_carrito()

    assert nombre_en_carrito == nombre_agregado