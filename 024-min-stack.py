class MinStack:

    def __init__(self):
        self.__stk = []
        self.__mins = []
        

    def push(self, val: int) -> None:
        self.__update_mins(val)
        self.__stk.append(val)


    def pop(self) -> None:
        self.__stk.pop()
        self.__mins.pop()


    def top(self) -> int:
        if not self.__is_empty(): return self.__stk[-1]
        raise IndexError("top from empty MinStack")
        

    def getMin(self) -> int:
        if not self.__is_empty(): return self.__mins[-1]
        raise IndexError("getMin from empty MinStack")


    def __is_empty(self) -> bool:
        return len(self.__stk) == 0


    def __update_mins(self, val: int) -> None:
        last_min = float('inf')
        if not self.__is_empty():
            last_min = self.__mins[-1]
        self.__mins.append(min(last_min, val))

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
