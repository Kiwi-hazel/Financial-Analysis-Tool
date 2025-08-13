# ==============================================
# 【利息保障倍数压力测试计算器】v1.0
# 独特性：衰退情景测试 + 债务风险预警分级 + 利息结构分析
# 开发者：Kiwi_hazel
# 公式：利息保障倍数 = EBIT / 利息费用 → 衡量"利润覆盖利息"能力
# ==============================================

def interest_coverage_stress(ebit, interest_expense, short_term_interest=None, industry_cycle=None):
    """
    核心功能：评估利息覆盖能力及衰退情景下的抗风险能力
    :param ebit: 息税前利润（万元，如：500 → 利润表"EBIT"项）
    :param interest_expense: 利息费用总额（万元，含短期+长期利息）
    :param short_term_interest: 短期利息费用（万元，可选，用于结构分析）
    :param industry_cycle: 行业周期性（强周期/弱周期/防御性）→ 衰退情景调整
    """
    # 基础数据校验（避免除零或负数）
    if ebit <= 0 or interest_expense <= 0:
        return {"error": "⚠️ 数据错误：EBIT和利息费用需>0（例：EBIT=500万，利息=100万 → 倍数=5倍）"}
    
    # 基础计算：正常情景利息保障倍数
    interest_coverage = round(ebit / interest_expense, 2)
    
    # ----------------------
    # 点1：衰退情景压力测试（经济下行冲击）
    # ----------------------
    # 根据行业周期性调整EBIT下降比例（强周期行业衰退时利润降幅更大）
    cycle_adjustment = {
        "强周期": 0.3,    # 如钢铁/房地产，衰退期EBIT降30%
        "弱周期": 0.15,   # 如家电/消费，衰退期EBIT降15%
        "防御性": 0.1     # 如医药/公用事业，衰退期EBIT降10%
    }
    ebit_drop_ratio = cycle_adjustment.get(industry_cycle, 0.2)  # 默认衰退情景EBIT降20%
    stress_ebit = ebit * (1 - ebit_drop_ratio)  # 衰退情景下的EBIT
    stress_coverage = round(stress_ebit / interest_expense, 2) if stress_ebit > 0 else 0  # 衰退情景倍数
    
    # ----------------------
    # 点2：债务风险预警分级（四级预警体系）
    # ----------------------
    if interest_coverage >= 5 and stress_coverage >= 3:
        risk_level = "【安全级】"
        risk_note = "利息覆盖充足，衰退情景下仍安全（强周期行业首选标准）"
    elif interest_coverage >= 3 and stress_coverage >= 2:
        risk_level = "【关注级】"
        risk_note = "正常情景安全，但衰退情景下需监控EBIT变化（弱周期行业可接受）"
    elif interest_coverage >= 2 and stress_coverage > 1:
        risk_level = "【风险级】"
        risk_note = "利息覆盖薄弱，需控制债务规模（避免新增高息融资）"
    else:
        risk_level = "【高危级】"
        risk_note = "利息无法覆盖，存在违约风险（需立即债务重组或增加EBIT）"
    
    # ----------------------
    # 点3：利息结构分析（短期偿债压力）
    # ----------------------
    structure_analysis = "（未提供短期利息数据，无法分析结构）"
    if short_term_interest and interest_expense > 0:
        short_term_ratio = round(short_term_interest / interest_expense * 100, 1)  # 短期利息占比（%）
        structure_analysis = f"短期利息占比{short_term_ratio}% → {'⚠️ 短期偿债压力大（建议优先偿还）' if short_term_ratio > 60 else '短期压力可控（结构健康）'}"
    
    return {
        "normal_coverage": interest_coverage,          # 正常情景倍数
        "stress_coverage": stress_coverage,            # 衰退情景倍数
        "ebit_drop": round(ebit_drop_ratio * 100, 1),  # EBIT下降比例（%）
        "risk_level": risk_level,                      # 风险等级（安全/关注/风险/高危）
        "risk_note": risk_note,                        # 风险解读
        "structure_analysis": structure_analysis,      # 利息结构分析
        "industry_cycle": industry_cycle or "中性行业"  # 行业周期性
    }

# ----------------------
# 极简交互界面
# ----------------------
if __name__ == "__main__":
    print("\n===== ⚠️ 利息保障倍数压力测试计算器 =====")
    print("→ 独特功能：衰退情景测试（模拟经济下行）+ 债务风险四级预警 + 利息结构分析\n")
    
    # 核心数据输入（带财务提示）
    ebit = float(input("1. 息税前利润EBIT（万元，例：500 → 利润表'营业利润+利息费用'）："))
    interest_expense = float(input("2. 利息费用总额（万元，例：100 → 含短期借款+长期借款利息）："))
    short_term_interest = input("3. 短期利息费用（万元，可选，例：60 → 不填直接回车）：")
    short_term_interest = float(short_term_interest) if short_term_interest else None
    
    # 行业周期性选择（影响衰退情景模拟）
    industry_cycle = input("\n4. 行业周期性（输入数字1-3）：1.强周期 2.弱周期 3.防御性 → ")
    cycle_map = {"1": "强周期", "2": "弱周期", "3": "防御性"}
    industry_name = cycle_map.get(industry_cycle, "中性行业")
    
    # 计算+输出结果（卡片式展示，突出关键结论）
    result = interest_coverage_stress(ebit, interest_expense, short_term_interest, industry_name)
    print(f"\n{'='*50}")
    if "error" in result:
        print(result["error"])  # 数据错误提示
    else:
        print(f"📊 核心指标：")
        print(f"   正常情景利息保障倍数：{result['normal_coverage']}倍（EBIT/利息费用）")
        print(f"   衰退情景测试（{result['industry_cycle']}，EBIT降{result['ebit_drop']}%）：{result['stress_coverage']}倍\n")
        
        print(f"🚨 债务风险等级：{result['risk_level']}")
        print(f"💡 风险解读：{result['risk_note']}\n")
        
        print(f"🔍 利息结构分析：{result['structure_analysis']}")
    
    print(f"\n📌 安全标准参考：")
    print("   - 强周期行业：正常>5倍，衰退>3倍 | 弱周期行业：正常>3倍，衰退>2倍")
    print("   - 短期利息占比<60% → 利息结构健康（避免集中偿付压力）")
    print("="*50)
 
