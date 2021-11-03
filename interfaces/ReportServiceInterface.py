#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class ReportServiceInterface(metaclass=ABCMeta):
    """ The base service called by BI to process report """
    @abstractmethod
    def send_report(self, reportTypeInterface):
        '''
        Inject ReportType to know which (aarp or comerica)
        report needs to be created
        '''
        pass
