# Smog Level Prediction Application

A machine learning web app to predict vehicle smog levels and raise environmental awareness.
<br>Developed as part of an Introduction to AI course.

# Project Overview

This application uses a Decision Tree Classifier to predict smog levels based on vehicle data.
<br>It features an interactive interface built with Streamlit to make smog level assessment accessible and user-friendly.
<br>Live Demo: Streamlit App
<br>GitHub Repo: AI_Final_Project

# Features

Predict smog levels from real vehicle emission data.
<br>Train and test using a Decision Tree Classifier.
<br>Fully interactive app using Streamlit.
<br>Easy to use with real-time feedback on predictions.
<br>Promotes environmental awareness and sustainability education.

# Project Structure
<br>📦 AI_Final_Project
<br>├── Final_Project.py         # Streamlit app and ML model
<br>├── CO2_emission.csv         # Vehicle emission dataset
<br>├── requirements.txt         # Dependencies
<br>├── SmogNY.jpg               # Smog reference image
<br>├── README.md                # Project documentation

# Installation
<br>Install dependencies
<br>pip install -r requirements.txt
<br>Run the Streamlit app
<br>streamlit run Final_Project.py

# Dependencies
<br>streamlit
<br>pandas
<br>scikit-learn
<br>(See requirements.txt)

# Dataset
<br>We used CO2_emission.csv, which includes multiple features related to vehicle emissions, including engine size, fuel consumption, and CO2 emissions.

# Model
<br>Algorithm: Decision Tree Classifier
<br>Goal: Classify vehicles into smog levels based on emission data
<br>Output: Smog Level (e.g., Low, Moderate, High)

# Motivation
<br>Smog affects millions of lives every year. This tool aims to:
<br>Help users understand their vehicle's environmental impact.
<br>Encourage low-emission choices.
<br>Promote AI's role in solving real-world environmental issues.

📜 License
<br>This project is licensed for academic and educational use.
