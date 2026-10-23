"""
Question 4: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum
element — all in constant time O(1).
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    min_stack = MinStack()

    min_stack.push(-2)
    print("push(-2)")

    min_stack.push(0)
    print("push(0)")

    min_stack.push(-3)
    print("push(-3)")

    print(f"get_min() -> {min_stack.get_min()}")

    min_stack.pop()
    print("pop()")

    print(f"top()     -> {min_stack.top()}")

    print(f"get_min() -> {min_stack.get_min()}")

    print()

    ms2 = MinStack()
    ms2.push(5)
    ms2.push(3)
    ms2.push(7)
    ms2.push(1)
    print("push(5), push(3), push(7), push(1)")
    print(f"get_min() -> {ms2.get_min()}")
    ms2.pop()
    print(f"After pop(), get_min() -> {ms2.get_min()}")
    ms2.pop()
    print(f"After pop(), get_min() -> {ms2.get_min()}")
