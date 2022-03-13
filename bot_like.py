from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username,password
import time
import random
from selenium.common.exceptions import NoSuchFrameException

class InstagramBot():
    def __init__(self, username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome('chromedriver/chromedriver')

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def login(self):
        browser = self.browser
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(2)
        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

    def like_photo_by_hasag(self,hashtag):
        browser = self.browser
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(5)

        for i in range(1,4):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(3,5))

        hrefs = browser.find_elements_by_tag_name('a')

        posts_urls = []
        for item in hrefs:
            href = item.get_attribute('href')
            if "/p/" in href:
                posts_urls.append(href)

        for url in posts_urls:
            try:
                browser.get(url)
                time.sleep(3)

                like_button = browser.find_element_by_xpath(
                    '/html/body/div[6]/div[3]/div/article/div/div[3]/div/div/section[1]/span[1]/button'
                ).click()
                time.sleep(random.randrange(80,100))
            except Exception as ex:
                print(ex)
                self.close_browser()

    def xpath_exists(self,url):
        browser = self.browser
        try:
            browser.find_element_by_xpath(url)
            exist = True
        except NoSuchFrameException:
            exist = False
        return exist
    #ставим лайк на пост по прямой ссылке
    def put_exactly_like(self,userpost):
        browser = self.browser
        browser.get(userpost)
        time.sleep(4)

        wrong_userpage = "/html/body/div[1]/div/div/section/main/div/div/h2"
        if self.xpath_exists(wrong_userpage):
            print("Такого поста не существует, проверьте URL")
            self.close_browser()
        else:
            print("Пост успешно найдет, ставим лайк!")
            time.sleep(2)
            like_button = "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button"
            browser.find_element_by_xpath(like_button).click()
            self.browser()

my_bot = InstagramBot(username,password)
my_bot.login()
my_bot.put_exactly_like("https://www.instagram.com/p/CZtwfyKP9dC/")