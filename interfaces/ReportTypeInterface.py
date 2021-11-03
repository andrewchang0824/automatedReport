#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class ReportTypeInterface(metaclass=ABCMeta):
    """ Set/Get which type it needs to be retrieved. """
    """ instance data attribute : string __type"""
    @abstractmethod
    def get_report_type(self):
        """Return the type that is a string. e.g, aarp, comerica"""
        pass

    @abstractmethod
    def set_report_type(self, type):
        """Set the type that is a string, e.g., aarp, comerica"""
        pass
