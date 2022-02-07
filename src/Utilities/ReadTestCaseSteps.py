import sys
import traceback
import openpyxl
from Utilities.ReadConfiguration import ReadConfiguration
import pathlib


"""
15-09-2021  Kannan      Initial version


"""

class ReadTestCases:


    def ReadTestCase(case_no):
        '''
        it read the execl file from the configured path in testconfig.cfg file.
        :return: list of data that available in file
        '''
        try:
            sheet_cells = []
            if case_no > 0:
                testcasePath = ReadConfiguration.read_config('TestConfig.cfg', 'TestSuite', 'TestCasePath').strip('/')
                testCasePrefix = ReadConfiguration.read_config('TestConfig.cfg', 'TestPattern', 'TestCasePrefix')
                testCaseName = testCasePrefix + str(case_no)
                testcasePath='{testcasepath}/{testcasename}/TestCase/{testcasename}.xlsx'.format(testcasepath=testcasePath,testcasename=testCaseName)

                print(testcasePath)
                file = pathlib.Path(testcasePath)
                if file.exists():
                    print("File exist")
                    wb = openpyxl.load_workbook(testcasePath)
                    sh = wb['Sheet1']
                    for rows in sh.iter_rows():
                        sheet_cells.append({'tc_id': rows[0].value,
                                            'tc_step_id': rows[1].value,
                                            'element_xpath': rows[2].value,
                                            'element_id': rows[3].value,
                                            'action_key': str(rows[4].value).lower(),
                                            'description': rows[5].value})

                else:
                    print("File not exist")
                if len(sheet_cells)>0:
                    sheet_cells.pop(0)
                return sheet_cells

        except Exception as e:
            print('FATAL ERROR in ReadTest.py(ReadTestCases)')
            print(e)
            print(sys.exc_info())
            print(traceback.format_exc())
            raise Exception(e)
