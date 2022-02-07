
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from Utilities.ReadConfiguration import ReadConfiguration

""""
TODO Items.
1. Need to implement for various browsers

"""

"""
used to initate the webdriver based on the browser param

15-09-2021  Kannan      Initial version


"""

class Driverbase(object):
    def __init__(self, browser):
        self.headless = ReadConfiguration.read_config('TestConfig.cfg', 'TestExecution', 'Headless')
        if str(browser).lower() == 'chrome':
            if str(self.headless).lower()=='true':
                options = Options()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                # create webdriver object
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            else:
                driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            driver = webdriver.Firefox('C:/geckodriver-v0.29.1-win64/geckodriver')
        self.driver = driver
        self.driver.maximize_window()
        self.value = ''
        self.element_xpath = None
        self.element_id = None
