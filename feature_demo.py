"""
功能演示模块 - 在 feature 分支上创建
"""

def calculate_average(numbers):
    """
    计算一个列表的平均值
    
    参数:
        numbers: 数字列表，例如 [1, 2, 3, 4, 5]
    
    返回:
        平均值，例如 3.0
        如果列表为空，返回 0
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# 测试代码（可以直接运行测试）
if __name__ == "__main__":
    test_list = [10, 20, 30, 40, 50]
    result = calculate_average(test_list)
    print(f"列表 {test_list} 的平均值是: {result}")
    
    # 测试空列表
    empty_list = []
    print(f"空列表的平均值是: {calculate_average(empty_list)}")
