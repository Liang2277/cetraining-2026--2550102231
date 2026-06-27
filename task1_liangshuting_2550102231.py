def is_bracket_match(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    print(is_bracket_match("(a+b)"))
    print(is_bracket_match("([{}])"))
    print(is_bracket_match("(]"))
