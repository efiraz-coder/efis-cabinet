import streamlit as st
import google.generativeai as genai

# הגדרות דף - מראה מקצועי ורחב
st.set_page_config(page_title="הקבינט האסטרטגי - אפי", layout="wide")

# --- חיבור למוח של גוגל (GEMINI) ---
API_KEY = "AIzaSyB12avvwGP6ECzfzTFOLDdfJHW37EQJvVo" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- מנגנון אבטחה ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

with st.sidebar:
    st.header("🔐 כניסה לקבינט")
    pwd = st.text_input("סיסמה:", type="password")
    if st.button("פתח ישיבה"):
        if pwd == "אפי2026":
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("סיסמה שגויה")

if not st.session_state['auth']:
    st.info("ממתין לזיהוי מנהל הקבינט...")
    st.stop()

# --- ממשק המשתמש ---
st.title("🏛️ קבינט המוחות הגדולים: ניתוח אסטרטגי")
st.markdown("### המערכת תנתח את הדילמה שלך דרך הצלבת דעות וסינתזה מעמיקה")

# אזור הזנת השאלה
user_input = st.text_area("תאר את המיזם או הבעיה העסקית שלך:", 
                          height=150, 
                          placeholder="למשל: סקירת צרכים של עורכי דין בארה\"ב ללידים של תאונות דרכים...")

if st.button("🚀 הפעל סימולציית קבינט"):
    if not user_input:
        st.warning("נא להזין תוכן לניתוח.")
    else:
        with st.spinner("הקבינט מעבד את הנתונים ומייצר עימות רעיוני..."):
            
            # הפרומפט שגורם להם לחשוב באמת
            full_prompt = f"""
            נתח לעומק את הנושא הבא עבור אפי: "{user_input}"
            
            המשימה: צור דיון חי ונוקב בין המוחות הבאים:
            1. סטיב ג'ובס (מיקוד בחוויית משתמש ופשטות קיצונית).
            2. אלון מאסק (מיקוד באופטימיזציה הנדסית, דאטה וסקייל).
            3. ניקולו מאקיאוולי (מיקוד בכוח, בלעדיות וניצול הזדמנויות בשוק).
            4. ישעיהו לייבוביץ (ביקורת ערכית וחדות לוגית).
            5. מרקו אורליוס (סטואיות, חובה וניהול סיכונים מושכל).
            
            דרישות חובה:
            - כל דמות חייבת להתייחס לנקודות ספציפיות בטקסט של אפי (כמו 'עורכי דין בארה"ב', 'לידים של תאונות').
            - על הדמויות להתווכח אחת עם השנייה (למשל: מאסק קורא ללייבוביץ' מיושן, ג'ובס מבקר את חוסר הסטייל של מאסק).
            - ספק תובנות אופרטיביות (מה הלקוח באמת צריך?).
            
            בסוף הדיון, כתוב פרק בשם 'שורה תחתונה אסטרטגית לאפי' עם 3 המלצות לביצוע.
            כתוב הכל בעברית רהוטה ומקצועית.
            """
            
            try:
                response = model.generate_content(full_prompt)
                st.divider()
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"שגיאה בתקשורת עם ה-AI: {e}")

st.divider()
st.caption("מערכת הקבינט 2026 | מופעל על ידי Gemini 1.5 Pro")