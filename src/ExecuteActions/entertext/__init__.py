import sys
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from ExecuteActions.ActionBase import ActionBase

"""
15-09-2021  Kannan      Initial version


"""


class entertext(ActionBase):

    def __init__(self, driverBase):
        super(entertext, self).__init__(driverBase)


    def execute(self):
        '''
        it is used to enter the text into the element that can be found out using element xpath or id from the webdriver.
        :return:
        '''
        try:
            if self.driverBase.value is not None:
                if self.driverBase.element_xpath is not None and self.driverBase.element_xpath != '':
                    element = self.driverBase.driver.find_element_by_xpath(self.driverBase.element_xpath)
                if self.driverBase.element_id is not None and self.driverBase.element_id != '' and element is None:
                    element = self.driverBase.driver.find_element_by_id(self.driverBase.element_id)
                if element is not None:
                    element.clear()
                    action = ActionChains(self.driverBase.driver)
                    action.click(on_element=element)
                    action.send_keys(self.driverBase.value)
                    action.perform()
            return True
        except Exception as e:
            print(e)
            print(sys.exc_info())
            print(traceback.format_exc())
            return False

