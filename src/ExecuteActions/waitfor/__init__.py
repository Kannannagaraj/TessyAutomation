import time
from selenium import webdriver


from ExecuteActions.ActionBase import ActionBase

"""
15-09-2021  Kannan      Initial version


"""

class waitfor(ActionBase):

    def __init__(self, driverBase):
        super(waitfor, self).__init__(driverBase)

    def execute(self):
        '''
        pass the execution for some time.
        :return:
        '''
        #self.driver.implicitly_wait(waitTime)
        time.sleep(self.driverBase.value)
        return True