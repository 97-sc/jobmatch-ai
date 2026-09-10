MATCH_PROMPT = """你是一位资深招聘顾问。根据【职位描述】和【简历】评估匹配度。
【职位描述】
{jd}
【简历】
{resume}
严格只输出符合 schema 的 JSON，不要任何额外文字。
score: 0-100 的整数整体匹配度。
matched_skills: 简历已具备且 JD 要求的技能列表。
missing_skills: JD 要求但简历缺失的技能列表。
suggestions: 3-5 条针对该简历的具体改进建议。"""

COVER_PROMPT = """你是求职信写作助手。基于【职位描述】和【简历】及【匹配分析】，写一封专业、简洁、个性化的中文求职信。
【职位描述】
{jd}
【简历】
{resume}
【匹配分析】
{analysis}
只输出求职信正文，不要额外解释。"""
