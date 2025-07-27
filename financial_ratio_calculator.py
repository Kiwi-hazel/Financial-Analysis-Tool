 # ========================
# 财务比率计算器（零基础安全版） v1.0
# 功能：输入流动资产/速动资产和流动负债，自动计算流动比率/速动比率
# 开发者：Kiwi-hazel（https://github.com/Kiwi-hazel）
# 特点：零基础友好 | 输入安全校验 | 比率意义解读 | 行业适配建议
# ========================
# ------------------------
# 1. 定义计算函数（新增速动比率函数，保持格式统一）
# ------------------------
def calculate_current_ratio(current_assets, current_liabilities):
    """计算流动比率（通用公式：流动资产/流动负债）"""
    # 安全校验：避免除数为0或负数（财务数据不可能为负）
    if current_liabilities <= 0 or current_assets < 0:
        return "⚠️ 输入错误：资产/负债不能为负数或零（流动负债需>0）"
    ratio = current_assets / current_liabilities
    return round(ratio, 2)  # 保留2位小数

def calculate_quick_ratio(quick_assets, current_liabilities):
    """计算速动比率（定制公式：速动资产/流动负债，速动资产=流动资产-存货-预付费用）"""
    # 安全校验（与流动比率共用逻辑，增强代码复用）
    if current_liabilities <= 0 or quick_assets < 0:
        return "⚠️ 输入错误：资产/负债不能为负数或零（流动负债需>0）"
    ratio = quick_assets / current_liabilities
    return round(ratio, 2)


# ------------------------
# 2. 手动输入测试数据（定制交互：先解释，再输入，零基础友好）
# ------------------------
print("\n===== 财务比率计算器（零基础安全版） =====")
print("📌 什么是流动比率/速动比率？")
print("   流动比率 = 流动资产 / 流动负债 → 衡量短期偿债能力（含存货等慢速变现资产）")
print("   速动比率 = 速动资产 / 流动负债 → 衡量立即偿债能力（剔除存货，仅保留现金/应收账款等）")
print("   安全提示：输入数据应为正数，流动负债不可为0（企业不可能无负债却有资产）\n")

# 让用户选择计算模式（用"数字+中文"引导，更直观）
mode = input("请选择计算模式（输入数字1或2）：\n1. 计算流动比率\n2. 计算速动比率\n你的选择：")

# 根据选择获取输入（流动负债为共用数据，先统一输入）
current_liabilities = float(input("\n请输入流动负债总额（万元，例如：500）："))

if mode == "1":
    # 流动比率输入（保持原变量名assets，与你原有代码统一）
    assets = float(input("请输入流动资产总额（万元，例如：1200）："))
    result = calculate_current_ratio(assets, current_liabilities)
    ratio_name = "流动比率"
    # 定制化解读（比通用"大于2为好"更详细，增加"行业差异"提示，体现独特性）
   解读 = "（传统安全值>2，实际需结合行业：制造业可能需更高，服务业可略低）"
elif mode == "2":
    # 速动比率输入（新增变量名quick_assets，明确区分）
    quick_assets = float(input("请输入速动资产总额（万元，=流动资产-存货，例如：800）："))
    result = calculate_quick_ratio(quick_assets, current_liabilities)
    ratio_name = "速动比率"
    解读 = "（传统安全值>1，现金充裕型企业可更高，如金融行业；重存货企业可能偏低）"
else:
    result = "❌ 输入错误"
    解读 = "（请重新运行程序，选择1或2）"


# ------------------------
# 3. 调用计算并打印结果
# ------------------------
print(f"\n{'='*20}")
print(f"📊 计算结果：{ratio_name} = {result}")
if isinstance(result, float):  # 仅当计算成功时显示解读和建议
    print(f"📝 比率解读：{解读}")
    # 安全提示：结合你的"零基础"定位，用更口语化的建议替代生硬判断
    if ratio_name == "流动比率":
        if result > 2.5:
            print("💡 建议：比率较高，可能存在资金闲置，可优化资产结构（如增加投资）")
        elif result < 1.5:
            print("💡 建议：比率较低，需确保短期现金流充足，避免偿债压力")
        else:
            print("💡 建议：比率在合理范围，关注流动资产内部结构（如存货周转率）")
    else:  # 速动比率
        if result > 1.5:
            print("💡 建议：立即偿债能力强，现金储备充足，可考虑短期理财提升收益")
        elif result < 0.8:
            print("💡 建议：速动资产不足，需优先收回应收账款或补充现金")
        else:
            print("💡 建议：速动资产健康，注意应收账款回收周期（避免坏账风险）")
print(f"{'='*20}\n")
 
