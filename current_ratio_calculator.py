# ====================
# 财务比率计算器（零基础安全版）
# 功能：输入流动资产和流动负债，自动计算流动比率
# 开发者：Kiwi-hazel
# ====================

# 1. 定义计算函数
def calculate_current_ratio(current_assets, current_liabilities):
    """
    计算流动比率
    公式：流动比率 = 流动资产 / 流动负债
    """
    ratio = current_assets / current_liabilities
    return round(ratio, 2)  # 保留2位小数

# 2. 手动输入测试数据（避免文件冲突）
print("=== 流动比率计算器 ===")
assets = float(input("请输入流动资产总额（万元）："))
liabilities = float(input("请输入流动负债总额（万元）："))

# 3. 调用计算并打印结果
result = calculate_current_ratio(assets, liabilities)
print(f"\n✅ 计算结果：流动比率 = {result}")
if result > 2:
    print("（提示：该企业短期偿债能力良好）")
else:
    print("（提示：需关注短期偿债风险）")