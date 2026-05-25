import streamlit as st
import cv2
import mediapipe as mp
import librosa
import google.generativeai as genai
import tempfile
import plotly.graph_objects as go
import numpy as np
import datetime
import os

# Key HuggingFace Secrets bata lincha. Code ma kahile na lekh
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

st.set_page_config(page_title="Dance Kundali AI 💰", layout="wide")
st.title("Dance Kundali AI - US RPM Booster 💃")
st.write("Dance video hal, ma cut, loop, hook, caption, hashtag + Dollar sabai bhandinchhu")

uploaded_file = st.file_uploader("Dance Video Upload Gar", type=["mp4", "mov", "mkv"])

def analyze_video(video_path):
    y, sr = librosa.load(video_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    energy_per_sec, face_score = [], []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        if frame_count % int(fps) == 0:
            results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                lm = results.pose_landmarks.landmark
                lw = lm[mp_pose.PoseLandmark.LEFT_WRIST.value]
                rw = lm[mp_pose.PoseLandmark.RIGHT_WRIST.value]
                energy = (abs(lw.y - rw.y) + abs(lw.x - rw.x)) * 100
                energy_per_sec.append(min(energy, 100))
                face_score.append(1 if lm[0].visibility > 0.8 else 0)
            else:
                energy_per_sec.append(0)
                face_score.append(0)
        frame_count += 1
    cap.release()
    return tempo, beat_times, energy_per_sec, face_score, duration, fps

def generate_kundali(tempo, beats, energy, face, duration, audio, post_time):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    You are MrBeast's video editor + Facebook Ads expert. Yo dance video ko PURA KUNDALI nikal Nepali ma.

    VIDEO DATA:
    1. Length: {duration:.1f} sec, BPM: {tempo:.0f}
    2. Beat drops at sec: {np.round(beats[:8],1).tolist()}
    3. Energy per second: {np.round(energy,0).tolist()}
    4. Face visible per second: {face}
    5. User ko Audio: {audio}, Post Time NPT: {post_time}

    TIMILAI YEHI DEU - EXACT FORMAT MA:

    **1. 3-SEC HOOK KUNDALI:**
    - Problem: Kun second boring cha?
    - Fix: "0.0s ma YO GAR" - exact step deu. Text: "3 SABDA KO HOOK" suggest gar.

    **2. CUT KAHAN GARNE:**
    - Boring Zone: {np.where(np.array(energy) < 30)[0].tolist()} second ma energy low cha. Yaha kaat.
    - Best Parts: {np.argsort(energy)[-3:].tolist()} second rakh. Baki faalda.
    - Final Length: X sec banaune.

    **3. PERFECT LOOP KAHAN:**
    - Last frame: {duration-0.5:.1f}s dekhi First frame 0.0s sanga match garne.
    - Trick: "Last 0.5s ma first pose copy han" bhanera exact bhan.

    **4. US RPM KUNDALI:**
    - Estimated RPM: $X.XX - $X.XX per 1000 views
    - Why Low/High: 1 line reason
    - 3 Fix for USA: Audio, Caption, Time exact bhan.

    **5. CAPTION + HASHTAG:**
    - Caption: 1 line English, comment bait. Example: "Rate this move 1-10 👇"
    - Hashtags: 3 ota matra. #dance #usa #fyp

    **6. UPLOAD TIME:**
    - Nepal Time: {post_time} = US New York kati baje hunchha calculate gar. "YES/NO" post garne ki nai bhan.

    **7. FINAL SCORE: X/100 + If 1M views = $XXXX earning**
    Hype ma bhan, MrBeast jastai.
    """
    response = model.generate_content(prompt)
    return response.text

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
        tmp.write(uploaded_file.read())
        video_path = tmp.name

    st.video(uploaded_file)

    col1, col2 = st.columns(2)
    with col1: audio_used = st.text_input("Audio Name", "Espresso - Sabrina Carpenter")
    with col2: post_time = st.time_input("Post Time NPT", value=datetime.time(20, 0))

    if st.button("🔮 KUNDALI NIKAL", type="primary"):
        with st.spinner('Beat, Pose, Face, RPM sabai analyze gardai chu... 30 sec'):
            tempo, beats, energy, face, duration, fps = analyze_video(video_path)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(range(len(energy))), y=energy, mode='lines+markers', name='Energy'))
        for beat in beats:
            if beat < duration: fig.add_vline(x=beat, line_dash="dot", line_color="green")
        fig.add_hrect(y0=0, y1=30, fillcolor="red", opacity=0.2, annotation_text="CUT THIS ZONE")
        fig.update_layout(title="Second-by-Second KUNDALI: Red=Cut, Green=Beat", xaxis_title="Seconds")
        st.plotly_chart(fig)

        st.subheader("💎 PURA KUNDALI REPORT")
        report = generate_kundali(tempo, beats, energy, face, duration, audio_used, post_time)
        st.markdown(report)
