import streamlit as st
import pandas as pd

st.set_page_config(page_title="EcoInsight AI", layout="wide")

# -----------------------------
# Sidebar Navigation
# -----------------------------
page = st.sidebar.radio("Navigation", ["Home", "How It Works", "Climate Analysis"])

# -----------------------------
# HOME PAGE
# -----------------------------
if page == "Home":

    st.title("EcoInsight AI")
    st.write("AI-powered system for climate analysis and sustainability insights.")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("ML Analysis\n\nAnalyzes climate patterns")

    with col2:
        st.info(" AI Report\n\nGenerates sustainability insights")

    with col3:
        st.warning(" Sustainability\n\nSupports climate decisions")

# -----------------------------
# HOW IT WORKS (NEW)
# -----------------------------
elif page == "How It Works":

    st.title(" How EcoInsight AI Works")

    st.markdown("### 3 Simple Steps to Understand Climate Data")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 1️ Input Climate Data")
        st.write("Users enter environmental data such as temperature, CO₂ levels, and rainfall.")

    with col2:
        st.markdown("### 2️ AI-Based Analysis")
        st.write("Machine learning analyzes patterns and identifies environmental risk levels.")

    with col3:
        st.markdown("### 3️ Report Generation")
        st.write("Generative AI converts results into easy-to-understand sustainability insights.")

    st.markdown("---")

    st.info("This system simplifies complex climate analysis into understandable insights for better decision-making.")
    st.markdown("##  How Risk is Analyzed")

    st.write("""
The system analyzes climate data using predefined thresholds and AI-based logic:

- High Risk → Temperature > 35°C OR CO₂ > 450 ppm  
- Medium Risk → Temperature between 25°C–35°C OR CO₂ between 380–450 ppm  
- Low Risk → Stable environmental conditions below threshold values  

This classification helps in identifying environmental risk levels quickly and effectively.
""")
    
    

# -----------------------------
# CLIMATE ANALYSIS PAGE
# -----------------------------
elif page == "Climate Analysis":

    st.title(" Climate Data Analysis")

    st.markdown("Enter climate data to analyze environmental risk and generate insights.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        temperature = st.slider("🌡️ Temperature (°C)", 10, 50, 30)
        co2 = st.slider("🏭 CO2 Level (ppm)", 300, 600, 400)

    with col2:
        rainfall = st.slider("🌧️ Rainfall (mm)", 0, 300, 100)

    # -----------------------------
    # AI Logic
    # -----------------------------
    def classify_risk(temp, co2, rain):
        if temp > 35 or co2 > 450:
            return "High"
        elif temp > 25 or co2 > 380:
            return "Medium"
        else:
            return "Low"

    # -----------------------------
    # LLM Report
    # -----------------------------
    def generate_report(temp, co2, rain, risk):
        if risk == "High":
            return f"High climate risk detected. Temperature ({temp}°C) and CO2 ({co2} ppm) are significantly high. Immediate action is required."
        elif risk == "Medium":
            return f"Moderate climate risk observed. Temperature ({temp}°C) and CO2 ({co2} ppm) are elevated. Preventive measures are recommended."
        else:
            return f"Low climate risk. Environmental conditions are stable with temperature {temp}°C and CO2 {co2} ppm."

    if st.button("🔍 Analyze Climate Data"):

        risk = classify_risk(temperature, co2, rainfall)
        report = generate_report(temperature, co2, rainfall, risk)

        st.markdown("---")
        st.markdown("## Results")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🌡️ Risk Level")
            if risk == "High":
                st.error(risk)
            elif risk == "Medium":
                st.warning(risk)
            else:
                st.success(risk)

        with col2:
            st.subheader("📄 Sustainability Report")
            st.write(report)

        st.markdown("---")

        st.subheader("📊 Data Visualization")

        data = pd.DataFrame({
            "Parameter": ["Temperature", "CO2", "Rainfall"],
            "Value": [temperature, co2, rainfall]
        })

        st.bar_chart(data.set_index("Parameter"))

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("AI + ML + LLM Concept | Mini Project based on AI for Earth")