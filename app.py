import streamlit as st
import random

# הגדרות דף
st.set_page_config(page_title="קבינט המוחות", layout="wide")

# מנגנון סיסמה
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

with st.sidebar:
    st.header("🔐 כניסה לקבינט")
    pwd = st.text_input("סיסמת גישה:", type="password")
    if st.button("התחבר"):
        if pwd == "אפי2026":
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("סיסמה שגויה")

if not st.session_state['auth']:
    st.warning("אנא הזן סיסמה כדי להתחיל בישיבה.")
    st.stop()

# ניהול יועצים בסרגל הצד
with st.sidebar:
    st.divider()
    st.header("👥 בחר את היועצים")
    
    cabinet_data = {
        "סטיב ג'ובס": "🍏", "אלון מאסק": "🚀", "מהטמה גנדי": "🧘", 
        "מרקו אורליוס": "🏛️", "ישעיהו לייבוביץ": "✡️", "זיגמונד פרויד": "🛋️", 
        "פרידריך ניטשה": "🌋", "סונדאר פיצ'אי": "🔍", "ג'נסן הואנג": "🎮"
    }

    selected_members = []
    for name in cabinet_data.keys():
        if st.checkbox(name, value=True):
            selected_members.append(name)
            
    st.divider()
    surprise_on = st.toggle("הוסף יועץ בהפתעה", value=True)

# גוף האפליקציה
st.title("🏛️ קבינט המוחות הגדולים")
idea = st.text_area("העלה את המחשבה שלך כאן:", placeholder="למשל: האם כדאי לי לעזוב הכל ולפתוח חווה בפורטוגל?")

if st.button("🚀 שמע את דעת הקבינט"):
    if not idea:
        st.error("כתוב רעיון כדי שהקבינט יוכל לדון בו.")
    else:
        # בנק התגובות
        responses = {
            "סטיב ג'ובס": "זה חסר נשמה. אם זה לא משאיר שריטה ביקום, חבל על הזמן שלך. איפה הטירוף?",
            "אלון מאסק": "מה ה-First Principles כאן? זה צריך להיות יעיל פי 10 מהקיים או שזה יקרוס.",
            "מהטמה גנדי": "האם זה משרת את האדם העני ביותר? קידמה ללא אנושיות היא אלימות שקטה.",
            "מרקו אורליוס": "האם זה תואם את הטבע והחובה שלך? אם זה נובע מאגו, זה חסר ערך.",
            "ישעיהו לייבוביץ": "שטויות! אתה מבלבל בין צרכים לערכים. זוהי עוד עבודת אלילים טכנולוגית.",
            "זיגמונד פרויד": "זהו מנגנון פיצוי על חרדת שליטה. האם זה פתרון או סימפטום של תסביך?",
            "פרידריך ניטשה": "האם זה רעיון של אדם עליון או של עדר? היה מסוכן, רק כך תצמח עוצמה.",
            "סונדאר פיצ'אי": "מעניין, אבל האם זה Scaleable? בלי דאטה ותשתית ענן, אין פה באמת עסק.",
            "ג'נסן הואנג": "אתה צריך יותר כוח מחשוב. אם זה לא רץ על GPU, זה כבר שייך לעבר."
        }

        # הוספת יועץ בהפתעה
        if surprise_on:
            surprise_pool = {
                "ניקולו מאקיאוולי": "🦊 'עדיף שיפחדו ממך מאשר שיאהבו אותך. השתמש ברעיון הזה לכוח.'",
                "לאונרדו דה וינצ'י": "🎨 'פשטות היא התחכום האולטימטיבי. הרעיון שלך עמוס מדי.'",
                "אלכסנדר הגדול": "⚔️ 'הרעיון שלך קטן מדי. העולם שייך למי שמעז לכבוש את הבלתי אפשרי!'"
            }
            s_name, s_text = random.choice(list(surprise_pool.items()))
            selected_members.append(s_name)
            responses[s_name] = s_text
            cabinet_data[s_name] = "🎁"

        # תצוגה בעמודות
        cols = st.columns(3)
        for idx, name in enumerate(selected_members):
            with cols[idx % 3]:
                with st.chat_message(name, avatar=cabinet_data.get(name, "👤")):
                    st.subheader(name)
                    st.write(responses.get(name, "אין לי מה לומר על זה."))

        st.divider()
        st.info("✅ הישיבה ננעלה.")