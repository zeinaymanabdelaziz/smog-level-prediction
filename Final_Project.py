import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

data = pd.read_csv('CO2_emission.csv')
data.head()

X = data.drop(['Model_Year','Make','Model','Vehicle_Class','Smog_Level'],axis = 1)
y = data['Smog_Level']

label_encoder = LabelEncoder()
X['Transmission'] = label_encoder.fit_transform(X['Transmission'])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)

model = DecisionTreeClassifier(random_state = 42)
model.fit(X_train, y_train)

def predict_smog_level(features):
    # Convert features to DataFrame with proper column names
    newTestData = pd.DataFrame([features], columns=X.columns)
    predicted_label = model.predict(newTestData)[0]
    return predicted_label

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)

st.markdown("<h1 style='text-align: center; color: pink;'>Smog Level Prediction App</h1>",unsafe_allow_html = True)
st.image("SmogNY.jpg",use_column_width = True)
st.markdown("<h3 style='text-align: center; color: pink;'>Model Description: Decision Tree Model trained on Vehicle data</h3>",unsafe_allow_html = True)

st.markdown("<span style='color: #000080;'>Enter vehicle details here <br>(In format 'Engine_Size,Cylinders,Transmission,Fuel_Consumption_in_City,L/100 km,Fuel_Consumption_in_Hwy,L/100 km,Fuel_Consumption_comb,L/100km,CO2_Emissions')</span>",unsafe_allow_html = True)
text_input = st.text_input("", "",key = "text_input")

predict_button = st.button("Predict Smog Level")

if predict_button:
    try:
        text = text_input.split(",")
        # Convert text inputs to floats
        text = [float(val) if index != 2 else label_encoder.transform([val])[0] for index, val in enumerate(text)]
        predicted_smog_level = predict_smog_level(text)
        st.success(f"Predicted Smog Level: {predicted_smog_level}")
    except Exception as e:
        st.error("Please enter valid vehicle details in the specified format.")
        st.error(f"Error: {e}")

st.write(f"<span style='color: #000080;'>Accuracy: {accuracy * 100:.2f}%</span>",unsafe_allow_html = True)


