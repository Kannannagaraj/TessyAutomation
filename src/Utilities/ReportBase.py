import os

from Utilities.ReadConfiguration import ReadConfiguration

"""
16-09-2021  Kannan      Initial version


"""


class ReportBase:
    def __init__(self, report_data):
        self.report_data = report_data
        self.report_path = ReadConfiguration.read_config('TestConfig.cfg', 'Report', 'ReportPath').strip('/')
        self.report_name = ReadConfiguration.read_config('TestConfig.cfg', 'Report', 'ReportName')
        self.report_format = ReadConfiguration.read_config('TestConfig.cfg', 'Report', 'ReportFormat')
        self.reportpath_validate()

    def reportpath_validate(self):
        if not os.path.exists('{path}'.format(path=self.report_path)):
            os.makedirs('{path}'.format(path=self.report_path))
        if self.report_format.lower() == 'html':
            if not os.path.exists('{path}/assets'.format(path=self.report_path)):
                os.makedirs('{path}/assets'.format(path=self.report_path))

    def writeReport(self):
        raise Exception('writeReport should be overridden')
