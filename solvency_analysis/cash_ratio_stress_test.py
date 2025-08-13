# ==============================================
# 【现金比率压力测试计算器】v1.0
# 独特性：极端情景模拟 + 现金健康度四象限 + 行业危机阈值
# 开发者：Kiwi_hazel
# 公式：现金比率 =（货币资金 + 交易性金融资产）/ 流动负债
# ==============================================

def cash_ratio_stress_test(cash_eq, short_term_debt, daily_cash_burn, industry_type):
    """
    核心功能：评估极端情景下的短期偿债能力（现金比率+压力测试）
    :param cash_eq: 现金及等价物（万元）
    :param short_term_debt: 流动负债（万元）
    :param daily_cash_burn: 日均现金消耗（万元/天，如无收入时的运营成本）
    :param industry_type: 行业类型（重资产/轻资产/金融/服务业）
    """
    if cash_eq < 0 or short_term_debt < 0 or daily_cash_burn < 0:
        return {"error": "⚠️ 数据错误：现金/负债/日均消耗不可为负（例：现金=500万，负债=1000万）"}
    
    # 基础计算
    cash_ratio = round(cash_eq / short_term_debt, 2) if short_term_debt !=0 else float('inf')
    survival_days = round(cash_eq / daily_cash_burn, 1) if daily_cash_burn !=0 else float('inf')  # 现金储备天数
    
    # 点1：行业危机阈值（不同行业现金比率安全线不同）
    crisis_thresholds = {
        "重资产": {"ratio": 0.5, "days": 90},   # 如制造业，需更多现金应对设备维护
        "轻资产": {"ratio": 0.3, "days": 60},   # 如科技公司，现金消耗快但融资灵活
        "金融": {"ratio": 0.8, "days": 120},    # 如银行，需高流动性应对挤兑风险
        "服务业": {"ratio": 0.4, "days": 75}    # 如餐饮，依赖现金流周转
    }
    threshold = crisis_thresholds.get(industry_type, {"ratio": 0.5, "days": 90})  # 默认重资产
    
    # 点2：极端情景压力测试（模拟60天无收入）
    stress_cash_needed = daily_cash_burn * 60  # 60天现金需求
    stress_coverage = "✅ 覆盖" if cash_eq >= stress_cash_needed else f"❌ 缺口{round(stress_cash_needed - cash_eq,1)}万"
    
    # 点3：现金健康度四象限
    if cash_ratio >= threshold["ratio"] * 1.5 and survival_days >= threshold["days"] * 1.5:
        health_quadrant = "【安全区】"
        health_note = "现金储备充足，极端情景下仍有较高安全边际"
    elif cash_ratio >= threshold["ratio"] and survival_days >= threshold["days"]:
        health_quadrant = "【警惕区】"
        health_note = "现金基本健康，但需监控现金流变化，避免消耗过快"
    elif cash_ratio > 0 and survival_days > 0:
        health_quadrant = "【危险区】"
        health_note = "现金紧张！需加快应收账款回收或削减非必要支出"
    else:
        health_quadrant = "【危机区】"
        health_note = "现金耗尽风险！建议立即启动融资或资产变现"
    
    return {
        "cash_ratio": cash_ratio,
        "survival_days": survival_days,
        "stress_test": f"60天无收入压力测试：{stress_coverage}",
        "health_quadrant": health_quadrant,
        "health_note": health_note,
        "industry_threshold": f"{industry_type}安全线：现金比率≥{threshold['ratio']}，储备天数≥{threshold['days']}天"
    }

# ----------------------
# 极简交互（3步输入+战略输出）
# ----------------------
if __name__ == "__main__":
    print("\n===== 💸 现金比率压力测试计算器 =====")
    print("→ 独特功能：极端情景模拟 + 现金健康度四象限\n")
    
    # 3步输入（带行业特性提示）
    cash_eq = float(input("1. 现金及等价物（万元，含货币资金+交易性金融资产）："))
    short_term_debt = float(input("2. 流动负债总额（万元，含短期借款+应付账款）："))
    daily_cash_burn = float(input("3. 日均现金消耗（万元/天，无收入时的运营成本）："))
    industry_type = input("\n4. 行业类型（输入数字1-4）：\n1.重资产 2.轻资产 3.金融 4.服务业 → ")
    industry_map = {"1": "重资产", "2": "轻资产", "3": "金融", "4": "服务业"}
    industry_name = industry_map.get(industry_type, "重资产")
    
    # 计算+卡片式输出
    result = cash_ratio_stress_test(cash_eq, short_term_debt, daily_cash_burn, industry_name)
    print(f"\n{'='*50}")
    if "error" in result:
        print(result["error"])
    else:
        print(f"现金比率：{result['cash_ratio']}（现金/流动负债 → 越高短期偿债能力越强）")
        print(f"现金储备天数：{result['survival_days']}天（无收入时可维持运营的天数）")
        print(f"行业安全线：{result['industry_threshold']}\n")
        print(f"⚠️ 极端情景测试：{result['stress_test']}")
        print(f"🎯 现金健康度：{result['health_quadrant']}")
        print(f"💡 行动建议：{result['health_note']}")
    print(f"\n📌 关键逻辑：现金比率>行业安全线 → 短期偿债无虞；储备天数>60天 → 抗风险能力强")
    print("="*50)
 
