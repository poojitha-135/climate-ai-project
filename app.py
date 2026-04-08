import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
        st.markdown(
            """
            <div style="background-color:#E8F5E9;padding:15px;border-radius:10px">
            <h4 style="color:#2E7D32;">📊 ML Analysis</h4>
            <p style="color:#1B5E20;">Analyzes climate patterns</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="background-color:#E3F2FD;padding:15px;border-radius:10px">
            <h4 style="color:#1565C0;">🤖 AI Report</h4>
            <p style="color:#0D47A1;">Generates sustainability insights</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style="background-color:#FFF3E0;padding:15px;border-radius:10px">
            <h4 style="color:#EF6C00;">🌱 Sustainability</h4>
            <p style="color:#E65100;">Supports climate decisions</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------
# HOW IT WORKS
# -----------------------------
elif page == "How It Works":

    st.title("How EcoInsight AI Works")
    st.markdown("### 3 Simple Steps to Understand Climate Data")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 1️⃣ Input Climate Data")
        st.write("Users enter environmental data such as temperature, CO₂ levels, and rainfall.")

    with col2:
        st.markdown("### 2️⃣ AI-Based Analysis")
        st.write("Machine learning analyzes patterns and identifies environmental risk levels.")

    with col3:
        st.markdown("### 3️⃣ Report Generation")
        st.write("Generative AI converts results into easy-to-understand sustainability insights.")

    st.markdown("---")

    st.markdown(
        """
        <div style="background-color:#E0F7FA;padding:15px;border-radius:10px;color:#006064;">
        This system simplifies complex climate analysis into understandable insights for better decision-making.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## How Risk is Analyzed")

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

    st.title("Climate Data Analysis")
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
    # Report Generation
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

        st.subheader("📊 Data Visualization")

        # ✅ ADD THIS (missing part)
        labels = ["Temperature", "CO2", "Rainfall"]
        values = [temperature, co2, rainfall]
        
        col1, col2, col3 = st.columns([1,2,1])
        
        with col2:
            fig, ax = plt.subplots(figsize=(4,2.5), dpi=100)
        
            ax.bar(labels, values)
            ax.set_title("Climate Data Overview", fontsize=10)
            ax.tick_params(labelsize=8)
        
            st.pyplot(fig, use_container_width=False)

        

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("AI + ML + LLM Concept | Mini Project based on AI for Earth")
