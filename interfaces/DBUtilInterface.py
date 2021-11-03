#!/usr/bin/python3

from abc import ABCMeta, abstractmethod
# import the db connection module


class DBUtilInterface(metaclass=ABCMeta):
    """ The DB utility resible to connect DB and """
    """ injecting query string to come up the final query result """
    @abstractmethod
    def query(self, queryString):
        """Inject query string and return back an array"""
        pass
