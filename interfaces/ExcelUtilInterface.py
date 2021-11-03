#!/usr/bin/python3

from abc import ABCMeta, abstractmethod
# import xlsxwriter module


class ExcelUtilInterface(metaclass=ABCMeta):
    '''
    The Excel utility responsible to create excel file and
    inject query result and other info to come up the final query result
    '''
    @abstractmethod
    def build(self, queryResult, excelfilePath, password):
        '''
        Inject query result and out excel path and password to
        create excel file, and return back file path
        '''
        pass
