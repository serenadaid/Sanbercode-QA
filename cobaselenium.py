import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)


    def test_b_failed_login_wrong_username(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("STANDARD_USER") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

    
    def test_c_success_add_to_cart(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
        time.sleep(1)
        driver.find_element(By.ID, "shopping_cart_container").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('YOUR CART', response_data)

    def tearDown(self):
        self.browser.close()

"""class TestCart(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_c_success_add_to_cart(self):
        # steps
        driver = self.browser #buka web browser
        test_a_success_login(self)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
        time.sleep(1)
        driver.find_element(By.ID, "shopping_cart_container").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('YOUR CART', response_data)
        time.sleep(3)
    
    def tearDown(self):
        self.browser.close()"""


if __name__ == "__main__":
    unittest.main()