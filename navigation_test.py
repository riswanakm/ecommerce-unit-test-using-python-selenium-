
import unittest
from selenium import webdriver

class NavigationMenuTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://live-wellstore.pantheonsite.io/')
        
    def test_menu_home(self):
        menu_home = self.driver.find_element_by_link_text('Home')
        menu_home.click()
        self.assertEqual(self.driver.current_url, 'https://live-wellstore.pantheonsite.io/')
        
    def test_menu_products(self):
        menu_products = self.driver.find_element_by_link_text('Products')
        menu_products.click()
        self.assertEqual(self.driver.current_url, 'https://live-wellstore.pantheonsite.io/products/')
        
    def test_menu_about(self):
        menu_about = self.driver.find_element_by_link_text('About')
        menu_about.click()
        self.assertEqual(self.driver.current_url, 'https://live-wellstore.pantheonsite.io/about/')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
