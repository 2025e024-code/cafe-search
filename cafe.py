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
    "Info",
    "Title_URL"
]]

df.columns = [
    "店名",
    "評価",
    "口コミ数",
    "予算",
    "URL"
]
st.sidebar.header("検索条件")

min_rating = st.sidebar.slider(
    "最低評価",
    float(df["評価"].min()),
    float(df["評価"].max()),
    3.0,
    0.1
)

min_review = st.sidebar.slider(
    "最低口コミ数",
    0,
    int(df["口コミ数"].max()),
    0
)

df = df[
    (df["評価"] >= min_rating) &
    (df["口コミ数"] >= min_review)
]
# 显示数据
st.dataframe(df)