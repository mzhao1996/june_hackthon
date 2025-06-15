def get_product_analysis_prompt(product_list: str) -> str:
    """
    Generate a prompt for analyzing product lists with specific requirements
    """
    prompt = f"""
作为一个专业的商品分析专家，请分析以下商品列表数据。这是一个来自Amazon的商品列表，可能包含best sellers、new releases或热搜商品。

商品列表：
{product_list}

请按照以下要求进行分析：

1. 数据清洗：
   - 排除以下类别的商品：
     * 敏感货物（书籍、食品、药物等）
     * IP保护商品（如迪士尼相关产品）
     * 重货（家具等大件物品）
     * 抛货（重量极轻的商品）
     * 政治相关商品
     * 节庆用品
     * 含电池的商品

2. 重复商品分析：
   - 识别在不同榜单中重复出现的商品（忽略品牌差异，关注商品本质）
   - 分析这些商品的共同特征和属性
   - 计算重复出现的频率
   - 按商品类别（如床单、水杯等）进行分组统计
   - 总结重复商品的主要类别：
     * 家居用品（如床单、枕头、毛巾等）
     * 厨房用品（如锅具、餐具、水杯等）
     * 个人护理（如护肤品、美妆工具等）
     * 电子产品配件（如手机壳、充电器等）
     * 运动健身（如瑜伽垫、运动器材等）
     * 办公用品（如笔记本、文具等）

3. 地域文化分析：
   - 结合加拿大当地天气特点
   - 考虑地理环境因素
   - 分析加拿大文化特征
   - 研究当地消费习惯

4. 输出要求：
   - 使用中文输出分析结果
   - 包含以下部分：
     * 数据概览（总商品数、有效商品数等）
     * 重复商品列表及分析
     * 地域文化影响分析
     * 市场趋势总结
     * 建议和洞察

请确保分析结果：
1. 客观准确
2. 数据驱动
3. 具有实际参考价值
4. 符合加拿大市场特点
"""
    return prompt

def get_product_analysis_tool(product_list: str) -> str:
    """
    Tool function to analyze product list
    """
    prompt = get_product_analysis_prompt(product_list)
    # 这里可以添加实际的AI调用逻辑
    return prompt 