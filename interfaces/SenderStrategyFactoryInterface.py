#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class SenderStrategyFactoryInterface(metaclass=ABCMeta):
    """ The factory to get sender startegy """
    @abstractmethod
    def get_sender_strategy(self, ReportTypeInterface):
        '''
        Inject ReportType to know which
        (aarp or comerica) strategy needs to give
        '''
        pass
