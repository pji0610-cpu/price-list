import streamlit as st
import pandas as pd

st.title("📱 우리집 가격표")

# 같은 폴더에 있는 data.csv 파일을 읽어옵니다.
try:
    df = pd.read_csv("data.csv", encoding='utf-8')
    query = st.text_input("🔍 품목명 검색", "")
    if query:
        res = df[df['품목명'].str.contains(query, na=False)]
        for i, row in res.iterrows():
            st.info(f"**{row['품목명']}**: {row['가격']:,}원")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)
except:
    st.error("data.csv 파일을 찾을 수 없거나 형식이 잘못되었습니다.")
