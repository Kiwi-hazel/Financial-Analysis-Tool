# ==============================================
# 【EVA战略价值计算器】v1.0
# 独特性：价值创造分级 + 资本成本动态调整 + 驱动因素拆分
# 开发者：Kiwi_hazel
# 公式：EVA = NOPAT - (资本总额 × WACC) → 真正的"经济利润"
# ==============================================

def calculate_eva_strategic(nopat, capital_employed, company_type, eva_last_year=None):
    """
    核心功能：计算EVA并评估企业价值创造能力
    :param nopat: 税后净营业利润（万元，=EBIT×(1-税率)，税率默认25%）
    :param capital_employed: 资本总额（万元，=股东权益+有息负债）
    :param company_type: 企业类型（国企/民企/外企）→ 动态调整WACC
    :param eva_last_year: 上年EVA（万元，可选，用于计算增长率）
    """
    # 基础数据校验
    if nopat <= 0 or capital_employed <= 0:
        return {"error": "⚠️ 数据错误：NOPAT和资本总额需>0（例：NOPAT=1000万，资本总额=8000万）"}
    
    # 点1：资本成本（WACC）动态调整（不同企业类型融资成本差异）
    wacc_baseline = {
        "国企": 5.5,    # 融资成本低（债券利率3-4%）
        "民企": 7.5,    # 融资成本高（债券利率5-6%）
        "外企": 6.5     # 国际融资渠道多，成本中等
    }
    wacc = wacc_baseline.get(company_type, 6.5) / 100  # 转为小数（如5.5% → 0.055）
    
    # 核心计算
    eva = round(nopat - (capital_employed * wacc), 2)
    eva_yield = round(eva / capital_employed * 100, 2)  # EVA资本收益率（%）
    
    # 点2：价值创造分级（战略定位）
    if eva > 0:
        if eva_last_year and (eva - eva_last_year)/eva_last_year > 0.1:
            value_level = "【价值创造者（高增长）】"
            level_note = "EVA为正且增速>10% → 企业在创造超额价值，可持续扩大投资"
        else:
            value_level = "【价值创造者（稳定型）】"
            level_note = "EVA为正但增速<10% → 价值创造能力稳定，需优化资本结构降低WACC"
    elif eva == 0:
        value_level = "【价值平庸者】"
        level_note = "EVA=0 → 刚好覆盖资本成本，未创造超额价值，需提升经营效率"
    else:
        value_level = "【价值毁灭者】"
        level_note = "EVA<0 → 资本成本高于回报，需紧急剥离低效率资产或改进经营"
    
    # 创新点3：EVA驱动因素拆分（管理改进方向）
    nopat_contribution = round(nopat / capital_employed * 100, 2)  # NOPAT资本收益率（%）
    cost_contribution = round(wacc * 100, 2)  # 资本成本率（%）
    driver_analysis = f"EVA驱动：{nopat_contribution}%（NOPAT收益率） - {cost_contribution}%（WACC） = {eva_yield}%（EVA收益率）"
    
    return {
        "eva": eva,
        "eva_yield": eva_yield,
        "wacc": round(wacc*100, 2),
        "value_level": value_level,
        "level_note": level_note,
        "driver_analysis": driver_analysis,
        "company_type": company_type
    }

# ----------------------
# 极简交互（战略型输出）
# ----------------------
if __name__ == "__main__":
    print("\n===== 🏆 EVA战略价值计算器 =====")
    print("→ 独特功能：价值创造分级 + 资本成本动态调整（国企/民企/外企差异）\n")
    
    # 输入（带战略提示）
    nopat = float(input("1. 税后净营业利润NOPAT（万元，=EBIT×0.75，例：1200 → 建议>资本总额×WACC）："))
    capital_employed = float(input("2. 资本总额（万元，=股东权益+有息负债，例：8000）："))
    company_type = input("3. 企业类型（输入数字1-3）：1.国企 2.民企 3.外企 → ")
    company_map = {"1": "国企", "2": "民企", "3": "外企"}
    company_name = company_map.get(company_type, "民企")
    eva_last_year = input("4. 上年EVA（万元，可选，例：1000 → 用于计算增长率，不填直接回车）：")
    eva_last_year = float(eva_last_year) if eva_last_year else None
    
    # 计算+卡片输出（战略型结果）
    result = calculate_eva_strategic(nopat, capital_employed, company_name, eva_last_year)
    print(f"\n{'='*50}")
    if "error" in result:
        print(result["error"])
    else:
        print(f"EVA（经济增加值）：{result['eva']}万元（真正的'经济利润'，非会计利润）")
        print(f"EVA收益率：{result['eva_yield']}%（=EVA/资本总额 → 衡量资本使用效率）")
        print(f"加权平均资本成本WACC：{result['wacc']}%（{result['company_type']}融资成本）\n")
        print(f"🎯 价值创造定位：{result['value_level']}")
        print(f"💡 战略解读：{result['level_note']}")
        print(f"🔍 驱动因素：{result['driver_analysis']}")
    print(f"\n📌 关键逻辑：EVA>0 → 企业创造的价值>资本成本 → 值得投资")
    print("="*50)
 
