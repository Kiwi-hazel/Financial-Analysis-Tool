# Financial-Analysis-Tool
## 财务分析自动化工具包 
**一句话定位**：用Python实现从“短期偿债”到“价值创造”的全流程财务分析，内置战略解读和压力测试，零基础3分钟出结果。  

## ✨ 核心工具清单（4大分析模块）  
| **分析模块**       | 工具名称                          | 核心功能                          | **创新点**（区别于通用工具）                |  
|--------------------|-----------------------------------|-----------------------------------|---------------------------------------------|  
| **1. 偿债能力**   | `current_ratio_calculator.py`     | 流动比率+速动比率双算             | 行业安全值判断（制造业>2，服务业>1.5）       |  
|                    | `cash_ratio_stress_test.py`       | 现金比率压力测试                  | 极端情景模拟（60天无收入覆盖能力）+ 健康度四象限 |  
|                    | `interest_coverage_stress.py`     | 利息保障倍数测试                  | 衰退情景EBIT降30% + 债务风险四级预警          |  
| **2. 盈利能力**   | `roce_calculator.py`              | 资本回报率计算                    | 资本结构校验（股东权益+非流动负债）            |  
|                    | `dupont_analysis_strategic.py`    | ROE三因素分解                     | 战略类型判断（高利润/高周转/高杠杆企业）       |  
| **3. 运营效率**   | `inventory_turnover_days.py`      | 存货周转天数分析                  | 供应链健康度评分（A/B/C/D）+ 隐性成本估算     |  
| **4. 投资估值**   | `roi_ri_calculator.py`            | ROI+RI双指标联动分析              | 双指标矛盾提示（如“高ROI但低RI”）             |  
|                    | `pe_valuation_safety_margin.py`   | 市盈率安全边际分析                | 估值驱动因素拆分（增长预期vs风险溢价）         |  
|                    | `eva_economic_value_added.py`     | EVA价值创造评估                   | 价值创造分级（创造者/毁灭者/平庸者）           |  

## 🚀 3步上手使用   
### 第1步：下载代码  
```bash  
git clone https://github.com/Kiwi-hazel/Financial-Analysis-Tool.git  
``` 

### 第2步：安装依赖（仅2个工具需要）  
```bash  
pip install matplotlib  # 用于ROCE计算器的行业对比图  
```  
### 第3步：运行工具（以杜邦分析为例）
```bash   
cd Financial-Analysis-Tool  
python dupont_analysis_strategic.py   
```  

## 📊 案例：制造业企业综合分析  
1. **短期偿债能力**  
   - 工具：`current_ratio_calculator.py`  
   - 结果：流动比率=1.8（制造业安全值>2），速动比率=0.9（行业基准>1）  
   - 结论：短期偿债能力较弱，需关注存货变现速度  

2. **现金抗风险能力**  
   - 工具：`cash_ratio_stress_test.py`  
   - 情景测试：60天无收入情景下，现金缺口=120万元（健康度D级）  
   - 建议：增加200万短期借款补充现金储备  

 3.**资本盈利效率**  
   - 工具：` ROCE_calculator.py`  
   - 结果：ROCE=16%（行业基准15%），税前利润=800万元，资本总额=5000万元 
   - 优势：资本利用效率高于行业平均，依赖高毛利率（25% vs 行业20%）

 4.**综合改进方案**  
   - 运营端：用` inventory_turnover_days.py`优化存货周转（65天→45天）  
   - 融资端：发行300万3年期债券替换短期借款，降低利息费用（8%→5%）  

 
## 🔍 关于项目  
**作者**：Kiwi-hazel  
**定位**：财务+Python复合能力实践，通过自动化工具替代Excel手动计算，提升财务分析效率（3分钟完成传统1小时工作）  
**核心价值**：不仅是计算器，更是“财务分析方法论”的代码实现，覆盖从偿债能力到价值评估的全流程  
**开发说明**：项目开发过程中使用AI工具辅助代码优化和文档撰写，但核心财务逻辑（如杜邦分析战略类型判断、EVA价值创造分级）由人工设计并验证，确保专业准确性。  
 

## 📚 工具快速导航（4大分类）    
- [1. 偿债能力工具](https://github.com/Kiwi-hazel/Financial-Analysis-Tool/blob/main/solvency_analysis/)  
- [2. 盈利能力工具](https://github.com/Kiwi-hazel/Financial-Analysis-Tool/blob/main/profitability_analysis/)  
- [3. 运营效率工具](https://github.com/Kiwi-hazel/Financial-Analysis-Tool/blob/main/operation_efficiency/)  
- [4. 投资估值工具](https://github.com/Kiwi-hazel/Financial-Analysis-Tool/blob/main/investment_valuation/)  
 
