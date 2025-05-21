🚗 Smog Level Prediction Application

A machine learning web app to predict vehicle smog levels and raise environmental awareness.
Developed as part of an Introduction to AI course.
📌 Project Overview

This application uses a Decision Tree Classifier to predict smog levels based on vehicle data.
It features an interactive interface built with Streamlit to make smog level assessment accessible and user-friendly.
Live Demo: Streamlit App
GitHub Repo: AI_Final_Project
🔍 Features

Predict smog levels from real vehicle emission data.
Train and test using a Decision Tree Classifier.
Fully interactive app using Streamlit.
Easy to use with real-time feedback on predictions.
Promotes environmental awareness and sustainability education.
📁 Project Structure
📦 AI_Final_Project
├── Final_Project.py         # Streamlit app and ML model
├── CO2_emission.csv         # Vehicle emission dataset
├── requirements.txt         # Dependencies
├── SmogNY.jpg               # Smog reference image
└── README.md                # Project documentation
⚙️ Installation
# Install dependencies
pip install -r requirements.txt
# Run the Streamlit app
streamlit run Final_Project.py
🧪 Dependencies
streamlit
pandas
scikit-learn
(See requirements.txt)
📈 Dataset
We used CO2_emission.csv, which includes multiple features related to vehicle emissions, including engine size, fuel consumption, and CO2 emissions.
📊 Model
Algorithm: Decision Tree Classifier
Goal: Classify vehicles into smog levels based on emission data
Output: Smog Level (e.g., Low, Moderate, High)
🌍 Motivation
Smog affects millions of lives every year. This tool aims to:
Help users understand their vehicle's environmental impact.
Encourage low-emission choices.
Promote AI's role in solving real-world environmental issues.
📜 License
This project is licensed for academic and educational use.
