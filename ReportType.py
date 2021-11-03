from interfaces.ReportTypeInterface import ReportTypeInterface


class ReportType(ReportTypeInterface):
    """ Implementation of ReportTypeInterface"""

    def get_report_type(self):
        return self.__type

    def set_report_type(self, type):
        self.__type = type

ReportTypeInterface.register(ReportType)