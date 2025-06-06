import pandas as pd
import streamlit as st
st.title("🕶学生 小陆-数字档案")
st.header("🔑基础信息")
st.text("学生ID:NEO-2023-001")
st.markdown('注册时间:`2025年6月4日16:29:37`|精神状态：✅正常')
st.markdown("当前教室:`实训楼`|安全等级:`绝密`")
st.header(" 📊 技能矩阵")
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="唱歌", value="85%", delta="-5%")
c2.metric(label="打篮球", value="86%", delta="6%")
c3.metric(label="rapper", value="90%", delta="5%")

st.subheader('Streamlit课程进度')
st.progress(40,text="Streamlit课程进度")
st.header("📝任务日志")
import pandas as pd
import streamlit as st


data = {
    '日期': ['2023-10-01', '2023-10-05', '2023-10-12'],
    '任务': ['学生数学档案', '课程管理系统', '数据图表展示'],
    '状态': ['✅完成', '🕒进行中', '❌未完成'],
    '难度': ['★★☆☆☆', '★☆☆☆☆', '★★★☆☆'],
}


df = pd.DataFrame(data)


def color_task_column(row):
    colors = ['black'] * len(row)
    colors[1] = 'yellow'  
    return [f'color: {color}' for color in colors]


styled_df = df.style.apply(color_task_column, axis=1)


st.subheader("带样式的DataFrame")
st.dataframe(styled_df, height=300)


st.header("🔐最新代码成果")

python_code = '''def matrix_breach():
     while True:
         if detect_vulnerability():
             exploit()
             return "ACCESS GRANTED"
         else:
                stealth_evade()")
'''

st.code(python_code)


st.markdown(':green[`>>SYSTEM MESSAGE:`]下一个任务目标已解锁')
st.markdown(' :green[`>>TARGET:`]课程管理系统')
st.markdown(':green[`>>CUNTDOWN:`]2025-06-03 15：24：58')
