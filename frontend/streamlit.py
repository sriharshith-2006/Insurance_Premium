import streamlit as st
import requests

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="💰",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("🏥 Insurance Premium Predictor")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "About", "Prediction"]
)

# ---------------- HOME PAGE ---------------- #
if page == "Home":

    st.title("Insurance Premium Prediction System")

    st.markdown("""
    ### Predict Insurance Premium Category using AI

    This application predicts insurance premium category based on:

    - Age  
    - Weight  
    - Height  
    - Income  
    - Smoking Habit  
    - City  
    - Occupation  

    ---
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model", "Logistic Regression")

    with col2:
        st.metric("Features", "7")

    with col3:
        st.metric("API", "FastAPI")



# ---------------- ABOUT PAGE ---------------- #
elif page == "About":

    st.title("About Project")

    st.write("""
    This project predicts Insurance Premium Categories using Machine Learning.

    ### Tech Stack
    - Python
    - Pandas
    - Scikit-Learn
    - FastAPI
    - Streamlit

    ### ML Pipeline
    - Feature Engineering
    - One Hot Encoding
    - Logistic Regression
    - FastAPI Deployment

    ### Developed By
    AI & Data Science Student
    """)


# ---------------- PREDICTION PAGE ---------------- #
elif page == "Prediction":

    st.title("Insurance Premium Prediction")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input("Age", min_value=1, max_value=100, value=25)

        weight = st.number_input("Weight (kg)", min_value=20.0, value=70.0)

        height = st.number_input("Height (m)", min_value=1.0, value=1.75)

        income = st.number_input("Income (LPA)", min_value=1.0, value=10.0)

    with col2:

        smoker = st.selectbox("Smoker", [True, False])

        city = st.text_input("City")

        occupation = st.selectbox(
            "Occupation",
            [
                "retired",
                "freelancer",
                "student",
                "government_job",
                "business_owner",
                "unemployed",
                "private_job"
            ]
        )

    st.divider()

    # ---------------- PREDICTION BUTTON ---------------- #
    if st.button("🔮 Predict Premium Category"):

        payload = {
            "age": age,
            "weight": weight,
            "height": height,
            "income_lpa": income,
            "smoker": smoker,
            "city": city,
            "occupation": occupation
        }

        try:
            with st.spinner("Predicting..."):

                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    json=payload
                )

                st.write(response.status_code)
                st.write(response.text)

            if response.status_code == 200:
                result = response.json()

                st.success("Prediction Successful")

                st.markdown("## Predicted Category")
                st.info(result.get("prediction", "No prediction returned"))

            else:
                st.error("API Error")
                st.write(response.text)

        except Exception as e:
            st.error("FastAPI server not running")
            st.write(str(e))
            st.write("PAYLOAD SENT:", payload)