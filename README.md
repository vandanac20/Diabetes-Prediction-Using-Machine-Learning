## 🩺 Diabetes Prediction Using Machine Learning

This project uses machine learning to predict whether a patient is likely to have diabetes based on diagnostic input parameters. It utilizes a trained model and a standard scaler to provide predictions via a user interface.

## 📊 Dataset

The dataset used is diabetes.csv, which contains diagnostic measurements for patients. It includes features like:

Pregnancies

Glucose

BloodPressure

SkinThickness

Insulin

BMI

DiabetesPedigreeFunction

Age

Outcome (0 = Non-diabetic, 1 = Diabetic)

## 🧠 Machine Learning Model

The project includes:

Data preprocessing using scikit-learn's StandardScaler (saved as scaler.pkl)

A classification model (e.g., Logistic Regression, Random Forest, etc.) trained on diabetes.csv

Prediction pipeline using the trained model and scaler

## 💻 How to Run
# 1. Clone the Repository
git clone https://github.com/vandanac20/Diabetes-Prediction-Using-Machine-Learning.git

cd Diabetes-Prediction-Using-Machine-Learning

# 2. Install Requirements

pip install numpy pandas scikit-learn matplotlib streamlit

pip install flask

# 3. Run the App
python app.py

## 🧪 Example Input
Feature	Example Value:

Pregnancies	2

Glucose	120

BloodPressure	70

SkinThickness	25

Insulin	80

BMI	28.0

DiabetesPedigreeFunction	0.5

Age	30

Output: Diabetic or Not Diabetic

## ✅ Future Improvements

Add feature selection or PCA

Deploy on a cloud platform (Heroku, AWS, etc.)

Improve UI/UX design

Add user authentication
