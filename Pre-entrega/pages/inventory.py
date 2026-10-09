from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage():
    def __init__(self, driver):
        self.driver = driver

    def obtener_productos(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")

    def obtner_nombre_primer_producto(self):
        producto = self.obtener_productos()
        return producto[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    
    def obtner_valor_primer_producto(self):
            producto = self.obtener_productos()
            return producto[0].find_element(By.CLASS_NAME, "inventory_item_price").text

#Tuve que cambiar a is_enable, la IA me decía que como esta transparente el botón no lo reconocía el método is_displayed
    def menu_visible(self):
        menu = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))
        )
        return menu.is_enabled()

    def filtro_visible(self):
        filtro = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
        )
        return filtro.is_enabled()

    def obtener_titulo_seccion(self):
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".title"))
            ).text