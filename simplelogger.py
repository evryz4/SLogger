# SimpleLogger (SLogger) library for easy logging
# Official SLogger repository - https://github.com/watermelon46/slogger
#
# Commands:
#
# log(text) - write anything in logs
# info(text) - write info in logs
# warn(text) - write warn in logs
# error(text) - write error in logs
# user(text) - write user input in logs
# enable_printint(boolean) - enable additional printing logs in terminal
# get_current_time() - get current time in HOURS:MINUTES:SECONDS type
# clear() - clear terminal
# loadinganim(text, delay, cycles) - play loading animation


from datetime import datetime
from time import sleep
from os import system

def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

class BuildInfo():
    version = '1.0'
    buildType = 'Release'
    branding = 'SimpleLogger'


def clear():
    try:
        system('cls')
    except:
        print('\n' * 100)

loading_symvols = '| / - \ '

def loadinganim(text, delay=0.1, cycles=5):
    for i in range(1, cycles):
        for i in loading_symvols:
            clear()
            print(f'{text} {i}')
            sleep(delay)

logfile = open('latestlog.txt', 'w+')
logfile.truncate(0)

enable_printing = False

def enable_printing(mode = True):
    global enable_printing
    enable_printing = bool(mode)

def log(text):
    logtext = f'[{get_current_time()}] [{BuildInfo.branding}] {text}'
    logfile.write(logtext + '\n')
    if enable_printing:
        print(logtext)

def warn(text):
    logtext = f'[{get_current_time()}] [{BuildInfo.branding}] [WARN] {text}'
    logfile.write(logtext + '\n')
    if enable_printing:
        print(logtext)

def error(text):
    logtext = f'[{get_current_time()}] [{BuildInfo.branding}] [ERROR] {text}'
    logfile.write(logtext + '\n')
    if enable_printing:
        print(logtext)

def info(text):
    logtext = f'[{get_current_time()}] [{BuildInfo.branding}] [INFO] {text}'
    logfile.write(logtext + '\n')
    if enable_printing:
        print(logtext)

def user(text):
    logtext = f'[{get_current_time()}] [{BuildInfo.branding}] [USER] {text}'
    logfile.write(logtext + '\n')
    if enable_printing:
        print(logtext)

info(f'SLogger started. Version {BuildInfo.version} {BuildInfo.buildType}\n')
