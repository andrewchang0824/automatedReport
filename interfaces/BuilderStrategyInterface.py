#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class BuilderStrategyInterface(metaclass=ABCMeta):
    """ The builder startegy that includes the info to build excel and """
    """ injects the ExcelUtilInterface to create Excel file. """
    @abstractmethod
    def build(self, queryResult, excelUtilInterface):
        '''
        Inject query result and ExcelUtilInterface to
        create the excel file and return full path of file
        '''
        pass
