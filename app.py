import streamlit as st
import google.generativeai as genai

# הגדרות דף
st.set_page_config(page_title="קבינט המוחות: ניתוח אסטרטגי", layout="wide")

# --- חיבור ל-API ---
API_KEY = "AIzaSyB12avvwGP6ECzfzTFOLDdfJHW37EQJvVo" 
genai.configure(api_key=API_KEY)

# ניסיון חיבור למודל יציב
model = genai.GenerativeModel('gemini-1.5-flash')

# --- מנגנון סיסמה ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

with st.sidebar:
    st.header("🔐 כניסה")
    pwd = st.text_input("סיסמה:", type="password")
    if st.button("התחבר"):
        if pwd == "אפי2026":
            st.session_state['auth'] = True
            st.rerun()

if not st.session_state['auth']:
    st.info("אנא הזן סיסמה.")
    st.stop()

st.title("🏛️ קבינט המוחות הגדולים")
st.markdown("### ניתוח אסטרטגי וסינתזה בין מוחות")

idea = st.text_area("תאר את המיזם או הבעיה העסקית שלך (למשל: לידים לעורכי דין בארה\"ב):", height=200)

if st.button("🚀 הפעל סימולציית קבינט"):
    if not idea:
        st.error("הכנס תוכן לניתוח.")
    else:
        with st.spinner("המוחות מנתחים את השוק בארה\"ב ומתווכחים..."):
            prompt = f"""
            נתח עבור אפי את הנושא: "{idea}"
            אתה קבינט הכולל את: סטיב ג'ובס, אלון מאסק, ניקולו מאקיאוולי, וישעיהו לייבוביץ.
            
            הנחיות:
            1. כל דמות מגיבה מנקודת מבטה המקצועית/פילוסופית.
            2. צור ויכוח ביניהם (הצלבת דעות).
            3. התייחס ספציפית לשוק הלידים ותאונות הדרכים בארה"ב.
            4. סיכום: 3 המלצות מעשיות בשורה התחתונה.
            כתוב בעברית.
            """
            try:
                # התיקון המרכזי: שליחה ללא ציון גרסת API בתוך הפונקציה
                response = model.generate_content(prompt)
                st.divider()
                st.markdown(response.text)
            except Exception as e:
                st.error(f"שגיאה: {str(e)}")

st.divider()
st.caption("מערכת הקבינט | Gemini AI 2026")