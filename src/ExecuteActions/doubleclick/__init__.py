import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from ExecuteActions.ActionBase import ActionBase

"""
15-09-2021  Kannan      Initial version


"""

class doubleclick(ActionBase):

    def __init__(self,driverBase):
        super(doubleclick, self).__init__(driverBase)

    def execute(self):
        '''
        To do the double click operation in the webdriver.
        :return:
        '''
        try:
            if self.driverBase.element_xpath is not None and self.driverBase.element_xpath != '':
                element = self.driverBase.driver.find_element_by_xpath(self.driverBase.element_xpath)
            if self.driverBase.element_id is not None and self.driverBase.element_id != '' and element is None:
                element = self.driverBase.driver.find_element_by_id(self.driverBase.element_id)
            if element is not None:
                action = ActionChains(self.driverBase.driver)
                action.double_click(on_element=element)
                action.perform()
            return True
        except Exception as e:
            return False