# ==============================================
# ROCE资本回报率计算器（普适版）
# 功能：3步完成计算 | 财务公式标注 | 资本结构校验 | 结果卡片输出
# 开发者：Kiwi-hazel
# 特点：零基础友好 | 输入安全校验 | 比率意义解读
# ==============================================

def calculate_roce(operating_profit, capital_employed):
    """
    计算ROCE（资本回报率）
    公式来源：CFA一级教材P342（营业利润/资本总额）
    资本总额=总资产-流动负债=股东权益+非流动负债（会计恒等式转换）
    """
    # 财务数据校验
    if operating_profit <= 0:
        return f"⚠️ 营业利润需>0（当前输入：{operating_profit}万元），企业亏损状态下ROCE无意义"
    if capital_employed <= 0:
        return f"⚠️ 资本总额需>0（当前输入：{capital_employed}万元），资本是企业运营基础"
    if capital_employed < operating_profit:
        return f"⚠️ 资本总额异常（当前：{capital_employed}万元 < 营业利润：{operating_profit}万元），可能误将'净资产'输入为'资本总额'（资本总额通常为营业利润的5-10倍）"

    roce = (operating_profit / capital_employed) * 100
    return round(roce, 2)


def capital_structure_check(capital_employed, equity, debt):
    """
    【微创新点】资本结构健康度辅助判断
    逻辑：资本总额应≈股东权益+非流动负债（检验数据一致性）
    """
    if equity + debt == 0:
        return "→ 未提供权益/负债数据，跳过资本结构校验"
    # 允许±10%误差（财务数据四舍五入导致）
    if 0.9 * capital_employed <= (equity + debt) <= 1.1 * capital_employed:
        return "→ 资本结构健康：资本总额≈股东权益+非流动负债（数据一致）"
    else:
        return f"→ 注意：资本总额（{capital_employed}万）与权益+负债（{equity + debt}万）差异>10%，建议检查报表数据（可能流动负债计算错误）"


# ------------------------
# 主程序：3步极简交互
# ------------------------
if __name__ == "__main__":
    print("\n===== 🔄 ROCE资本回报率计算器（普适版） =====")
    print("→ 用途：衡量企业利用资本创造利润的效率（越高越好，通常>15%为健康）\n")

    # 【第1步：核心数据输入】（必填项，带单位示例）
    operating_profit = float(input("1. 营业利润（万元，例：5000 → 输入5000）："))
    capital_employed = float(input("2. 资本总额（万元，=总资产-流动负债，例：30000 → 输入30000）："))

    # 【第2步：行业选择】（提供参考基准，避免用户无方向）
    industry = input(
        "\n3. 所属行业（输入数字1-5）：\n1. 科技/互联网 | 2. 制造业 | 3. 零售/消费 | 4. 金融/银行 | 5. 能源/公用事业\n你的选择：")
    industry_map = {
        "1": ("科技/互联网", 20.0),  # 行业基准ROCE（%），参考Wind数据库2024年数据
        "2": ("制造业", 15.0),
        "3": ("零售/消费", 18.0),
        "4": ("金融/银行", 12.0),
        "5": ("能源/公用事业", 10.0)
    }
    industry_name, industry_benchmark = industry_map.get(industry, ("默认行业", 15.0))  # 兜底默认值

    # 【第3步：可选数据（提升准确性）】（非必填，按需输入）
    print("\n（可选）输入以下数据，进行资本结构健康度校验（不填直接按回车）")
    equity = input("4. 股东权益总额（万元，例：20000）：")
    debt = input("5. 非流动负债总额（万元，例：10000）：")
    # 处理可选数据（为空则跳过校验）
    equity = float(equity) if equity else 0
    debt = float(debt) if debt else 0

    # ------------------------
    # 计算+结果输出（卡片式展示，清晰易读）
    # ------------------------
    print("\n\n" + "=" * 50)
    print(f"📊 ROCE计算结果（{industry_name}）".center(50))
    print("=" * 50)
    # 1. 核心指标
    roce_result = calculate_roce(operating_profit, capital_employed)
    print(f"• 你的ROCE：{roce_result}%")
    print(f"• 行业基准：{industry_benchmark}%（2024年行业中位数）")
    # 2. 简单判断
    if isinstance(roce_result, float):  # 仅当计算成功时显示
        status = "✅ 优秀" if roce_result > industry_benchmark * 1.2 else \
            "👍 良好" if roce_result >= industry_benchmark else \
                "⚠️ 需关注" if roce_result > industry_benchmark * 0.8 else \
                    "❌ 较差"
        print(f"• 水平判断：{status}（高于行业{round((roce_result - industry_benchmark), 2)}个百分点）")
    # 3. 资本结构校验（微创新点）
    print(f"\n💡 资本结构辅助判断：{capital_structure_check(capital_employed, equity, debt)}")
    # 4. 使用提示（友好收尾）
    print("\n🔍 使用提示：ROCE=营业利润/资本总额，资本总额=总资产-流动负债（会计恒等式：=股东权益+非流动负债）")
    print("=" * 50)



