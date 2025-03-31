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
            .phone-container {{
                width: 300px;
                height: 600px;
                border: 16px solid black;
                border-radius: 40px;
                position: relative;
                background-color: white;
                overflow: hidden;
                margin: auto;
                padding: 10px;
            }}
            .phone-screen {{
                width: 100%;
                height: 100%;
                overflow-y: scroll;
            }}
            </style>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ Background image not found | ⚠️ صورة الخلفية غير موجودة.")

set_background("background.jpg")

st.markdown("""
    <div class="phone-container">
        <div class="phone-screen">
            <h2 style="text-align: center;">🌙 Eid al-Fitr 2025 🎉</h2>
            <p style="text-align: center;">🎊 Best wishes of peace and prosperity! | 🎊 أطيب التمنيات بالسلام والازدهار!</p>
            <p style="text-align: center;">💖 Enjoy every moment with your loved ones! | 💖 استمتع بكل لحظة مع أحبائك!</p>
        </div>
    </div>
""", unsafe_allow_html=True)

year_gregorian = 2025
year_hijri = HijriDate.today().year

# ✨ Effet pluie d'étoiles
try:
    rain(emoji="✨", font_size=20, falling_speed=3, animation_length="infinite")
except:
    st.balloons()

colored_header(
    label=f"📅 {year_gregorian} (Gregorian) - {year_hijri} (Hijri) | 📅 {year_gregorian} (ميلادي) - {year_hijri} (هجري)",
    color_name="blue-green-70",
    description=None
)

# 🎵 Musique de l'Eïd (Vidéo YouTube)
st.markdown("""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: black;">
        <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
        src="https://www.youtube.com/embed/G-njYClSVgE?autoplay=1" 
        frameborder="0" allow="autoplay" allowfullscreen></iframe>
    </div>
""", unsafe_allow_html=True)
