import os
from datetime import datetime
from decimal import Decimal
from HtmlReportTempletes import HtmlReportTemplete
from Utilities.ReadConfiguration import ReadConfiguration
from Utilities.ReportBase import ReportBase

"""
16-09-2021  Kannan      Initial version


"""


class HtmlReport(ReportBase):

    def __init__(self, report_data):
        super(HtmlReport, self).__init__(report_data)

    def writeReport(self):
        html_temp = HtmlReportTemplete()
        currentDT = datetime.now()
        reporteGenetated = str(currentDT.strftime("%Y%m%d_%H%M%S"))
        report_fullpath = '{reportpath}/{reportname}_{ts}.html'.format(reportpath=self.report_path,
                                                                      reportname=self.report_name,
                                                                      ts=reporteGenetated)
        self.report_data.pop(0)
        testcaseCnt = len(self.report_data)
        lst_passed = filter(lambda x: str(x[1]).lower() == 'passed', self.report_data)
        passedCnt=len(list(lst_passed))
        lst_skipped = filter(lambda x: str(x[1]).lower() == 'skipped', self.report_data)
        skippedCnt=len(list(lst_skipped))
        lst_failed = filter(lambda x: str(x[1]).lower() == 'failed', self.report_data)
        failedCnt=len(list(lst_failed))
        totalSeconds = round(sum(map(Decimal ,[x[2] for x in self.report_data])))
        ts_tbody =''
        for tb in self.report_data:
            ts_tbody=ts_tbody+str(html_temp.tbody_templete).format(tresult=str(tb[1]).lower(),test_result=str(tb[1]),ts_id=str(tb[0]),duration=str(tb[2]))

        html_finalreport=str(html_temp.reportTemplete).replace('{Reportname}',self.report_name)
        html_finalreport=html_finalreport.replace('{ReportGenerated}',reporteGenetated)
        html_finalreport = html_finalreport.replace('{testcasecnt}', str(testcaseCnt))
        html_finalreport = html_finalreport.replace('{totalSeconds}', str(totalSeconds))
        html_finalreport = html_finalreport.replace('{passedcnt}', str(passedCnt))
        html_finalreport = html_finalreport.replace('{skippedcnt}', str(skippedCnt))
        html_finalreport = html_finalreport.replace('{failedcnt}', str(failedCnt))
        html_finalreport = html_finalreport.replace('{ts_tbody}', str(ts_tbody))


        with open(report_fullpath, 'w') as file:
            file.writelines("% s\n" % html_finalreport)
        css_filepath='{path}/assets/style.css'.format(path=self.report_path)
        with open(css_filepath,'w') as file:
            file.writelines("%s\n" % html_temp.cssFile)

        return report_fullpath

