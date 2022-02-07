import sys
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



from ExecuteActions.ActionBase import ActionBase

"""
15-09-2021  Kannan      Initial version


"""
class geturl(ActionBase):

    def __init__(self, driverBase):
        super(geturl, self).__init__(driverBase)

    def execute(self):
        '''
        load the url into the webdriver or in the opened browser
        :return:
        '''
        try:
            print(self.driverBase.value)
            self.driverBase.driver.get(self.driverBase.value)
            return True
        except Exception as e:
            print(e)

            return False
