import psutil
import os


def killer(PROCNAME):
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()


killer("Realphones System-Wide.exe")
killer("audiodg.exe")

os.startfile('C:\\Windows\\System32\\audiodg.exe')
os.startfile("C:\Program Files\dSONIQ\Realphones\Realphones System-Wide.exe")