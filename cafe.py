import streamlit as st
import pandas as pd

# 页面标题
st.title("金沢カフェ検索")

# 读取数据
df = pd.read_csv("cafe.csv")

# 修改列名
df = df[[
    "Title",
    "crating_val",
    "Number",
    "Avg_price1",
    "Title_URL"
]]

df.columns = [
    "店名",
    "評価",
    "口コミ数",
    "予算",
    "URL"
]

# 显示数据
st.dataframe(df)