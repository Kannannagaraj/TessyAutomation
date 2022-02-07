import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from ExecuteActions.ActionBase import ActionBase

"""
15-09-2021  Kannan      Initial version


"""

class linktextclick(ActionBase):

    def __init__(self,driverBase):
        super(linktextclick, self).__init__(driverBase)

    def execute(self):
        '''
        to do the link text click operation in webdriver
        :return:
        '''
        try:
            print(self.driverBase.value)
            if self.driverBase.value is not None and self.driverBase.value != '':
                element = self.driverBase.driver.find_element_by_link_text(self.driverBase.value)
                print(element)
                if element is not None:
                    action = ActionChains(self.driverBase.driver)
                    action.context_click(on_element=element)
                    action.perform()
            return True
        except Exception as e:
            return False

