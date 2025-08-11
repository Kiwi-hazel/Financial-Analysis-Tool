# ==============================================
# 【市盈率安全边际计算器】v1.0
# 独特性：安全边际测算 + 估值驱动因素分析 + 动态PE修正
# 开发者：Kiwi_hazel
# 公式：静态PE=当前股价/最近12个月EPS；动态PE=当前股价/未来12个月预测EPS
# ==============================================

def calculate_pe_safety_margin(stock_price, eps_ttm, eps_forecast, industry_pe, historical_pe_75th):
    """
    核心功能：评估市盈率合理性及安全边际
    :param eps_ttm: 最近12个月EPS（元/股）
    :param eps_forecast: 未来3年预测EPS年均增速（%，如15=年均增长15%）
    :param industry_pe: 行业平均PE（静态）
    :param historical_pe_75th: 公司历史75分位PE（近5年）
    """
    if stock_price <= 0 or eps_ttm <= 0 or industry_pe <= 0 or historical_pe_75th <= 0:
        return {"error": "⚠️ 数据错误：股价/EPS/行业PE需>0（例：股价=50元，EPS=2元 → PE=25倍）"}
    
    # 基础计算
    pe_static = round(stock_price / eps_ttm, 2)  # 静态PE（当前估值）
    pe_dynamic = round(pe_static / (1 + eps_forecast/100), 2) if eps_forecast != -100 else float('inf')  # 动态PE（考虑增长）
    
    # 点1：安全边际测算（当前PE vs 安全PE上限）
    safety_pe_upper = min(industry_pe * 1.2, historical_pe_75th)  # 安全PE上限=行业PE*1.2和历史75分位PE的最小值
    safety_margin = round((safety_pe_upper - pe_static) / pe_static * 100, 1)  # 安全边际（%）
    margin_status = "✅ 低估" if safety_margin > 20 else \
                    "⚠️ 合理" if safety_margin >= -10 else \
                    "❌ 高估"
    
    # 点2：估值驱动因素分析
    if pe_static > industry_pe * 1.5:
        if eps_forecast > industry_pe * 0.5:  # 假设行业平均增速=行业PE*0.5（简化逻辑）
            driver = "【高增长预期驱动】"
            driver_note = "PE高于行业因市场预期未来盈利高增长（需验证增速能否兑现）"
        else:
            driver = "【风险溢价过高驱动】"
            driver_note = "PE高于行业但增速无支撑，可能存在估值泡沫或流动性溢价"
    elif pe_static < industry_pe * 0.8:
        driver = "【低增长预期驱动】"
        driver_note = "PE低于行业可能因盈利增速放缓或风险担忧（需分析基本面是否恶化）"
    else: driver = "【行业均衡驱动】" ; driver_note = "PE与行业匹配，估值逻辑合理无明显偏离"
    
    return {
        "pe_static": pe_static,
        "pe_dynamic": pe_dynamic,
        "safety_margin": safety_margin,
        "margin_status": margin_status,
        "driver": driver,
        "driver_note": driver_note,
        "safety_pe_upper": round(safety_pe_upper, 2)
    }

# ----------------------
# 极简交互（3步输入+战略输出）
# ----------------------
if __name__ == "__main__":
    print("\n===== 📈 市盈率安全边际计算器 =====")
    print("→ 独特功能：估值安全边际测算 + 驱动因素分析（避免盲目追高/杀跌）\n")
    
    # 输入（带数据来源提示）
    stock_price = float(input("1. 当前股价（元/股，例：60 → 来源：股票软件实时价）："))
    eps_ttm = float(input("2. 最近12个月EPS（元/股，例：2.5 → 来源：财报'基本每股收益'）："))
    industry_pe = float(input("3. 行业平均静态PE（倍，例：25 → 来源：Wind/同花顺行业数据）："))
    historical_pe_75th = float(input("4. 公司历史75分位PE（倍，例：30 → 近5年PE的75%分位数）："))
    eps_forecast = float(input("5. 未来3年预测EPS增速（%，例：15 → 机构一致预期）："))
    
    # 计算+卡片式输出
    result = calculate_pe_safety_margin(stock_price, eps_ttm, eps_forecast, industry_pe, historical_pe_75th)
    print(f"\n{'='*50}")
    if "error" in result:
        print(result["error"])
    else:
        print(f"静态PE（当前估值）：{result['pe_static']}倍")
        print(f"动态PE（考虑增长）：{result['pe_dynamic']}倍（=静态PE/(1+增速)）\n")
        print(f"安全边际分析：{result['margin_status']}（安全边际={result['safety_margin']}%，安全PE上限={result['safety_pe_upper']}倍）")
        print(f"估值驱动因素：{result['driver']}")
        print(f"💡 核心结论：{result['driver_note']}")
    print(f"\n📌 安全边际逻辑：安全边际>20% → 股价被低估；< -10% → 高估需警惕")
    print("="*50)
 
