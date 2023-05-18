from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

class Obliterar:
    def __init__(self):
        self.site = "https://www.youtube.com/watch?v=ABH8oZ2UmLo"
        self.driver = webdriver.Chrome()
        self.driver.get(self.site)
        sleep(50)
        self.driver.close()

