
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ProductSearchTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://live-wellstore.pantheonsite.io/")

    def test_product_search(self):
        # Find the search bar element and enter the search term
        search_input = self.driver.find_element_by_id("woocommerce-product-search-field-0")
        search_input.send_keys("protein powder")

        # Press the enter key to submit the search
        search_input.send_keys(Keys.RETURN)

        # Wait for the search results to load
        self.driver.implicitly_wait(5)

        # Check if the search results contain the expected product
        results = self.driver.find_elements_by_class_name("product")
        self.assertGreater(len(results), 0)
        self.assertIn("Protein Powder", results[0].text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
