import streamlit as st
import requests
import google.generativeai as genai

# 설정: 생성 AI API 키 입력
genai.configure(api_key='AIzaSyBcyGu7CKosQAukptvYEf0aFttt6_vMAa4')

# Streamlit 페이지 제목
st.title("I Pill You - 증상 분석 챗봇")

# 챗봇 UI 상태 초기화
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


