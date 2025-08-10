# ==============================================
# 【存货周转天数精细化计算器】v1.0
# 独特性：供应链健康度评分 + 隐性成本提示 + 细分行业对标
# 开发者：Kiwi_hazel
# 公式：存货周转率=营业成本/平均存货；周转天数=365/周转率
# ==============================================

def calculate_inventory_health(cogs, avg_inventory, industry_subtype):
    """
    核心功能：计算存货周转效率并评估供应链健康度
    :param industry_subtype: 细分行业（快消品/耐用品/奢侈品/制造业）
    """
    if cogs <= 0 or avg_inventory <= 0:
        return {"error": "⚠️ 数据错误：营业成本和平均存货需>0（例：营业成本=1000万，存货=200万）"}
    
    # 基础计算
    turnover_rate = round(cogs / avg_inventory, 2)  # 周转率（次/年）
    turnover_days = round(365 / turnover_rate, 1)   # 周转天数（天/次）
    
    # 点1：细分行业标准
    industry_standards = {
        "快消品": {"优秀": 30, "良好": 45, "警戒": 60},  # 如食品饮料
        "耐用品": {"优秀": 60, "良好": 90, "警戒": 120},  # 如家电
        "奢侈品": {"优秀": 90, "良好": 150, "警戒": 200}, # 如高端服装
        "制造业": {"优秀": 60, "良好": 90, "警戒": 150}   # 如汽车零部件
    }
    std = industry_standards.get(industry_subtype, industry_standards["制造业"])
    
    # 点2：供应链健康度评分（A/B/C/D）
    if turnover_days <= std["优秀"]:
        health_score = "A（优秀）"
        health_note = "供应链高效，存货变现快，资金占用少"
    elif turnover_days <= std["良好"]:
        health_score = "B（良好）"
        health_note = "周转正常，可优化采购计划降低存货水平"
    elif turnover_days <= std["警戒"]:
        health_score = "C（警戒）"
        health_note = "周转偏慢，可能存在滞销风险，建议促销清库存"
    else:
        health_score = "D（危险）"
        health_note = "严重积压！需紧急分析存货结构，处理呆滞库存"
    
    # 点3：隐性成本提示（资金占用成本）
    hidden_cost = round(avg_inventory * 0.05 * (turnover_days / std["良好"] - 1), 2)
    hidden_note = f"隐性成本：较良好水平多占用资金成本约{hidden_cost}万元（按年利率5%估算）" if hidden_cost > 0 else "无额外隐性成本"
    
    return {
        "turnover_rate": turnover_rate,
        "turnover_days": turnover_days,
        "industry_subtype": industry_subtype,
        "health_score": health_score,
        "health_note": health_note,
        "hidden_cost_note": hidden_note
    }

# ----------------------
# 极简交互（3步输入+卡片输出）
# ----------------------
if __name__ == "__main__":
    print("\n===== 📦 存货周转天数精细化计算器 =====")
    print("→ 独特功能：供应链健康度评分 + 隐性成本提示\n")
    
    # 输入（带细分行业示例）
    cogs = float(input("1. 营业成本（万元，例：快消品=8000 → 存货成本）："))
    avg_inventory = float(input("2. 平均存货（万元，例：快消品=1000 → 期初+期末存货/2）："))
    print("\n3. 细分行业（输入数字1-4）：")
    industry_subtype = input("   1.快消品 2.耐用品 3.奢侈品 4.制造业 → ")
    subtype_map = {"1": "快消品", "2": "耐用品", "3": "奢侈品", "4": "制造业"}
    subtype_name = subtype_map.get(industry_subtype, "制造业")
    
    # 计算+输出
    result = calculate_inventory_health(cogs, avg_inventory, subtype_name)
    print(f"\n{'='*50}")
    if "error" in result:
        print(result["error"])
    else:
        print(f"存货周转率：{result['turnover_rate']}次/年（越高越好）")
        print(f"存货周转天数：{result['turnover_days']}天/次（越短越好）")
        print(f"细分行业：{result['industry_subtype']}（优秀标准：<{industry_standards[subtype_name]['优秀']}天）\n")
        print(f"🏥 供应链健康度：{result['health_score']}")
        print(f"📝 改善建议：{result['health_note']}")
        print(f"💰 {result['hidden_cost_note']}")
    print(f"\n💡 关键逻辑：周转天数=365/周转率 → 短天数=快变现=少资金占用")
    print("="*50)
 
