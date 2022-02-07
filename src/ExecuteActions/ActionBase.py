
"""
15-09-2021  Kannan      Initial version


"""
class ActionBase(object):
    def __init__(self,driverBase):
        self.driverBase=driverBase

    def execute(self):
        raise Exception('execute should be implemented')

