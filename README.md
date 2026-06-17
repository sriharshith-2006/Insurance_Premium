# 🏥 Insurance Premium Prediction System

An end-to-end Machine Learning project that predicts the **insurance premium category** (Low / Medium / High) based on user details like age, BMI, income, lifestyle, and city.

---

## 🔗 Live Demo
| Service | Link |
|---|---|
| Frontend (Streamlit) | https://insurancepremium1.streamlit.app |
| Backend (FastAPI Docs) | https://insurance-premium-3-qmw7.onrender.com/docs |

---

## 🏗️ Project Architecture

```
User → Streamlit UI → FastAPI Backend → ML Pipeline → Prediction
                                              ↑
                              Feature Engineering (BMI, Age Group,
                              City Tier, Lifestyle Risk, OHE)
```

---

## ⚙️ Tech Stack
| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Data Processing | Pandas, NumPy |
| ML Model | Scikit-learn (Logistic Regression) |
| ML Pipeline | ColumnTransformer + Pipeline |
| Backend API | FastAPI + Uvicorn |
| Frontend UI | Streamlit |
| Model Serialization | Pickle |
| Deployment | Render (API) + Streamlit Cloud (UI) |

---

## 🧠 ML Pipeline

```
Raw Input
    │
    ▼
Feature Engineering
    ├── BMI = weight / height²
    ├── Age Group (Young / Middle / Senior)
    ├── Lifestyle Risk Score
    └── City Tier (Tier 1 / 2 / 3)
    │
    ▼
ColumnTransformer
    ├── OneHotEncoder → categorical features
    └── PassThrough   → numerical features
    │
    ▼
Logistic Regression
    │
    ▼
Predicted Category (Low / Medium / High)
```

---

## 📂 Project Structure

```
Insurance_Premium/
│
├── backend/
│   ├── main.py              # FastAPI app
│   ├── model.pkl            # Trained ML model
│   └── requirements.txt     # Backend dependencies
│
├── frontend/
│   ├── app.py               # Streamlit UI
│   └── requirements.txt     # Frontend dependencies
│
├── notebooks/
│   └── model.ipynb          # Model training notebook
│
└── README.md
```

---

## 📊 Input Features

| Feature | Type | Description |
|---|---|---|
| Age | Number | Age in years |
| Weight | Number | Weight in kg |
| Height | Number | Height in metres |
| Income | Number | Annual income in LPA |
| Smoker | Boolean | Yes / No |
| City | Text | City of residence |
| Occupation | Dropdown | Employment type |

---

## ⚙️ Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/sriharshith-2006/Insurance_Premium
cd Insurance_Premium
```

### 2. Run the FastAPI backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
- API: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`

### 3. Run the Streamlit frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## 👨‍💻 Developed By
AI & Data Science Student
