from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_get_to_home_page(self):
        # Jonh heard about a new blog site. He goes to check out its homepage.
        self.browser.get(self.live_server_url)
        # He notices the page's title says Welcome and the Header Welcome to PyDev
        self.assertIn('Welcome', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Hi, welcome to', header_text)

        self.fail('Finish the test!')
    
    def test_can_get_to_blogs_section(self):
        # then he see a link in the nav to Blogs and click on it. he is redirect to the blogs section
        browser = self.browser
        browser.get(self.live_server_url)

        link = browser.find_element_by_partial_link_text('Blogs')
        link.click()
        time.sleep(1)

        self.assertIn('Blogs', self.browser.title)

        # Here he notice that there is one Blog called PyDev 1.0 and click Read More
        blog_title = browser.find_element_by_css_selector('.title').text
        self.assertIn('Blogs', blog_title)
        # He is redirect to a different page that show more about the blog and all its entries
        # He goes to one entry called Testing PyDev 1.0 and get redirect to that page
        # He read the entry and at the bottom see a bottom called edit entry click on it
        # The he got a 404 error that says he has no right to change this entry. Goes back to the entry and then goes
        # to lastest. Here all the lastest entries on the site are listed.
        # after that hit login,  because he has not account he then click on singin and fill the form
        # Now that he is a registered user he can create his own blog and start adding entries.
        # after trying all that he logout and close the tap.

if __name__ == '__main__':
    unittest.main()
