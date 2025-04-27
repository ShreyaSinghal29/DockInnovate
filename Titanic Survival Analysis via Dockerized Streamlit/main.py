import streamlit as st
import pandas as pd
import joblib

# Load the trained model
try:
    model = joblib.load('titanic_model.pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Page Configuration
st.set_page_config(page_title="Will You Survive? | Titanic Predictor", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
    .header {
        font-size: 44px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtext {
        font-size: 18px;
        text-align: center;
        color: #555;
        font-style: italic;
        margin-bottom: 40px;
    }
    .input-section {
        background: #f2f6fc;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True
)

# Header
st.markdown('<div class="header">🚢 Titanic: Will You Survive?</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Fill out the details and find out your fate!</div>', unsafe_allow_html=True)

# Input Form
with st.container():
    with st.form(key="survival_form"):
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)

        with col1:
            pclass = st.selectbox("Ticket Class", options=[1, 2, 3], index=2)
            age = st.slider("Passenger Age", min_value=0, max_value=80, value=30)
            sex = st.radio("Gender", options=["male", "female"], horizontal=True)

        with col2:
            sibsp = st.number_input("Siblings/Spouse Aboard", min_value=0, max_value=10, value=0)
            parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)
            fare = st.slider("Ticket Fare ($)", min_value=0, max_value=500, value=50)

        submitted = st.form_submit_button("Predict 🎯")
        st.markdown('</div>', unsafe_allow_html=True)

# Prediction Logic
if submitted:
    with st.spinner("Analyzing your survival chances..."):
        try:
            sex_binary = 1 if sex == "female" else 0
            input_data = pd.DataFrame(
                [[pclass, sex_binary, age, sibsp, parch, fare]],
                columns=['Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare']
            )
            prediction = model.predict(input_data)
            outcome = "🎉 You would have survived!" if prediction[0] == 1 else "😢 Unfortunately, you wouldn't survive."

            if prediction[0] == 1:
                st.success(outcome)
            else:
                st.error(outcome)

        except Exception as error:
            st.error(f"Prediction failed due to: {error}")
