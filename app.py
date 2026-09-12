import streamlit as st
from core.matcher import analyze
from core.cover_letter import generate_cover_letter

st.set_page_config(page_title="AI 求职助手 JobMatch AI")
st.title("🤖 AI 求职助手 · JobMatch AI")
st.caption("本地大模型驱动 · 数据不出本机")

jd = st.text_area("① 粘贴职位描述 (JD)", height=200)
resume = st.text_area("② 粘贴你的简历内容", height=200)

if st.button("开始分析") and jd.strip() and resume.strip():
    with st.spinner("AI 分析中..."):
        result = analyze(jd, resume)
    st.subheader(f"匹配度：{result['score']} / 100")
    st.progress(result["score"] / 100)
    st.success("已匹配技能：" + "、".join(result["matched_skills"]))
    st.error("缺失技能：" + "、".join(result["missing_skills"]))
    st.write("💡 改进建议：")
    for s in result["suggestions"]:
        st.markdown(f"- {s}")
    cl = generate_cover_letter(jd, resume, result)
    st.text_area("③ 生成求职信", cl, height=300)
    st.download_button("下载求职信", cl, file_name="cover_letter.txt")
