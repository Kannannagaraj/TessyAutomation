import logging
import os

from Utilities.ReadConfiguration import ReadConfiguration
from datetime import datetime

"""
17-09-2021  Kannan      Initial version


"""
class Logger:
    @staticmethod
    def logger():
        logpath= ReadConfiguration.read_config('TestConfig.cfg', 'Project', 'LogPath').strip('/')
        currentDT = datetime.now()
        if not os.path.exists('{path}'.format(path=logpath)):
            os.makedirs('{path}'.format(path=logpath))
        logpath=f'{logpath}/Testexecution_{str(currentDT.strftime("%Y%m%d_%H%M"))}.log'
        logging.basicConfig(filename=logpath,format='%(asctime)s: %(levelname)s : %(message)s',datefmt='%m/%d/%y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return  logger