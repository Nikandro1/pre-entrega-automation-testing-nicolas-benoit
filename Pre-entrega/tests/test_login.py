from pages.login import LoginPage
from pages.inventory import InventoryPage

def test_login_exitoso(driver):
    #Instancia de login
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    #Conectarme a la pag
    driver.get("https://www.saucedemo.com/")

    #Ingresar los datos con funcion de la clase
    login.login("standard_user", "secret_sauce")

    #Validar que esta en la pagina
    assert "/inventory.html" in driver.current_url
    assert driver.title == "Swag Labs"
    assert inventory.obtener_titulo_seccion() == "Products"

