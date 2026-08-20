class MinStack:

    def __init__(self):
        self.st = []
        self.mini = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.mini)>0:
            here = min(self.mini[-1],val)
            self.mini.append(here)
        else:
            self.mini.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mini[-1]
