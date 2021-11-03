#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class SenderStrategyInterface(metaclass=ABCMeta):
    '''
    The sender startegy that includes the info
    (sender email address, receiver emial address)
    to send email and injects the EmailUtilInterface to send email.
    '''
    @abstractmethod
    def send(self, filePath, emailUtilInterface):
        """Inject attachment file path and EmailUtilInterface to send email"""
        pass
