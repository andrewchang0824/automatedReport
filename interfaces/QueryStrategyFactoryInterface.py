#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class QueryStrategyFactoryInterface(metaclass=ABCMeta):
    """ The factory to get query startegy """
    @abstractmethod
    def get_query_strategy(self, reportTypeInterface):
        '''
        Inject ReportType to know which (aarp or comerica)
        strategy needs to give
        '''
        pass
