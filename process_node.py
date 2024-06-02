class Process:
    def __init__(self, pid, ppid, comm):
        self.pid = pid
        self.ppid = ppid
        self.comm = comm
        self.childrens = []

    def __str__(self):
        return f"pid: {self.pid} | ppid: {self.ppid} | childrens: {list(map(lambda x: (x.pid, x.ppid), self.childrens))} | comm: {self.comm}"


if __name__ == "__main__":
    print("Process")
    ps = Process(2, 1, "test")
    print(ps)
