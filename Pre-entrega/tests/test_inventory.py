from pages.login import LoginPage
from pages.inventory import InventoryPage

def test_inventory(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    
    driver.get("https://www.saucedemo.com/")
    login.login("standard_user","secret_sauce")

    assert driver.title == "Swag Labs"
    assert inventory.obtener_titulo_seccion() == "Products"

    productos = inventory.obtener_productos()
    assert len(productos) > 0

    nombre = inventory.obtner_nombre_primer_producto()
    assert nombre == "Sauce Labs Backpack"

    precio = inventory.obtner_valor_primer_producto()
    assert precio == "$29.99"

    assert inventory.menu_visible()
    assert inventory.filtro_visible()
