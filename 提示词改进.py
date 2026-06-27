def is_balanced(s: str) -> bool:
    """判断字符串中的括号是否匹配。

    使用栈来记录遇到的左括号，遇到右括号时检查是否与栈顶匹配。
    非括号字符会被忽略。

    Args:
        s: 需要检查的字符串。

    Returns:
        如果括号整体匹配，则返回 True；否则返回 False。
    """
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
    # 完整测试代码
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("([{}])", True),
        ("([)]", False),
        (("((()"), False),
        ("a(b)c{d}e[f]g", True),
        ("", True),
        ("]", False),
    ]

    for s, expected in test_cases:
        result = is_balanced(s)
        assert result == expected, f"{s!r}: expected {expected}, got {result}"

    print("所有测试通过")
