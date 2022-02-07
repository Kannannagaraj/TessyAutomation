import datetime
import importlib
import sys
import traceback

from Actionkeys import ActionKeys
from Utilities.CustomLogger import Logger
from Utilities.ReadConfiguration import ReadConfiguration
from src.DriverBase import Driverbase


"""
15-09-2021  Kannan      Initial version


"""


class TestStepExecution:
    def __init__(self, test_steps, test_data):
        self.test_steps = test_steps
        self.test_data = test_data
        self.screenshot_path = ReadConfiguration.read_config('TestConfig.cfg', 'Project', 'ScreenshotsPath').strip('/')
        self.logger = Logger.logger()

    def Testcase_step_execution(self):
        '''
        this is def is used to execute the testcase steps one by one in sequence order that we configured in testcase file.
        :return:
        '''
        self.logger.info(
            'Testcase steps started executing')
        print('test steps started executing')
        browser = self.test_data[0]['test_data']
        driverbase = Driverbase(browser)
        # removing the browser step from the list. since its been executed already dont want to loop again for the execution
        self.test_steps.pop(0)
        self.result = True
        i = 1;
        try:
            for ts in self.test_steps:
                driverbase.value = self.test_data[i]['test_data']
                driverbase.element_xpath = ts['element_xpath']
                driverbase.element_id = ts['element_id']
                if self.result == True:
                    action_key = str(ts['action_key']).lower()
                    self.logger.info(
                        'Executing {actionkey} - {desc}'.format(actionkey=action_key, desc=str(ts['description'])))

                    if action_key != '' and action_key in ActionKeys.action_keys():
                        actions_module = importlib.import_module('ExecuteActions.{act}'.format(act=action_key))
                        actionClass = getattr(actions_module, action_key)
                        actionInstance = actionClass(driverbase)
                        if actionInstance is not None:
                            self.result = actionInstance.execute()
                            if self.result == False:
                                currentDT = datetime.datetime.now()
                                screenshot_fullname = '{scpath}/{scname}_{ts}.png'.format(scpath=self.screenshot_path,
                                                                                          scname=str(ts['tc_step_id']),
                                                                                          ts=str(currentDT.strftime(
                                                                                              "%Y%m%d_%H%M%S")))
                                driverbase.driver.save_screenshot(screenshot_fullname)
                                self.logger.info('Screenshot taken for step {ts}'.format(ts=str(ts['tc_step_id'])))
                    else:
                        self.result = False
                        self.logger.info(
                            'Invalid actionkey found "{actionkey}" - {desc}'.format(actionkey=action_key,
                                                                                    desc=str(ts['description'])))

                        break
                i = i + 1
        except Exception as e:
            print(e)
            print(sys.exc_info())
            print(traceback.format_exc())
            self.result = False
        driverbase.driver.close()
        return self.result
