import sys
from process_node import Process

# DATA
# PID PPID COMM


MISSING_PARENTS = set()
PRINTED_PROCESSES = set()
LAUNCHD_PID = "1"


def normalize_pid_len(pid):
    if len(pid) == 5:
        return pid
    prefix_len = 5 - len(pid)
    return ("0" * prefix_len) + pid


def handle_late_parents(processes):
    for parent in MISSING_PARENTS:
        if processes.get(parent) == None:
            new_node = Process(parent, None, "__MISSING__")
            processes[parent] = new_node
        for _, ps in enumerate(processes):

            if not processes[ps].ppid == parent:
                continue
            if processes.get(parent):
                processes[parent].childrens.append(processes[ps])


def parse_line(line):
    pid, ppid, comm = " ".join(line.split()).split(sep=" ", maxsplit=2)
    pid = normalize_pid_len(pid)
    ppid = normalize_pid_len(ppid)
    return pid, ppid, comm


def scrap_processes():
    processes = {}
    data = sys.stdin.readlines()[1:]
    for line in data:
        pid, ppid, comm = parse_line(line)
        new_process = Process(pid, ppid, comm)
        if processes.get(ppid) == None:
            MISSING_PARENTS.add(ppid)
        if processes.get(ppid) != None:
            parent = processes.get(ppid)
            parent.childrens.append(new_process)
        processes[pid] = new_process
    return processes


def init():
    try:
        processes = scrap_processes()
        handle_late_parents(processes)
        print_processes(processes[normalize_pid_len(LAUNCHD_PID)], 0)
    except Exception as e:
        print("Exception occured", e)


def print_processes(ps, depth):
    if ps.pid in PRINTED_PROCESSES:
        return
    PRINTED_PROCESSES.add(ps.pid)
    space = " " * depth if depth > 0 else ""
    padding = space + "|__"

    print(f"{padding} pid: {ps.pid}  |  ppid: {ps.ppid}  |  comm: {ps.comm[-90:]}")

    for child in ps.childrens:
        print_processes(child, depth + 2)


if __name__ == "__main__":
    init()
