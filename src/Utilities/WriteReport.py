from datetime import datetime
import xlsxwriter as xlsxwriter
from Utilities.ReadConfiguration import ReadConfiguration
from Utilities.ReportBase import ReportBase

"""
16-09-2021  Kannan      Initial version


"""

class WriteReport(ReportBase):

    def __init__(self,report_data):
        super(WriteReport,self).__init__(report_data)

    def writeReport(self):
        '''
        generate the execl file using xlsxwriter and write the data into it.
        :return:
        '''
        column_name=['Testcase','Result','Duration(in seconds)']
        currentDT = datetime.now()
        report_fullpath='{reportpath}/{reportname}_{ts}.xlsx'.format(reportpath= self.report_path,reportname= self.report_name,ts=str(currentDT.strftime("%Y%m%d_%H%M%S")))
        self.report_data[0]=column_name
        with xlsxwriter.Workbook(report_fullpath) as workbook:
            worksheet = workbook.add_worksheet()

            for row_num, data in enumerate(self.report_data):
                worksheet.write_row(row_num, 0, data)
        return report_fullpath