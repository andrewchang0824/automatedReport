#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class QueryStrategyInterface(metaclass=ABCMeta):
    """ The query startegy that includes the query information and """
    """ injects the DBUtilInterface to complete query """
    @abstractmethod
    def query(self, dBUtilInterface):
        '''
        Inject DBUtilInterface to complete the query
        and returnback an array
        '''
        pass
