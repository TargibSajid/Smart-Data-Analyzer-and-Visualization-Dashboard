import streamlit as st
import pandas as pd

from bin.Analyse.Traffic import Traffic
from bin.Analyse.Weather import Weather
from bin.Analyse.Sales import Sales

st.set_page_config(page_title="Data Dashboard", layout="wide")
st.title("📊 Smart Data Dashboard")

file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx", "xls"])

df = None
dataset_index = 0

if file is not None:
    try:
        
        if file.name.endswith(".csv"):
             df = pd.read_csv(file)
             st.success("✅ File uploaded successfully!")
        elif file.name.endswith((".xlsx", ".xls")):
             df = pd.read_excel(file)
             st.success("✅ File uploaded successfully!")

        else:
             st.error("❌ Unsupported file type!")


        if "traffic" in file.name.lower():
            st.info("Loaded Traffic dataset.")
            dataset_index = 0
        elif "weather" in file.name.lower():
            st.info("Loaded Weather dataset.")
            dataset_index = 1
        elif "sales" in file.name.lower():
            st.info("Loaded Sales dataset.")
            dataset_index = 2
        else:
            dataset_index = 3

    except Exception as e:
        st.error(f"Error loading file: {e}")

base = st.selectbox(
    "Select a base for your analysis",
    ["Traffic", "Weather", "Sales", "others"],
    index=dataset_index
)

left, right = st.columns([1, 2])

with left:
    st.subheader("📂 Data Panel")

    if df is not None:
        st.write("**Rows:**", df.shape[0])
        st.write("**Columns:**", df.shape[1])

        selected_columns = st.multiselect(
            "Select columns",
            options=df.columns.tolist(),
            default=df.columns.tolist()
        )

        st.markdown("### Preview")
        st.dataframe(df[selected_columns].head(3600) if selected_columns else df.head())
    else:
        st.info("Upload a dataset to begin.")

with right:
    st.subheader("📊 Analytics Panel")

    if df is not None:

        if base == "Traffic":
            analysis_type = st.multiselect("Select analysis type", Traffic.analysis_options)
        elif base == "Weather":
            analysis_type = st.multiselect("Select analysis type", Weather.analysis_options)
        elif base == "Sales":
            analysis_type = st.multiselect("Select analysis type", Sales.analysis_options)
        else:
            analysis_type = st.multiselect(
                "Select analysis type",
                ["Summary Statistics", "Correlation Matrix", "Distribution Plots", "Time Series Analysis", "Custom Analysis"]
            )

        st.markdown("### Charts")
        if base == "Traffic":
            Traffic(df, st, analysis_type)
        elif base == "Weather":
            Weather(df, st, analysis_type)
        elif base == "Sales":
            Sales(df, st, analysis_type)

        st.markdown("### Insights")
        if base == "Traffic":
            st.info(Traffic.insights if Traffic.insights.strip() else "Select traffic analysis options to generate insights.")
        elif base == "Weather":
            st.info(Weather.insights if hasattr(Weather, "insights") and Weather.insights.strip() else "Select weather analysis options to generate insights.")
        elif base == "Sales":
            st.info(Sales.insights if hasattr(Sales, "insights") and Sales.insights.strip() else "Select sales analysis options to generate insights.")
        else:
            st.info("Insights are not available for this dataset type yet.")

        st.markdown("### Advanced Analysis & Predictions")
        st.warning("Advanced analysis and predictions will be available in future updates. Machine learning models will be added in future updates.")

        st.markdown("### Results")
        if base == "Traffic":
            st.success(Traffic.results if Traffic.results.strip() else "No traffic results yet.")
        elif base == "Weather":
            st.success(Weather.results if Weather.results.strip() else "No weather results yet.")
        elif base == "Sales":
            st.success(Sales.results if Sales.results.strip() else "No sales results yet.")
        else:
            st.success("No specific analysis results available for this dataset.")
    else:
        st.info("Upload data to view analytics.")