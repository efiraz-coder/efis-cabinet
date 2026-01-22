import streamlit as st
import google.generativeai as genai
import os

# הגדרות דף
st.set_page_config(page_title="קבינט המוחות של אפי", layout="wide")

# הגדרת ה-API עם כפיית גרסה יציבה (v1)
API_KEY = "AIzaSyB12avvwGP6ECzfzTFOLDdfJHW37EQJvVo"
genai.configure(api_key=API_KEY)

# יצירת המודל - שימוש ב-1.5 פלאש שהוא הכי עדכני כרגע
model = genai.GenerativeModel('gemini-1.5-flash')

# מנגנון סיסמה
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    pwd = st.text_input("סיסמה:", type="password")
    if st.button("התחבר"):
        if pwd == "אפי2026":
            st.session_state['auth'] = True
            st.rerun()
    st.stop()

st.title("🏛️ קבינט המוחות הגדולים")
idea = st.text_area("תאר את הדילמה (למשל: לידים לעורכי דין בארה\"ב):", height=150)

if st.button("🚀 הפעל דיון"):
    if idea:
        with st.spinner("הקבינט מתכנס לדיון מעמיק..."):
            try:
                # הפקודה הכי בסיסית שיש
                response = model.generate_content(f"נתח עבור אפי כקבינט של סטיב ג'ובס, אלון מאסק ומאקיאוולי את הנושא הבא: {idea}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"שגיאה בתקשורת: {str(e)}")
                st.info("אם מופיעה שגיאת 404, יש לבצע Reboot לאפליקציה ב-Streamlit Cloud.")