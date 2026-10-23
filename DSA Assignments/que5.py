"""
Question 5: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
  1. Open brackets must be closed by the same type of brackets.
  2. Open brackets must be closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same type.
"""


def is_valid(s: str) -> bool:
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    s1 = "()"
    print(f'Input: "{s1}" -> {is_valid(s1)}')

    s2 = "()[]{}"
    print(f'Input: "{s2}" -> {is_valid(s2)}')

    s3 = "(]"
    print(f'Input: "{s3}" -> {is_valid(s3)}')

    s4 = "{[()]}"
    print(f'Input: "{s4}" -> {is_valid(s4)}')

    s5 = "([)]"
    print(f'Input: "{s5}" -> {is_valid(s5)}')

    s6 = "((("
    print(f'Input: "{s6}" -> {is_valid(s6)}')

    s7 = ")"
    print(f'Input: "{s7}" -> {is_valid(s7)}')
