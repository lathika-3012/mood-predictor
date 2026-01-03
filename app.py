import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import os

# -------- Load Dataset --------
df = pd.read_csv("data.csv")

# Encode categorical columns
le_time = LabelEncoder()
le_mood = LabelEncoder()

df["time_of_day"] = le_time.fit_transform(df["time_of_day"])
df["mood"] = le_mood.fit_transform(df["mood"])

# Split X, y
X = df[["temperature", "humidity", "time_of_day"]]
y = df["mood"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# -------- Streamlit App --------
st.set_page_config(page_title="Mood Predictor", layout="centered")
st.title("🌤 Mood Predictor with Quotes, Recommendations & History")

# Input sliders
temp = st.slider("Temperature (°C)", 15, 40, 30)
humidity = st.slider("Humidity (%)", 20, 100, 50)
time_of_day = st.selectbox("Time of Day", ["morning", "afternoon", "evening", "night"])

# Predict button
if st.button("Predict Mood"):
    time_encoded = le_time.transform([time_of_day])[0]
    pred = model.predict([[temp, humidity, time_encoded]])
    predicted_mood = le_mood.inverse_transform(pred)[0]

    # -------- Mood Themes --------
    mood_colors = {
        "Happy": "#FFF59D",   # Light Yellow
        "Sad": "#90CAF9",     # Light Blue
        "Neutral": "#E0E0E0"  # Light Grey
    }

    st.markdown(
        f"<div style='background-color: {mood_colors[predicted_mood]}; padding: 20px; border-radius: 10px'>"
        f"<h2 style='text-align: center;'>Predicted Mood: {predicted_mood} "
        f"{'😄' if predicted_mood=='Happy' else '😞' if predicted_mood=='Sad' else '😐'}</h2></div>",
        unsafe_allow_html=True
    )

    # -------- Mood Quotes --------
    mood_quotes = {
        "Happy": "Happiness is not by chance, but by choice. 😊",
        "Sad": "Every storm runs out of rain. 💛",
        "Neutral": "Keep going! Every day is a new beginning. 🌱"
    }
    st.info(mood_quotes[predicted_mood])

    # -------- Mood Recommendations --------
    mood_recommendations = {
        "Happy": "Keep enjoying your day! 🎶 Listen to music or share a smile with someone.",
        "Sad": "Take a short walk, drink water, or talk to a friend. 💛",
        "Neutral": "Try doing something fun or relaxing to lift your spirits. 🌱"
    }
    st.success(mood_recommendations[predicted_mood])

    # -------- Save Prediction to history.csv --------
    history_file = "history.csv"
    new_data = pd.DataFrame({
        "temperature": [temp],
        "humidity": [humidity],
        "time_of_day": [time_of_day],
        "predicted_mood": [predicted_mood]
    })

    if os.path.exists(history_file):
        new_data.to_csv(history_file, mode='a', index=False, header=False)
    else:
        new_data.to_csv(history_file, index=False)

    st.info("✅ Prediction saved to history!")

# -------- Mood History Tracker --------
if os.path.exists("history.csv"):
    st.subheader("📊 Mood Prediction History")
    history_df = pd.read_csv("history.csv")
    st.dataframe(history_df)

    st.bar_chart(history_df["predicted_mood"].value_counts())

    # -------- Download Button --------
    csv = history_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Mood History CSV",
        data=csv,
        file_name='mood_history.csv',
        mime='text/csv'
    )
