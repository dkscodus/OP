import streamlit as st
import requests
import google.generativeai as genai

# 설정: 생성 AI API 키 입력
genai.configure(api_key="YOUR_API_KEY")
genai.configure(api_key="AIzaSyBcyGu7CKosQAukptvYEf0aFttt6_vMAa4")

genai.configure(api_key='AIzaSyBcyGu7CKosQAukptvYEf0aFttt6_vMAa4')

# Streamlit 페이지 제목
st.title("I Pill You - 증상 분석 챗봇")

# 챗봇 UI 상태 초기화
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# 증상 분석 알고리즘 정의
def analyze_symptoms(symptoms):
    """간단한 증상 분석 알고리즘"""
    common_illnesses = {
        "headache": "편두통",
        "fever": "감기",
        "stomachache": "위염",
        "cough": "기관지염"
    }
    for keyword, diagnosis in common_illnesses.items():
        if keyword in symptoms.lower():
            return diagnosis
    return "정확한 분석을 위해 더 많은 정보가 필요합니다."

# 웹 크롤링을 통한 관련 정보 검색
def fetch_medical_info(symptom):
    """간단한 웹 크롤링 시뮬레이션"""
    url = f"https://api.example.com/search?symptom={symptom}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("summary", "정보를 찾을 수 없습니다.")
    except Exception as e:
        return f"오류 발생: {e}"

# 생성 AI 모델 로드
def load_model():
    return genai.GenerativeModel('gemini-1.5-flash')

@st.cache_resource
def get_chat_model():
    return load_model()

model = get_chat_model()

# 채팅 메시지 표시
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 받기
if prompt := st.chat_input("증상을 입력하세요. 예: '머리가 아프고 열이 나요'"):
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.chat_history.append({"role": "user", "content": prompt})

    # 증상 분석
    diagnosis = analyze_symptoms(prompt)

    # 생성 AI 응답 생성
    chat_response = model.start_chat().send_message(prompt)

    # 웹 크롤링으로 정보 검색
    additional_info = fetch_medical_info(prompt)

    # AI 응답 표시
    with st.chat_message("ai"):
        response_content = (
            f"### 증상 분석 결과\n- {diagnosis}\n\n"
            f"### AI의 추가 정보\n- {chat_response.text}\n\n"
            f"### 관련 정보\n- {additional_info}"
        )
        st.markdown(response_content)
        st.session_state.chat_history.append({"role": "ai", "content": response_content})