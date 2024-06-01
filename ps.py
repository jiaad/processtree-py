import sys
from collections.abc import Mapping
from typing import Type

# DATA
# PID PPID COMM

class Process:
    def __init__(self, pid, ppid, comm):
        self.pid = pid
        self.ppid = ppid
        self.comm = comm
        self.childrens = []
    def __str__(self):
        return f"pid: {self.pid} | ppid: {self.ppid} | childrens: {list(map(lambda x: (x.pid, x.ppid), self.childrens))} | comm: {self.comm}"
    
def init():
    processes = {}
    data = sys.stdin.readlines()[1:]
    for datum in data:
        pid, ppid, comm = " ".join(datum.split()).split(sep=" ", maxsplit=2)
        new_process = Process(pid, ppid, comm)
        if processes.get(ppid) != None: # if ppid present
            parent  = processes.get(ppid)
            parent.childrens.append(new_process)
        processes[pid] = new_process
    print("data", processes)
    for _, pid in enumerate(processes):
        print(processes[pid])


init()
