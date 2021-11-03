#!/usr/bin/python3

from abc import ABCMeta, abstractmethod
# import the smtp module


class EmailUtilInterface(metaclass=ABCMeta):
    """ The Email utility responsible to email and """
    """ being injected sender, receiver, and other email related info. """
    @abstractmethod
    def send(self, filePath, sender, receiver, subject, message):
        '''
        @filePath string    attachment filePath
        @sender array       senders' email address
        @receiver array     receivers' email address
        @subject string     email subject
        @message string     email body
        '''
        pass
