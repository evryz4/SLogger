# SLogger (SimpleLogger) library for easy logging
# Official SLogger repository - https://github.com/watermelon46/slogger
# Commands:

# log(text) - write anything in logs
# info(text) - write info in logs
# warn(text) - write warn in logs
# error(text) - write error in logs
# user(text) - write user input in logs
# printing(boolean) - enable additional printing logs in terminal
# get_current_time() - get current time in HOURS:MINUTES:SECONDS type
# clear() - clear terminal

class BuildInfo():
    version = '1.1'
    buildType = 'Release'
    branding = 'SLogger'
    githublink = 'https://github.com/watermelon46/slogger'



from datetime import datetime
from time import sleep
from os import system

logfile = open('latest.log', 'w+')
logfile.truncate(0)

def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def clear():
    try:
        system('cls')
    except:
        print('\n' * 100)

enable_printing = True

def log(text):
    logtext = f'[{get_current_time()}] [{BuildInfo.branding}] {text}'
    logfile.write(logtext + '\n')
    if enable_printing == True:
        print(logtext, end='')

def warn(text):
    log(f'[WARN] {text}')

def error(text):
    log(f'[ERROR] {text}')

def info(text):
    log(f'[INFO] {text}')

def user(text):
    log(f'[USER] {text}')

def printing(mode = True):
    global enable_printing
    info('enable_printing changed to {mode}')
    enable_printing = bool(mode)

info(f'{BuildInfo.branding} {BuildInfo.version} {BuildInfo.buildType} started')

