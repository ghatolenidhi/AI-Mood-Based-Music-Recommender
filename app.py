import streamlit as st
import pandas as pd
import pickle
import re

# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="Mood Music Recommender",
    page_icon="🎧",
    layout="wide"
)

# ----------------------------------
# CSS
# ----------------------------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
url("https://images.unsplash.com/photo-1511379938547-c1f69419868d");
background-size: cover;
background-position: center;
background-attachment: fixed;
}

/* BIG TITLE */

.main-title{
font-size:70px;
font-weight:800;
color:white;
text-align:center;
margin-top:30px;
}

/* Subtitle */

.subtitle{
text-align:center;
color:#dddddd;
font-size:22px;
margin-bottom:30px;
}

/* White text */

.white-text{
color:white;
font-size:24px;
font-weight:500;
}

/* Mood box */

.mood-box{
background:rgba(255,255,255,0.25);
padding:15px;
border-radius:10px;
text-align:center;
color:white;
font-size:24px;
margin-bottom:25px;
}

/* Playlist title */

.playlist-title{
color:white;
font-size:30px;
margin-top:20px;
}

/* Song cards */

.song-card{
background:rgba(255,255,255,0.95);
padding:20px;
border-radius:15px;
box-shadow:0px 8px 20px rgba(0,0,0,0.3);
margin-bottom:20px;
}

.song-name{
font-size:24px;
font-weight:bold;
color:#111;
}

.artist{
color:#444;
margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# Title
# ----------------------------------

st.markdown('<p class="main-title">🎵 AI Mood Music Recommender</p>', unsafe_allow_html=True)

st.markdown('<p class="subtitle">Discover music based on your emotions</p>', unsafe_allow_html=True)

# ----------------------------------
# Load Model
# ----------------------------------

model = pickle.load(open("emotion_model.pkl","rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl","rb"))

# ----------------------------------
# Load Dataset
# ----------------------------------

songs_df = pd.read_csv("mood_music_dataset.csv")

# ----------------------------------
# Text Cleaning
# ----------------------------------

def clean_text(text):

    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]',' ',text)
    text = re.sub(r'\s+',' ',text)

    return text.strip()

# ----------------------------------
# Predict Emotion
# ----------------------------------

def predict_emotion(text):

    text = clean_text(text)

    vector = vectorizer.transform([text])

    emotion = model.predict(vector)[0]

    return emotion

# ----------------------------------
# Recommend Music
# ----------------------------------

def recommend_music(mood,language):

    if language!="Both":
        filtered = songs_df[
            (songs_df["mood"]==mood) &
            (songs_df["language"]==language)
        ]
    else:
        filtered = songs_df[songs_df["mood"]==mood]

    return filtered.sample(min(6,len(filtered)))

# ----------------------------------
# Sidebar
# ----------------------------------

st.sidebar.title("🎧 Music Settings")

language = st.sidebar.selectbox(
"Select Language",
["Both","Hindi","English"]
)

# ----------------------------------
# Input
# ----------------------------------

st.markdown('<p class="white-text">💬 How are you feeling today?</p>', unsafe_allow_html=True)

user_input = st.text_area("",placeholder="Example: I feel very happy today")

# ----------------------------------
# Button
# ----------------------------------

if st.button("🎶 Get My Playlist"):

    if user_input.strip()=="":
        st.warning("Please describe your mood")
    else:

        mood = predict_emotion(user_input)

        st.markdown(
            f'<div class="mood-box">Detected Mood : <b>{mood.upper()}</b></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class="playlist-title">🎧 Recommended Playlist</p>',
            unsafe_allow_html=True
        )

        playlist = recommend_music(mood,language)

        col1,col2,col3 = st.columns(3)

        cols=[col1,col2,col3]

        for i,(index,row) in enumerate(playlist.iterrows()):

            with cols[i%3]:

                st.markdown(f"""
                <div class="song-card">
                <div class="song-name">🎵 {row['song']}</div>
                <div class="artist">Artist: {row['artist']}</div>
                </div>
                """, unsafe_allow_html=True)

                # FIXED YOUTUBE BUTTON
                st.link_button("▶ Play on YouTube", row["youtube_link"])