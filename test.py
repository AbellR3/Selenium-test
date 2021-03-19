from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://projecteuler.net/index.php?section=problems')
    elem = driver.find_element_by_class_name('jump_to')
    elem.send_keys('14')
    elem.send_keys(Keys.ENTER)
    time.sleep(4)
    driver.back()
    table = driver.find_element_by_id('problems_table')
    table.click()
    elements = table.find_elements_by_tag_name('a')
    num = len(elements) - 1
    elem = elements[num]
    elem.click()
    time.sleep(4)
    driver.close()


if __name__ == '__main__':
    main()
