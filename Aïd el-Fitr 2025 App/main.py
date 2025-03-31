import streamlit as st
import time
import random
import os
import base64
from ummalqura.hijri_date import HijriDate
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="Eid al-Fitr 2025 | عيد الفطر 2025", page_icon="🌙", layout="wide")

# 📸 Définir l'image de fond
def set_background(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as file:
            encoded_string = base64.b64encode(file.read()).decode()
        st.markdown(f"""
            <style>
            .stApp {{
                background: url("data:image/jpg;base64,{encoded_string}") no-repeat center center fixed;
                background-size: cover;
            }}
            .text-box {{
                background-color: rgba(0, 0, 0, 0.5);
                padding: 10px;
                border-radius: 10px;
                display: inline-block;
            }}
            h1, h2, h3, h4, h5, h6, p, span, div {{
                color: gold !important;
                text-shadow: 2px 2px 5px black;
                font-weight: bold;
            }}
            /* 📱 Style pour mobile */
            @media (max-width: 768px) {{
                h1, h2, h3, h4, h5, h6, p, span, div {{
                    font-size: 18px !important;
                }}
                button {{
                    font-size: 20px !important;
                    padding: 12px !important;
                }}
            }}
            </style>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ Background image not found | ⚠️ صورة الخلفية غير موجودة.")

set_background("background.jpg")

year_gregorian = 2025
year_hijri = HijriDate.today().year

# ✨ Effet pluie d'étoiles
try:
    rain(emoji="✨", font_size=20, falling_speed=3, animation_length="infinite")
except:
    st.balloons()

# 🎉 Titre principal
st.markdown("""
    <h1 class="text-box" style="text-align: center; font-size: 50px;">
        🌙✨ Eid al-Fitr 2025 ✨🌙 | 🎉 عيد الفطر 2025 🎉
    </h1>
""", unsafe_allow_html=True)

colored_header(
    label=f"📅 {year_gregorian} (Gregorian) - {year_hijri} (Hijri) | 📅 {year_gregorian} (ميلادي) - {year_hijri} (هجري)",
    color_name="blue-green-70",
    description=None
)

# 🕌 Étapes de l'Aïd
steps = [
    ("🕌", "Perform Eid prayer | أداء صلاة العيد"),
    ("🍽️", "Enjoy a meal with family | تناول وجبة العيد مع العائلة"),
    ("🎁", "Give and receive gifts | تقديم واستقبال الهدايا"),
    ("💖", "Share joy with loved ones | مشاركة الفرح مع الأحباء")
]

progress_bar = st.progress(0)
for i, (emoji, text) in enumerate(steps):
    with st.spinner(f"{emoji} {text}..."):
        time.sleep(1.5)
    st.success(f"✅ {emoji} {text}")
    progress_bar.progress((i + 1) / len(steps))

# 📱 Simulation d'un téléphone avec écran défilant
phone_css = """
<style>
    .phone-frame {
        width: 300px;
        height: 550px;
        border: 16px solid black;
        border-radius: 40px;
        position: relative;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        overflow: hidden;
        background: white;
        margin: auto;
    }
    .phone-screen {
        width: 100%;
        height: 100%;
        overflow-y: scroll;
        padding: 10px;
    }
    .top-bar {
        width: 100%;
        height: 30px;
        background: black;
        border-radius: 25px 25px 0 0;
        position: absolute;
        top: 0;
        left: 0;
    }
</style>
"""

phone_content = """
<div class='phone-screen'>
    <h3>📱 Eid al-Fitr 2025</h3>
    <p>Bienvenue dans cette application spéciale Aïd !</p>
    <ul>
        <li>🌙 Informations sur l'Aïd</li>
        <li>🎁 Idées de cadeaux</li>
        <li>🍽️ Recettes traditionnelles</li>
    </ul>
    <p>Défilez pour en voir plus...</p>
</div>
"""

st.markdown(phone_css, unsafe_allow_html=True)
st.markdown("<div class='phone-frame'><div class='top-bar'></div>" + phone_content + "</div>", unsafe_allow_html=True)

# 💌 Message spécial
with stylable_container(
    key="special_message",
    css_styles=""" 
        border: 2px solid white;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        color: white;
        text-shadow: 2px 2px 5px black;
        font-weight: bold;
    """
):
    st.markdown("### 🎁 Receive a special message | 🎁 احصل على رسالة خاصة")
    if st.button("📩 Click here for a surprise | 📩 اضغط هنا للمفاجأة"):
        with st.spinner("Preparing message... | يتم تحضير الرسالة..."):
            time.sleep(2)
        st.success(random.choice([
            "🌟 May Eid bring you happiness! | 🌟 أتمنى لك عيدًا سعيدًا!",
            "🎊 Best wishes of peace and prosperity! | 🎊 أطيب التمنيات بالسلام والازدهار!",
            "💖 Enjoy every moment with your loved ones! | 💖 استمتع بكل لحظة مع أحبائك!"
        ]))

# 🎵 Musique de l'Eïd (Vidéo YouTube)
with stylable_container(
    key="music_section",
    css_styles=""" 
        background-color: rgba(0, 0, 0, 0.5);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
    """
):
    st.markdown("""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: black;">
        <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
        src="https://www.youtube.com/embed/G-njYClSVgE?autoplay=1" 
        frameborder="0" allow="autoplay" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)
