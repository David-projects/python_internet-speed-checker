from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)

        start_test_buttom = self.driver.find_element(By.CLASS_NAME, value="js-start-test")
        start_test_buttom.click()

        time.sleep(50)

        download_speed = self.driver.find_element(By.CLASS_NAME, value="download-speed")
        upload_speed = self.driver.find_element(By.CLASS_NAME, value="upload-speed")

        return {
            "down": download_speed.text,
            "up": upload_speed.text
        }

    def tweet_at_provider(self, config):
        self.driver.get("https://twitter.com/?lang=en-gb")

        time.sleep(10)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        login_button.click()
        time.sleep(10)

        user = self.driver.find_element(By.XPATH,
                                        value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user.send_keys(config['username'])
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        login_button.click()
        time.sleep(10)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(config['password'])

        login_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_button.click()

        time.sleep(30)
        text_box = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span')
        text_box.send_keys(config['message'])

        submit_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        submit_button.click()