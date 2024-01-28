class BuildInfo():
    version = '1.2'
    buildType = 'Release'
    branding = 'SLogger'
    brandingInLogs = f'[{branding}]'
    githublink = 'https://github.com/watermelon46/slogger'

from datetime import datetime
from time import sleep
from os import system

logfile = open('latest.log', 'w+')
logfile.truncate(0)

enable_printing = True



def change_branding(newbranding = None):
    """Change branding in logs from ''Slogger'' to your."""
    BuildInfo.brandingInLogs = f'[{newbranding}]'

def log(text):
    """Write anything in logs"""
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    logtext = f'[{time}] {BuildInfo.brandingInLogs} {text}'
    logfile.write(logtext + '\n')
    if enable_printing == True:
        print(logtext, end='')

def warn(text):
    """Write warn in logs"""
    log(f'[WARN] {text}')

def error(text):
    """Write error in logs"""
    log(f'[ERROR] {text}')

def info(text):
    """Write info in logs"""
    log(f'[INFO] {text}')

def user(text):
    """Write user input in logs"""
    log(f'[USER] {text}')

def custom(logtype, text):
    """Write custom log in logs"""
    log(f'[{logtype}] {text}')
    
def printing(mode = True):
    """Enable additional logs printing in terminal"""
    global enable_printing
    enable_printing = bool(mode)
    info(f'enable_printing changed to {mode}')

info(f'{BuildInfo.branding} {BuildInfo.version} {BuildInfo.buildType} started')
if BuildInfo.buildType != 'Release':
    warn(f'You are using unstable version of SLogger. Download stable from {BuildInfo.githublink}')
