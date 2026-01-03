#  Mood Predictor using Machine Learning

A Streamlit-based Machine Learning application that predicts a user's **mood** based on environmental conditions such as **temperature**, **humidity**, and **time of day**.  
The app also provides **motivational quotes**, **recommendations**, and maintains a **prediction history**.

---

##  Features
- Predicts mood: **Happy, Sad, Neutral**
- Interactive UI using **Streamlit**
- Uses **Random Forest Classifier**
- Displays mood with colors and emojis
- Shows motivational quotes and recommendations
- Stores predictions in a history file
- Visualizes mood history with charts
- Allows downloading mood history as CSV

---

##  Machine Learning Model
- Algorithm: **Random Forest Classifier**
- Encoding: **Label Encoding** for categorical features
- Features used:
  - Temperature
  - Humidity
  - Time of Day
- Target:
  - Mood

---

##  Tech Stack
- Python
- Streamlit
- Pandas
- Scikit-learn
- Random Forest Classifier

---

##  Project Structure
MoodPredictorProject/
│── app.py
│── data.csv
│── history.csv
│── requirements.txt
│── README.md

yaml
Copy code

---

##  How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Run the Streamlit app
bash
Copy code
streamlit run app.py
 Output
Displays predicted mood with emojis

Shows mood-based quotes and suggestions

Stores predictions in history.csv

Bar chart visualization of mood history

Downloadable mood history CSV file

 Use Cases
Mental health awareness

Mood tracking applications

Beginner-friendly ML + Streamlit project

Academic mini project / portfolio project

 Author
Lathika
GitHub: https://github.com/lathika-3012

 Acknowledgement
This project was developed as part of a Machine Learning learning initiative using Python and Streamlit.















