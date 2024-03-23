from datetime import datetime
from time import sleep
from os import system
from enum import Enum

class BuildInfo(Enum):
    version = '1.2'
    buildType = '[evryz4`s fork]'
    githublink = 'https://github.com/evryz4/slogger'
    githublinkforkedfrom = 'https://github.com/watermelon46/slogger'

class Logging:
    def __init__(self, enable_printing: bool = True, branding: str = 'Slogger'):
        """Initialize settings, create/clean log file"""

        logfile = open('latest.log', 'w+')
        logfile.truncate(0)

        self._enable_printing = enable_printing
        self._branding = branding
        self._logfile = logfile

    def log(self, type: str, text: str) -> None:
        """Write log"""

        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        logtext = f'{self._branding} {BuildInfo.version.value} {BuildInfo.buildType.value} | {time} | [{type.upper()}] | {text}'
        self._logfile.write(logtext + '\n')

        if self._enable_printing == True:
            print(logtext)

    def buildlog(self, type):
        """Build your own log func with entered type
        Returns lambda func"""

        return lambda ftext: self.log(type.upper(), ftext)
    
    def decorator_log(self, func):
        """Decorator | Write a log with returned value every function running"""
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            self.log('func', f'{func.__name__}() return: {result}')
            return result
        return wrapper
