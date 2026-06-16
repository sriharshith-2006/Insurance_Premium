# 🏥 Insurance Premium Prediction System (ML + FastAPI + Streamlit)

An end-to-end Machine Learning project that predicts the **insurance premium category** based on user details like age, BMI, income, lifestyle, and city.

The project includes:
- Machine Learning model (Scikit-learn)
- Feature engineering pipeline (ColumnTransformer + Pipeline)
- Backend API (FastAPI)
- Frontend UI (Streamlit)

---

## 🚀 Live Features

- User-friendly Streamlit interface
- Real-time prediction using FastAPI
- Automated feature engineering
- BMI, age group, lifestyle risk calculation
- City tier classification
- One-hot encoding + ML pipeline

---

## 🧠 Problem Statement

Predict the **insurance premium category** (Low / Medium / High) based on:
- Age
- Weight & Height (BMI)
- Income
- Smoking habit
- City
- Occupation

---

## 🏗️ Project Architecture

---

## ⚙️ Tech Stack

- Python 
- Pandas
- Scikit-learn
- FastAPI 
- Streamlit 
- Pickle (Model Serialization)

---

## ML Pipeline

- Feature Engineering:
  - BMI = weight / height²
  - Age Group
  - Lifestyle Risk
  - City Tier
-Pipelining
   -Column Transformer
      - Encoding:
          - OneHotEncoder for categorical features
          - PassThrough for numerical features

    - Model:
        - Logistic Regression 

---

## 📂 Project Structure



insurance-project/
│
├── backend/
│   ├── main.py
│   ├── model.pkl
│   ├── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│
├── notebooks/
│   ├── model.ipynb 
│
├── README.md


3️⃣ Run Streamlit frontend
    streamlit run streamlit_app.py
  Sample Input
{
  "age": 25,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 10,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "Engineer"
}
📈 Output
Predicted Category: Medium Risk / High Risk / Low Risk
