import streamlit as st
import google.generativeai as genai

# Google Generative AI 설정
YOUR_API_KEY = 'AIzaSyBcyGu7CKosQAukptvYEf0aFttt6_vMAa4'  # 여기에 본인의 Google Generative AI API 키를 입력하세요.
genai.configure(api_key=YOUR_API_KEY)

# 모델 로드
@st.cache_resource
def load_model():
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("Model loaded...")
    return model

model = load_model()

