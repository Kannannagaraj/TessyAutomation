import datetime, os, time
from RunTestcases.TestStepExecution import TestStepExecution
from Utilities.HtmlReportGenerate import HtmlReport
from Utilities.WriteReport import WriteReport
from Utilities.ReadConfiguration import ReadConfiguration
from Utilities.ReadTestCaseSteps import ReadTestCases
from Utilities.ReadTestData import ReadTestData
from Utilities.CustomLogger import Logger

"""
15-09-2021  Kannan      Initial version
16-09-2021  Kannan      Impelemented the report generation for the test case executions. Added WriteReport() in  RunTestCases()
17-09-2021  Kannan      Implemented the logging and screenshot functionality

"""


class TestCases:
    def __init__(self):
        self.testcasePath = ReadConfiguration.read_config('TestConfig.cfg', 'TestSuite', 'TestCasePath').strip('/')
        self.report_format = ReadConfiguration.read_config('TestConfig.cfg', 'Report', 'ReportFormat')
        self.testDataPath = ReadConfiguration.read_config('TestConfig.cfg', 'TestSuite', 'TestDataPath').strip('/')
        self.max_testCases = 0
        self.logger = Logger.logger()
        self.GetTestCasesCount()

    def GetTestCasesCount(self):
        '''
        It will read the path that configured in testconfig.cfg file and get the count of directories available in that
        particular path. Assumption here is we are taking the no. of directories count as no. of test cases count.
        :return:
        '''
        if not os.path.exists('{path}'.format(path=self.testcasePath + '/')):
            self.logger.info('Testcase path does not exists. Given path is {}'.format(self.testcasePath + '/'))
            return
        if not os.path.exists('{path}'.format(path=self.testDataPath + '/')):
            self.logger.info('Testdata path does not exists. Given path is {}'.format(self.testDataPath + '/'))
            return
        totalDir = os.listdir(self.testcasePath + '/')
        self.max_testCases = len(totalDir)
        self.logger.info('Started collecting the testcases from path {p}'.format(p=self.testcasePath + '/'))
        self.logger.info('{cnt} testcases found from the path'.format(cnt=str(self.max_testCases)))

    def RunTestCases(self):
        '''
        this def is used to run the no. of testcases by iterating one by one, and also collect the info that required to
        generate the report.
        :return:
        '''

        if self.max_testCases > 0:
            self.test_result = True
            self.report_data = []

            self.report_data.append([])
            for case_no in range(self.max_testCases + 1):
                if case_no > 0:
                    case_report = []
                    testCasePrefix = ReadConfiguration.read_config('TestConfig.cfg', 'TestPattern', 'TestCasePrefix')
                    testCaseName = testCasePrefix + str(case_no)
                    case_report.append(testCaseName)
                    start_time = datetime.datetime.now()
                    self.logger.info(
                        '***************** {c} testcase started **********************'.format(c=testCaseName))
                    test_case_steps = ReadTestCases.ReadTestCase(case_no)
                    self.logger.info(
                        '{c} test steps found to execute'.format(c=str(len(test_case_steps))))
                    if len(test_case_steps) == 0:
                        self.test_result = False
                        self.logger.info(
                            'Testcase {tc} skipped gracefully from execution,due to no step(s) found'.format(
                                tc=testCaseName))
                        case_report.append('Skipped')
                        case_report.append('0.00')
                        self.report_data.append(case_report)
                        continue
                    test_case_data = ReadTestData.ReadtestData(case_no)
                    if len(test_case_data) == 0:
                        self.test_result = False
                        self.logger.info(
                            'Testcase {tc} skipped gracefully from execution, due to no data found'.format(
                                tc=testCaseName))
                        case_report.append('Skipped')
                        case_report.append('0.00')
                        self.report_data.append(case_report)

                        continue
                    tsexecution = TestStepExecution(test_case_steps, test_case_data)
                    self.test_result = tsexecution.Testcase_step_execution()
                    end_time = datetime.datetime.now()
                    duration = (end_time - start_time).total_seconds()
                    result = 'Passed' if self.test_result == True else 'Failed'
                    self.logger.info('{tc} executed with result of "{rs}"'.format(tc=testCaseName, rs=result))
                    self.logger.info(
                        '***************** {c} testcase completed **********************'.format(c=testCaseName))
                    case_report.append(result)
                    # case_report.append(str(start_time))
                    # case_report.append(str(end_time))
                    case_report.append(duration)
                    self.report_data.append(case_report)
                    time.sleep(2)
            self.logger.info('Testcase Execution report generating')
            if self.report_format.lower() == 'html':
                report = HtmlReport(self.report_data)
            else:
                report = WriteReport(self.report_data)
            report_name = report.writeReport()
            self.logger.info('Testcase Execution report saved in {p}'.format(p=str(report_name)))
