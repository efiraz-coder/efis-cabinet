import streamlit as st
import google.generativeai as genai

# הגדרות בסיסיות
st.set_page_config(page_title="הקבינט של אפי", layout="wide")

# הגדרת ה-AI
API_KEY = "AIzaSyB12avvwGP6ECzfzTFOLDdfJHW37EQJvVo"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# כניסה פשוטה
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    pwd = st.text_input("סיסמה:", type="password")
    if st.button("התחבר"):
        if pwd == "אפי2026":
            st.session_state['auth'] = True
            st.rerun()
    st.stop()

# ממשק משתמש
st.title("🏛️ קבינט המוחות הגדולים")
idea = st.text_area("תאר את הדילמה (לידים, עורכי דין וכו'):", height=150)

if st.button("הפעל דיון"):
    if idea:
        with st.spinner("הקבינט חושב..."):
            try:
                # כאן מחקנו את ה-transport שגרם לשגיאה
                response = model.generate_content(f"נתח עבור אפי כקבינט יועצים (ג'ובס, מאסק, מאקיאוולי): {idea}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"שגיאה: {str(e)}")