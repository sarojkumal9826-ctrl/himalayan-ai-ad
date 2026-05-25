import requests
from geopy.geocoders import Nominatim

# Yo function haru mathi ko code ko muni paste han

def get_trending_audio_by_country():
    # Top 5 high RPM desh ko trending audio list
    # Real ma ta Apify/Instagram API chaiyo, demo ko lagi hardcoded
    high_rpm_trends = {
        "US": ["Love On - Selena Gomez", "MILLION DOLLAR BABY", "Espresso"],
        "UK": ["Band4Band", "Backbone", "Austin"],
        "Canada": ["BIRDS OF A FEATHER", "Good Luck Babe", "HOT TO GO"],
        "Australia": ["Please Please Please", "Not Like Us", "LUNCH"],
        "Germany": ["Wunder", "Komet", "Zeit"]
    }
    return high_rpm_trends

def rpm_predictor_ai(audio_name, caption_lang, post_time_npt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    You are Facebook Ads RPM expert. Yo video ko estimated RPM calculate gara USD ma.

    Data:
    1. Audio used: {audio_name}
    2. Caption language: {caption_lang} 
    3. Post time Nepal: {post_time_npt}

    Rule:
    - US/UK/Canada audio use bhayo bhane base RPM $3-$8
    - Nepali audio = $0.1-$0.5
    - English caption + 7-10 PM NPT post = US audience le raat ma herne, RPM x2
    - Nepali caption = Nepal only, RPM low

    Answer in Nepali:
    1. Estimated RPM: $X.XX - $X.XX per 1000 views
    2. Why: 1 line reason
    3. 3 ota Fix to target US: "Audio change gar", "Caption English ma lekh" jasto exact
    4. If 1M views: Estimated earning = $XXX - $XXXX
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI ma naya section add gara
st.subheader("💰 Worldwide RPM Kundali")

col1, col2, col3 = st.columns(3)
with col1:
    audio_used = st.text_input("Kun Audio Use Garyau?", "Espresso - Sabrina Carpenter")
with col2:
    caption_lang = st.selectbox("Caption Language", ["English", "Nepali", "Hindi"])
with col3:
    post_time = st.time_input("Kati Baje Post Garne?", value=datetime.time(19, 0))

if st.button("RPM Calculate Gar"):
    with st.spinner('Dollar hisab gardai chu...'):
        rpm_report = rpm_predictor_ai(audio_used, caption_lang, post_time)
    st.markdown(rpm_report)
    
    # High RPM Audio Suggestions
    st.subheader("🔥 High RPM Audio - Aaja ko lagi")
    trends = get_trending_audio_by_country()
    for country, audios in trends.items():
        st.write(f"**{country}**: {', '.join(audios)}")
