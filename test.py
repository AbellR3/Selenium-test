from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://projecteuler.net/index.php?section=problems')
    elem = driver.find_element_by_class_name('jump_to')
    elem.send_keys('14')
    elem.send_keys(Keys.ENTER)
    driver.back()
    elems = driver.find_elements_by_class_name('id_column')
    num = len(elems) - 1
    driver.close()


if __name__ == '__main__':
    main()
