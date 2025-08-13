# ==============================================
# 【利息保障倍数压力测试计算器】v1.0
# 独特性：衰退情景测试 + 债务风险预警分级 + 利息结构分析
# 开发者：Kiwi_hazel
# 公式：利息保障倍数 = EBIT / 利息费用 → 衡量"利润覆盖利息"能力
# ==============================================

def interest_coverage_stress(ebit, interest_expense, short_term_interest=None, industry_cycle=None):
    """
    核心功能：评估利息覆盖能力及衰退情景下的抗风险能力
    :param short_term_interest: 短期利息费用（万元，可选，用于结构分析）
    :param industry_cycle: 行业周期性（强周期/弱周期/防御性）→ 衰退情景调整
    """
    if ebit <= 0 or interest_expense <= 0:
        return {"error": "⚠️ 数据错误：EBIT和利息费用需>0（例：EBIT=500万，利息=100万 → 倍数=5倍）"}
    
    # 基础计算
    interest_coverage = round(ebit / interest_expense, 2)
    
    # 点1：衰退情景压力测试（经济下行30% EBIT冲击）
    cycle_adjustment = {"强周期": 0.3, "弱周期": 0.15, "防御性": 0.1}  # EBIT下降比例
    ebit_drop = cycle_adjustment.get(industry_cycle, 0.2)  # 默认衰退情景EBIT下降20%
    stress_ebit = ebit * (1 - ebit_drop)
    stress_coverage = round(stress_ebit / interest_expense, 2) if stress_ebit >0 else 0
    
    # 点2：债务风险预警分级（四级预警）
    if interest_coverage >= 5 and stress_coverage >= 3:
        risk_level = "【安全级】"
        risk_note = "利息覆盖充足，衰退情景下仍安全（强周期行业首选）"
    elif interest_coverage >= 3 and stress_coverage >= 2:
        risk_level = "【关注级】"
        risk_note = "正常情景安全，但衰退情景下需监控EBIT变化（弱周期行业可接受）"
    elif interest_coverage >= 2 and stress_coverage > 1:
        risk_level = "【风险级】"
        risk_note = "利息覆盖薄弱，需控制债务规模（避免高息融资）"
    else:
        risk_level = "【高危级】"
        risk_note = "利息无法覆盖，存在违约风险（需立即债务重组或增加EBIT）"
    
    # 点3：利息结构分析（短期偿债压力）
    structure_analysis = "（未提供短期利息数据）"
    if short_term_interest and interest_expense >0:
        short_term_ratio = round(short_term_interest / interest_expense * 100, 1)
        structure_analysis = f"短期利息占比{short_term_ratio}% → {'⚠️ 短期压力大' if short_term_ratio>60 else '短期压力可控'}"
    
    return {
        "coverage_normal": interest_coverage,
        "coverage_stress": stress_coverage,
        "ebit_drop": round(ebit_drop*100, 1),
        "risk_level": risk_level,
        "risk_note": risk_note,
        "structure_analysis": structure_analysis,
        "industry_cycle": industry_cycle or "中性"
    }

# ----------------------
# 极简交互（风险型输出）
# ----------------------
if __name__ == "__main__":
    print("\n===== ⚠️ 利息保障倍数压力测试计算器 =====")
    print("→ 独特功能：衰退情景测试（EBIT降30%）+ 债务风险四级预警\n")
    
    # 输入（带风险提示）
    ebit = float(input("1. 息税前利润EBIT（万元，例：800 → 强周期行业建议>利息5倍）："))
    interest_expense = float(input("2. 利息费用总额（万元，例：150 → 含短期+长期利息）："))
    short_term_interest = input("3. 短期利息费用（万元，可选，例：100 → 不填直接回车）：")
    short_term_interest = float(short_term_interest) if short_term_interest else None
    industry_cycle = input("\n4. 行业周期性（输入数字1-3）：1.强周期 2.弱周期 3.防御性 → ")
    cycle_map = {"1": "强周期", "2": "弱周期", "3": "防御性"}
    cycle_name = cycle_map.get(industry_cycle, "中性")
    
    # 计算+卡片输出（风险型结果）
    result = interest_coverage_stress(ebit, interest_expense, short_term_interest, cycle_name)
    print(f"\n{'='*50}")
    if "error" in result:
        print(result["error"])
    else:
        print(f"正常情景利息保障倍数：{result['coverage_normal']}倍（EBIT/利息费用）")
        print(f"衰退情景测试（{cycle_name}行业，EBIT降{result['ebit_drop']}%）：{result['coverage_stress']}倍\n")
        print(f"🎯 债务风险等级：{result['risk_level']}")
        print(f"💡 风险解读：{result['risk_note']}")
        print(f"📊 利息结构：{result['structure_analysis']}")
    print(f"\n📌 安全标准：正常情景>5倍，衰退情景>3倍 → 抗风险能力强")
    print("="*50)
 
