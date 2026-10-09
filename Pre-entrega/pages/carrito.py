from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CarritoPage:
    def __init__(self, driver):
        self.driver = driver

    def agregar_al_carrito(self):
        producto = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_item"))
        )
        nombre = producto.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        producto.find_element(By.TAG_NAME, "button").click()
        return nombre

    def obtener_contador(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
        ).text

    def ir_al_carrito(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

    def verificar_item_en_carrito(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
            )
        ).text