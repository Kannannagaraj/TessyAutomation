import sys
import traceback
import openpyxl
from Utilities.ReadConfiguration import ReadConfiguration
import pathlib

"""
15-09-2021  Kannan      Initial version


"""
class ReadTestData:


    def ReadtestData(case_no):
        '''
        it read the execl file from the configured path in testconfig.cfg file.
        :return: list of data that available in file
        '''
        try:
            sheet_cells = []
            if case_no > 0:
                testDataPath = ReadConfiguration.read_config('TestConfig.cfg', 'TestSuite', 'TestDataPath').strip('/')
                testCasePrefix = ReadConfiguration.read_config('TestConfig.cfg', 'TestPattern', 'TestCasePrefix')
                testDataPrefix = ReadConfiguration.read_config('TestConfig.cfg', 'TestPattern', 'TestDataPrefix')
                testDataName = testDataPrefix + str(case_no)
                testCaseName = testCasePrefix + str(case_no)
                testDataPath ='{testdatapath}/{testcasename}/TestData/{testdataname}.xlsx'.format(testdatapath=testDataPath,testcasename=testCaseName,testdataname=testDataName)
                print(testDataPath)
                file = pathlib.Path(testDataPath)
                if file.exists():
                    print("File exist")
                    wb = openpyxl.load_workbook(testDataPath)
                    sh = wb['Sheet1']
                    for rows in sh.iter_rows():
                        '''row_cells = []
                        for cell in rows:
                            row_cells.append(cell.value)
                        sheet_cells.append(tuple(row_cells))'''
                        sheet_cells.append({'td_id': rows[0].value,
                                            'tc_id': rows[1].value,
                                            'tc_step_id': rows[2].value,
                                            'test_data': rows[3].value
                                            })

                else:
                    print("File not exist")
                if len(sheet_cells)>0:
                    sheet_cells.pop(0)
                return sheet_cells

        except Exception as e:
            print('FATAL ERROR in ReadTestData.py(ReadtestData)')
            print(e)
            print(sys.exc_info())
            print(traceback.format_exc())
            raise Exception(e)
