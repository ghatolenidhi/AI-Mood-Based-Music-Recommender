# 🎵 AI Mood-Based Music Recommendation System

An **AI-powered music recommendation web application** that detects a user's mood from text input and recommends songs accordingly.

This project uses **Natural Language Processing (NLP)** and **Machine Learning** to analyze user emotions and suggest music that matches the detected mood.

The application is built using **Python, Scikit-learn, and Streamlit** and provides an interactive web interface where users can enter their feelings and instantly get music recommendations.

---

# 📌 Project Description

Music plays an important role in influencing human emotions.  
The goal of this project is to build an intelligent system that recommends songs based on a user's emotional state.

The system works by:

1. Taking **user input text describing their mood**
2. Processing the text using **Natural Language Processing (NLP)**
3. Predicting the **emotion using a Machine Learning model**
4. Matching the predicted mood with songs from a **music dataset**
5. Displaying recommended songs with **direct YouTube links**

---

# 🚀 Features

- AI-based **Mood Detection**
- **Natural Language Processing (NLP)** for text analysis
- **Machine Learning Model** for emotion classification
- **Mood-Based Song Recommendation**
- Support for **Hindi and English songs**
- **Direct YouTube links** for listening to songs
- **Interactive Streamlit Web Application**
- Clean and attractive music-themed UI

---

# 🧠 Technologies Used

- Python
- Natural Language Processing (NLP)
- Scikit-learn
- TF-IDF Vectorization
- Machine Learning (Naive Bayes)
- Streamlit
- Pandas
- NumPy

---

# 📂 Project Structure

```
AI-Mood-Music-Recommender
│
├── data
│   ├── emotion_dataset.csv
│   └── mood_music_dataset.csv
│
├── model
│   ├── emotion_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebook
│   └── mood_prediction.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### 1 Clone the repository

```
git clone https://github.com/yourusername/AI-Mood-Music-Recommender.git
```

### 2 Go to the project folder

```
cd AI-Mood-Music-Recommender
```

### 3 Install dependencies

```
pip install -r requirements.txt
```

### 4 Run the application

```
streamlit run app.py
```

### 5 Open in browser

```
http://localhost:8501
```

---

# 🎥 Demo Video

Drag and drop your demo video here when editing this README on GitHub.

Example:

```
Upload demo-video.mp4 here
```

GitHub will automatically generate a video player after you upload the file.

---

# 📊 Dataset Information

This project uses two datasets.

## 1 Emotion Dataset

Used to train the machine learning model.

Columns:

```
text
emotion
```

Example:

```
I feel very happy today → happy
I feel lonely → sad
I am very angry → angry
```

---

## 2 Music Dataset

Used for recommending songs based on mood.

Columns:

```
song
artist
mood
language
youtube_link
```

Example:

```
Kesariya, Arijit Singh, happy, Hindi, https://youtube.com/...
Believer, Imagine Dragons, angry, English, https://youtube.com/...
```

---

# 🔍 How the System Works

```
User Input Text
        ↓
Text Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Machine Learning Model
        ↓
Emotion Prediction
        ↓
Song Dataset Filtering
        ↓
Recommended Playlist
```

---

# 🌟 Future Improvements

- Spotify API integration
- Voice-based mood detection
- Deep learning emotion detection
- Personalized music playlists
- User login system

---

