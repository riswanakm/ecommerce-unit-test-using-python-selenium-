import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ContactFormTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://live-wellstore.pantheonsite.io/contact/')
        
    def test_contact_form_submission(self):
        name_input = self.driver.find_element_by_name('your-name')
        email_input = self.driver.find_element_by_name('your-email')
        subject_input = self.driver.find_element_by_name('your-subject')
        message_input = self.driver.find_element_by_name('your-message')
        submit_button = self.driver.find_element_by_css_selector('input[type="submit"]')
        
        name_input.send_keys('John Doe')
        email_input.send_keys('johndoe@example.com')
        subject_input.send_keys('Test Message')
        message_input.send_keys('This is a test message.')
        submit_button.click()
        
        success_message = self.driver.find_element_by_css_selector('.wpcf7-response-output')
        self.assertEqual(success_message.text, 'Thank you for your message. It has been sent.')
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
unittest.main()
