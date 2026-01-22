import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="קבינט המוחות של אפי", layout="wide")

# הגדרת ה-API - המפתח שלך
API_KEY = "AIzaSyB12avvwGP6ECzfzTFOLDdfJHW37EQJvVo"
genai.configure(api_key=API_KEY)

# שימוש במודל הבסיסי ביותר שעובד בכל מצב
model = genai.GenerativeModel('gemini-pro')

if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    pwd = st.text_input("סיסמה:", type="password")
    if st.button("התחבר"):
        if pwd == "אפי2026":
            st.session_state['auth'] = True
            st.rerun()
    st.stop()

st.title("🏛️ קבינט המוחות: ניתוח אסטרטגי")
idea = st.text_area("תאר את הדילמה (למשל: לידים לעורכי דין בארה\"ב):", height=150)

if st.button("🚀 הפעל דיון"):
    if idea:
        with st.spinner("הקבינט מתכנס..."):
            try:
                # פקודה פשוטה ללא שום תוספות
                prompt = f"נתח עבור אפי כקבינט של סטיב ג'ובס, מאסק ומאקיאוולי את הנושא: {idea}"
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"שגיאה: {str(e)}")