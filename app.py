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

# 세션 상태 초기화
if "chat_session" not in st.session_state:    
    st.session_state["chat_session"] = model.start_chat(history=[])

# UI 제목
st.title("I pill you - AI Health Chatbot")

# 과거 대화 기록 출력
for content in st.session_state.chat_session.history:
    with st.chat_message("ai" if content.role == "model" else "user"):
        st.markdown(content.parts[0].text)

# 사용자 입력 처리
if user_input := st.chat_input("증상을 입력하세요 (예: '두통이 심해요')."):
    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.chat_session.history.append({"role": "user", "message": user_input})

    # AI 응답 생성
    with st.chat_message("ai"):
        response = st.session_state.chat_session.send_message(
            f"다음 증상에 대한 병명과 약 추천: {user_input}"
        )
        # 응답 출력
        st.markdown(response.text)
        st.session_state.chat_session.history.append({"role": "ai", "message": response.text})
