def is_brackets_matched(s: str) -> bool:
	"""判断字符串中的括号是否匹配。支持 () [] {} 三种类型。

	参数:
	- s: 输入字符串，非括号字符会被忽略。

	返回:
	- True 如果所有括号正确匹配且顺序合法，否则 False。
	"""
	pairs = {')': '(', ']': '[', '}': '{'}
	opening = set(pairs.values())
	stack = []
	for ch in s:
		if ch in opening:
			stack.append(ch)
		elif ch in pairs:
			if not stack or stack.pop() != pairs[ch]:
				return False
	return not stack


def _test():
	cases = [
		("()", True),
		("([]{})", True),
		("([)]", False),
		("", True),
		("abc(def)[ghi]{jkl}", True),
		("(((", False),
		("{[}", False),
	]
	for s, expected in cases:
		res = is_brackets_matched(s)
		print(f"{s!r}: {res} (expected {expected})")


if __name__ == '__main__':
	_test()

