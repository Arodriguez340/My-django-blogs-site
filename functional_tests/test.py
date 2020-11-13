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
    
    def test_can_get_to_blogs_section(self):
        # then he see a link in the nav to Blogs and click on it. he is redirect to the blogs section
        browser = self.browser
        browser.get(self.live_server_url)

        link = browser.find_element_by_partial_link_text('Blogs')
        link.click()
        time.sleep(2)

        self.assertIn('Blogs', browser.title)
        blog_title = browser.find_element_by_css_selector('.title').text
        self.assertIn('Blogs', blog_title)
        # Here he notice that there is a message that says no blogs have been added.
        # below he see a buttom that say add new blog and click on it.
        add_link = browser.find_element_by_link_text('Add a new blog')
        add_link.click()
        time.sleep(2)
        # then he is redirect to a signin page 
        signin_promt = browser.find_elements_by_tag_name('h1')
        self.assertIn('Signin', browser.title)
        self.assertIn('Singin', [j.text for j in signin_promt])
        # He create an account and now he happyly create his new blog.
        username_place_holder = browser.find_element_by_css_selector('#id_username')
        password1_place_holder = browser.find_element_by_css_selector('#id_password1')
        password2_place_holder = browser.find_element_by_css_selector('#id_password2')

        username_place_holder.send_keys('cool_user01')
        password1_place_holder.send_keys('12345')
        password2_place_holder.send_keys('12345')

        submit_button = browser.find_element_by_css_selector('#submit-button')
        submit_button.click()
        time.sleep(2)
        # now he goes back to the blogs section and try to create his new blog
        link = browser.find_element_by_partial_link_text('Blogs')
        link.click()
        time.sleep(1)
        add_link = browser.find_element_by_link_text('Add a new blog')
        add_link.click()
        time.sleep(1)



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
