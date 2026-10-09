from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def ingresar_usuario(self, usuario="standar_user"):
        self.driver.find_element(By.ID, "user-name").send_keys(usuario)

    def ingresar_contrasena(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def hacer_click_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    def login(self, usuario, password):
        self.ingresar_usuario(usuario)
        self.ingresar_contrasena(password)
        self.hacer_click_login()
