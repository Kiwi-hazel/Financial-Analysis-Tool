# ==============================================
# ROI&RI双指标计算器（投资决策专用）
# 功能：同时计算ROI（投资回报率）和RI（剩余收益），辅助项目投资决策
# 开发者：Kiwi_hazel
# 输入：项目收益、投资额、行业类型 → 输出双指标结果+联动分析
# ==============================================

def calculate_roi_ri(profit, investment, industry):
    """
    计算ROI和RI
    ROI = 项目收益 / 投资额 × 100%
    RI = 项目收益 - (投资额 × 资本成本率)
    资本成本率：根据行业风险自动匹配（参考2024年Wind行业数据）
    """
    # 1. 基础数据校验
    if profit <= 0:
        return {"error": f"⚠️ 项目收益需>0（当前：{profit}万元），亏损项目无需评估ROI/RI"}
    if investment <= 0:
        return {"error": f"⚠️ 投资额需>0（当前：{investment}万元），投资额为0意味着无风险"}
    
    # 2. 行业资本成本率
    industry_cost = {
        "高科技": 12.0,  # 高风险行业，资本成本高
        "制造业": 8.0,   # 中等风险
        "服务业": 6.5,   # 低风险
        "房地产": 10.0   # 政策敏感型，资本成本较高
    }
    cost_of_capital = industry_cost.get(industry, 8.0)  # 默认8%（全行业平均）
    
    # 3. 双指标计算
    roi = round((profit / investment) * 100, 2)
    ri = round(profit - (investment * cost_of_capital / 100), 2)  # RI=收益-资本成本
    
    # 4. 联动分析（核心价值：揭示单一指标局限性）
    analysis = ""
    if roi > cost_of_capital and ri > 0:
        analysis = "✅ 双指标达标：项目创造超额价值，建议投资（ROI高于资本成本，RI为正）"
    elif roi > cost_of_capital and ri <= 0:
        analysis = "⚠️ 注意矛盾：ROI达标但RI为负 → 可能因投资额过大，资本成本侵蚀利润（例：高ROI但低收益额）"
    elif roi <= cost_of_capital and ri > 0:
        analysis = "⚠️ 注意矛盾：ROI未达标但RI为正 → 可能因投资额过小，收益额足以覆盖资本成本（例：低ROI但高收益额）"
    else:
        analysis = "❌ 双指标不达标：项目未创造超额价值，不建议投资"
    
    return {
        "roi": roi,
        "ri": ri,
        "cost_of_capital": cost_of_capital,
        "analysis": analysis,
        "industry": industry
    }

# ------------------------
# 主程序：极简交互（3步输入）
# ------------------------
if __name__ == "__main__":
    print("\n===== 📈 ROI&RI双指标投资决策计算器 =====")
    print("→ 用途：评估项目是否创造超额价值（需同时参考ROI和RI，避免单一指标误导）\n")
    
    # 3步输入（带示例，降低使用门槛）
    profit = float(input("1. 项目年收益（万元，例：150 → 输入150）："))
    investment = float(input("2. 项目投资额（万元，例：1000 → 输入1000）："))
    industry = input("3. 所属行业（输入数字1-4）：\n1. 高科技 | 2. 制造业 | 3. 服务业 | 4. 房地产\n你的选择：")
    
    # 行业映射（数字转中文，避免输入错误）
    industry_map = {
        "1": "高科技", "2": "制造业", "3": "服务业", "4": "房地产"
    }
    industry_name = industry_map.get(industry, "制造业")  # 默认制造业
    
    # 计算+结果输出（卡片式展示，清晰易读）
    result = calculate_roi_ri(profit, investment, industry_name)
    print(f"\n{'='*50}")
    if "error" in result:
        print(result["error"])  # 显示错误提示
    else:
        print(f"📊 基础指标（{industry_name}行业）")
        print(f"• ROI（投资回报率）：{result['roi']}%")
        print(f"• 行业资本成本率：{result['cost_of_capital']}%")
        print(f"• RI（剩余收益）：{result['ri']}万元（= 收益 - 资本成本）\n")
        print(f"🔍 联动分析：{result['analysis']}")
    print(f"\n💡 决策逻辑：ROI>资本成本率且RI>0 → 项目创造超额价值")
    print("="*50)
 
