#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class BuilderStrategyFactoryInterface(metaclass=ABCMeta):
    """ The factory to get builder startegy """
    @abstractmethod
    def get_builder_strategy(self, reportTypeInterface):
        '''
        Inject ReportType to know which (aarp or comerica)
        strategy needs to give
        '''
        pass
