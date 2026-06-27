
def is_balanced(s: str) -> bool:
	"""判断字符串中的括号是否匹配。

	支持的括号类型：圆括号 `()`, 方括号 `[]`, 花括号 `{}`。
	忽略字符串中非括号字符，只检查括号的配对与嵌套顺序。

	算法：使用栈（list 模拟）记录遇到的左括号，遇到右括号时检查栈顶是否为对应左括号。

	复杂度：时间 O(n)，空间 O(n)，其中 n 为字符串长度。

	参数:
		s: 输入字符串（可以为空）

	返回:
		bool: 若所有括号正确配对且嵌套顺序合法则返回 True，否则返回 False。
	"""
	pairs = {')': '(', ']': '[', '}': '{'}
	open_set = set(pairs.values())
	stack = []
	for ch in s:
		if ch in open_set:
			stack.append(ch)
		elif ch in pairs:
			if not stack or stack[-1] != pairs[ch]:
				return False
			stack.pop()
	return not stack


if __name__ == '__main__':
	# 支持两种运行模式：
	#  - --demo : 打印若干示例及其结果
	#  - --test : 运行断言测试（若失败会抛出 AssertionError）
	import sys

	if len(sys.argv) > 1 and sys.argv[1] == '--demo':
		samples = [
			"()",
			"([{}])",
			"(]",
			"([)]",
			"a+(b*c)-{d/e}",
			"",
		]
		for t in samples:
			print(f"{t!r} -> {is_balanced(t)}")
	elif len(sys.argv) > 1 and sys.argv[1] == '--test':
		# 至少 6 个测试用例，覆盖正常、异常、边界情况
		assert is_balanced("()") is True
		assert is_balanced("()[]{}") is True
		assert is_balanced("([{}])") is True
		assert is_balanced("([)]") is False
		assert is_balanced("((()") is False
		assert is_balanced("a(b)c{d}e[f]g") is True
		assert is_balanced("") is True
		assert is_balanced("]") is False
		# 额外边界与混合用例
		assert is_balanced("{[()()]}") is True
		assert is_balanced("{[(])}") is False
		print("All tests passed.")
	else:
		# 默认行为：从 stdin 逐行读取并输出判断结果
		for line in sys.stdin:
			line = line.rstrip('\n')
			print(is_balanced(line))

