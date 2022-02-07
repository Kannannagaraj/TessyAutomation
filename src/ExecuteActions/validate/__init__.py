import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from ExecuteActions.ActionBase import ActionBase

"""
15-09-2021  Kannan      Initial version


"""

class validate(ActionBase):

    def __init__(self,driverBase):
        super(validate, self).__init__(driverBase)

    def execute(self):
        '''
        To validate the given message is presented  anywhere in the webdriver.
        :return:
        '''
        htmlText=self.driverBase.driver.find_element_by_xpath("html").text
        if self.driverBase.value in htmlText:
            return True
        else:
            return False

