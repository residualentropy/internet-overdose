from subprocess import Popen, PIPE
from os import system

from datetime import datetime, timedelta
from time import sleep

# TODO: Replace the -kg flag with a -lb flag for American users
SLEEP_JOURNAL_SHELL = "journalctl -kg '^PM:.*suspend' | tail -n 1"

# chosen randomly by fair dice roll
# pure coincidence that it's the 3 in :3
THRESHOLD_TIME = timedelta(minutes= 3)

def get_time_since_sleep(subject: str):
    if subject == 'me':
        raise RuntimeError('i dont even want to know')
    if subject != 'computer':
        raise RuntimeError('there is me and computer, that is all')
    sub = Popen(SLEEP_JOURNAL_SHELL, shell= True, stdout= PIPE)
    line = next(sub.stdout).decode('utf-8').strip()
    if not line.endswith(': suspend exit'):
        return 0
    date_text = line[len('Jan 01 '):len('Jan 01 00:00:00')]
    date = datetime.strptime(date_text, '%H:%M:%S')
    # what follows is stupid
    # unfortunately i don't care
    now_text = datetime.now().strftime('%H:%M:%S')
    now = datetime.strptime(now_text, '%H:%M:%S')
    return now - date

def the_british_are_coming():
    system('swaymsg workspace TouchGrass')
    system('mpv --fs INTERNET_OVERDOSE.mp4')

while True:
    print('digging inside your computer for yummy logs...')
    time_since = get_time_since_sleep('computer')
    if time_since > THRESHOLD_TIME:
        print('FOUND SOMETHING!')
        the_british_are_coming()
    else:
        print('ur safe... this time')
    sleep(60)
