import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="קבינט המוחות של אפי", layout="wide")

# הגדרת ה-API
API_KEY = "AIzaSyB12avvwGP6ECzfzTFOLDdfJHW37EQJvVo"
genai.configure(api_key=API_KEY)

# מנגנון שמוצא אוטומטית את המודל התקין כדי למנוע שגיאת 404
@st.cache_resource
def load_model():
    try:
        # ניסיון ראשון: המודל הכי חדיש
        return genai.GenerativeModel('gemini-1.5-flash-latest')
    except:
        # ניסיון שני: המודל הסטנדרטי
        return genai.GenerativeModel('gemini-pro')

model = load_model()

# --- אבטחה ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    pwd = st.text_input("סיסמה:", type="password")
    if st.button("התחבר"):
        if pwd == "אפי2026":
            st.session_state['auth'] = True
            st.rerun()
    st.stop()

# --- ממשק ---
st.title("🏛️ קבינט המוחות: ניתוח לידים בארה\"ב")
idea = st.text_area("הכנס את הדילמה העסקית שלך:", height=150)

if st.button("🚀 הפעל את הקבינט"):
    if idea:
        with st.spinner("מתחבר למוחות הגדולים..."):
            try:
                # שימוש ב-transport='rest' עוקף את בעיית ה-v1beta
                response = model.generate_content(
                    f"נתח עבור אפי את נושא הלידים לעורכי דין בארה\"ב: {idea}. השב כקבינט של סטיב ג'ובס, מאסק ומאקיאוולי.",
                    transport='rest'
                )
                st.markdown(response.text)
            except Exception as e:
                st.error(f"ניסיון אחרון נכשל: {str(e)}")
                st.info("נסה ללחוץ על 'Clear Cache' בתפריט הימני למעלה.")