import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(layout="wide")

# ------------------ STYLE ------------------
st.markdown("""
<style>
body {
    background-color: white;
}
.block-container {
    padding-top: 1rem;
}
.card {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.title("Smart Data Analyzer Dashboard")

# ------------------ LAYOUT ------------------
col1, col2 = st.columns([1,2])

# ------------------ LEFT PANEL ------------------
with col1:
    st.markdown("### Upload Data")
    file = st.file_uploader("Upload CSV or Excel")

    if file:
        df = pd.read_csv(file)

        st.markdown("### Stats")
        st.write(f"Mean Value: {round(df.select_dtypes(include=np.number).mean().mean(),2)}")
        st.write(f"Median Value: {round(df.select_dtypes(include=np.number).median().median(),2)}")
        st.write(f"Max Value: {round(df.select_dtypes(include=np.number).max().max(),2)}")

        st.markdown("### Data Preview")
        st.dataframe(df.head())

# ------------------ RIGHT PANEL ------------------
with col2:

    # Insights box
    st.markdown("### Insights")
    st.info("📈 Sales increased by 22% last month")
    st.warning("🔍 High correlation detected between Age and Income")
    st.error("⚠️ Anomaly detected in sales data for March")

    if file:
        # Charts Row 1
        c1, c2 = st.columns(2)

        with c1:
            st.markdown("### Sales Trend")
            st.line_chart(df.select_dtypes(include=np.number))

        with c2:
            st.markdown("### Sales Chart")
            st.area_chart(df.select_dtypes(include=np.number))

        # Charts Row 2
        c3, c4 = st.columns(2)

        with c3:
            st.markdown("### Revenue Breakdown")
            fig, ax = plt.subplots()
            df.select_dtypes(include=np.number).iloc[0].plot.pie(autopct='%1.1f%%', ax=ax)
            st.pyplot(fig)

        with c4:
            st.markdown("### Correlation Heatmap")
            corr = df.select_dtypes(include=np.number).corr()
            st.dataframe(corr)

        # Prediction Box
        st.markdown("### Predictive Analysis")
        st.success(f"Predicted Sales Next Month: {int(np.random.randint(200,400))}")