
import streamlit as st
import pandas as pd
import joblib
from streamlit_lottie import st_lottie
import requests

# Load model and features
model = joblib.load("diabetes_model.pkl")
features = joblib.load("model_features.pkl")

# Set page config
st.set_page_config(
    page_title="GlucoCheck Pro | Diabetes Risk Assessment",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🩺"
)

# Load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

doctor_anim = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_5njp3vgg.json")
health_anim = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_0skurerf.json")

# Apply dark theme styles
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Montserrat:wght@500;600;700&display=swap');

    /* Base Styles */
    * {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: #121212;
        color: #FFFFFF;
    }

    /* Header Styles */
    .header {
        background: linear-gradient(135deg, #2c3e50 0%, #4a148c 100%);
        padding: 2rem 1rem;
        border-radius: 0 0 20px 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        text-align: center;
        margin: -1rem -1rem 2rem -1rem;
    }

    .app-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        margin: 0;
        color: white !important;
        letter-spacing: 0.5px;
    }

    .app-subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.3rem;
        font-weight: 400;
        margin-top: 0.5rem;
        color: white !important;
        opacity: 0.9;
    }

    /* Card Styles */
    .card {
        background: #1E1E1E;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
        border: 1px solid #333;
    }

    .section-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        color: #FFFFFF !important;
        position: relative;
    }

    .section-title:after {
        content: "";
        position: absolute;
        bottom: -10px;
        left: 0;
        width: 60px;
        height: 4px;
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        border-radius: 2px;
    }

    /* Input Fields */
    .input-label {
        font-weight: 500;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 8px;
        color: #FFFFFF !important;
        font-size: 1rem;
    }

    /* Result Cards */
    .result-card {
        background: #252525;
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 30px rgba(0,0,0,0.2);
    }

    .high-risk {
        border-left: 6px solid #ff4d4d;
    }

    .low-risk {
        border-left: 6px solid #4CAF50;
    }

    .risk-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }

    .high-risk .risk-title {
        color: #ff4d4d !important;
    }

    .low-risk .risk-title {
        color: #27ae60 !important;
    }

    .result-card p {
        font-size: 1.1rem;
        color: #EEEEEE !important;
    }

    /* Recommendation Cards */
    .recommendation-card {
        background: #252525;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        border: 1px solid #444;
    }

    .recommendation-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #FFFFFF !important;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        color: white !important;
        font-weight: 600;
        padding: 12px 30px;
        border: none !important;
        border-radius: 50px;
        box-shadow: 0 5px 15px rgba(106, 17, 203, 0.3);
        width: 100%;
        transition: all 0.3s;
        font-size: 1rem;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(106, 17, 203, 0.4);
    }

    /* Input Fields Styling */
    .stNumberInput>div>div>input, .stTextInput>div>div>input {
        background: #252525 !important;
        color: #FFFFFF !important;
        border: 1px solid #444 !important;
    }

    /* Lists */
    ul {
        color: #EEEEEE !important;
        margin-top: 0.5rem;
        padding-left: 1.2rem;
        line-height: 1.6;
    }

    li {
        margin-bottom: 0.5rem;
        font-size: 1rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        font-size: 0.9rem;
        margin-top: 2rem;
        color: #AAAAAA !important;
    }

    /* Fix Streamlit spacing */
    .stApp > div {
        padding-top: 0;
    }
    .block-container {
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ====== HEADER ====== #
st.markdown("""
    <div class="header">
        <h1 class="app-title">GlucoCheck Pro</h1>
        <p class="app-subtitle">Advanced Diabetes Risk Assessment Tool</p>
    </div>
""", unsafe_allow_html=True)

# ====== MAIN CONTENT ====== #
with st.container():
    st.markdown("""
        <div class="card">
            <div class="section-title">Patient Health Assessment</div>
    """, unsafe_allow_html=True)

    # Medical icons and labels
    medical_icons = {
        'Pregnancies': '🤰',
        'Glucose': '🩸',
        'BloodPressure': '💓',
        'SkinThickness': '📏',
        'Insulin': '💉',
        'BMI': '⚖️',
        'DiabetesPedigreeFunction': '🧬',
        'Age': '👴'
    }

    medical_labels = {
        'Pregnancies': 'Number of Pregnancies',
        'Glucose': 'Glucose Level (mg/dL)',
        'BloodPressure': 'Blood Pressure (mmHg)',
        'SkinThickness': 'Skin Thickness (mm)',
        'Insulin': 'Insulin Level (μU/mL)',
        'BMI': 'Body Mass Index (kg/m²)',
        'DiabetesPedigreeFunction': 'Diabetes Pedigree Score',
        'Age': 'Age (years)'
    }

    # Create 3 columns for inputs
    col1, col2, col3 = st.columns(3)
    inputs = []

    for i, feature in enumerate(features):
        label = f"""
        <div class="input-label">
            <span style="font-size: 1.3rem;">{medical_icons.get(feature, '📋')}</span>
            <span>{medical_labels.get(feature, feature)}</span>
        </div>
        """

        if i % 3 == 0:
            col = col1
        elif i % 3 == 1:
            col = col2
        else:
            col = col3

        col.markdown(label, unsafe_allow_html=True)
        val = col.number_input(
            "",
            min_value=0.0,
            step=0.1,
            key=feature,
            label_visibility="collapsed"
        )
        inputs.append(val)

    # Patient name input
    st.markdown("""
        <div class="input-label" style="margin-top: 1.5rem;">
            <span style="font-size: 1.3rem;">👤</span>
            <span>Patient Full Name</span>
        </div>
    """, unsafe_allow_html=True)
    name = st.text_input("", placeholder="Enter patient's name", label_visibility="collapsed")

    # Analyze button
    analyze_btn = st.button("Analyze Diabetes Risk", type="primary")

    st.markdown("</div>", unsafe_allow_html=True)  # Close card

# Results section
if analyze_btn and name:
    with st.spinner('🔍 Analyzing health data...'):
        input_df = pd.DataFrame([inputs], columns=features)
        prediction = model.predict(input_df)[0]
        confidence = model.predict_proba(input_df)[0][1]

        if prediction == 1:
            st.markdown(f"""
            <div class="result-card high-risk">
                <div class="risk-title">⚠️ High Diabetes Risk Detected</div>
                <p>Patient <strong>{name}</strong> shows a <strong>{confidence*100:.1f}% likelihood</strong> of diabetes risk.</p>
            </div>
            """, unsafe_allow_html=True)

            with st.container():
                st.markdown("""
                <div class="recommendation-card">
                    <div class="recommendation-title">📋 Medical Recommendations</div>
                    <ul>
                        <li>Consult an endocrinologist immediately for comprehensive evaluation</li>
                        <li>Monitor fasting blood glucose levels daily</li>
                        <li>Follow a strict low-carbohydrate, high-fiber diet</li>
                        <li>Engage in 30 minutes of moderate exercise daily</li>
                        <li>Schedule quarterly HbA1c tests</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

                if doctor_anim:
                    st_lottie(doctor_anim, height=250, key="doctor-anim")

        else:
            st.markdown(f"""
            <div class="result-card low-risk">
                <div class="risk-title">✅ Low Diabetes Risk</div>
                <p>Patient <strong>{name}</strong> has a <strong>{(1-confidence)*100:.1f}% probability</strong> of being low-risk.</p>
            </div>
            """, unsafe_allow_html=True)

            with st.container():
                st.markdown("""
                <div class="recommendation-card">
                    <div class="recommendation-title">🌟 Preventive Care Tips</div>
                    <ul>
                        <li>Maintain a Mediterranean-style diet rich in whole foods</li>
                        <li>Engage in 150 minutes of aerobic activity weekly</li>
                        <li>Get annual comprehensive metabolic panels</li>
                        <li>Practice stress-reduction techniques like meditation</li>
                        <li>Maintain healthy sleep patterns (7-9 hours nightly)</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

                if health_anim:
                    st_lottie(health_anim, height=250, key="health-anim")

# Footer with medical icon
st.markdown("""
    <div class="footer">
        🚑 © 2025 GlucoCheck Pro | Developed with ❤️ by Healthcare AI Team
    </div>
""", unsafe_allow_html=True)
