import streamlit as st
import pandas as pd

from bin.Analyse.Traffic import Traffic
from bin.Analyse.Weather import Weather
from bin.Analyse.Sales import Sales

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Data Dashboard", layout="wide")

# ------------------ TITLE ------------------
st.title("📊 Smart Data Dashboard")

# ------------------ FILE UPLOAD ------------------
file = st.file_uploader(label="Upload your dataset (CSV or Excel)", type=["csv", "xlsx", "xls"])

df = None

print("File uploaded:", file)

set = int(0)  # Default to Traffic if no file is uploaded
if file is not None:
    try:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.success("✅ File uploaded successfully!")
        if "traffic" in file.name.lower():
            st.info("Loaded Traffic dataset.")
            set = int(0)
        elif "weather" in file.name.lower():
            st.info("Loaded Weather dataset.")
            set = int(1)
        elif "sales" in file.name.lower():
            st.info("Loaded Sales dataset.")
            set = int(2)
        else:
            set = int(3)
    except Exception as e:
        st.error(f"Error loading file: {e}")


base = st.selectbox(
    "Select a base for your analysis",
    options=["Traffic", "Weather", "Sales","others"],
    index = set
)
# ------------------ LAYOUT ------------------
left, right = st.columns([1, 2])

# ------------------ LEFT PANEL ------------------
with left:
    st.subheader("📂 Data Panel")

    if df is not None:
        st.write("**Rows:**", df.shape[0])
        st.write("**Columns:**", df.shape[1])

        # Column selector (generic)
        selected_columns = st.multiselect(
            "Select columns",
            options=df.columns.tolist(),
            default=df.columns.tolist()
        )

        st.markdown("### Preview")
        st.dataframe(df[selected_columns].head(3600) if selected_columns else df.head())

    else:
        st.info("Upload a dataset to begin.")

# ------------------ RIGHT PANEL ------------------
with right:
    st.subheader("📊 Analytics Panel")

    if df is not None:

        # ---------- PLACEHOLDERS ----------

        if base is "Traffic":
            analysis_type = st.multiselect(
            "Select analysis type",
            options=Traffic.analysis_options

            )
        elif base is "Weather":
            analysis_type = st.multiselect(
            "Select analysis type",
            options=Weather.analysis_options
            )
        elif base is "Sales":
            analysis_type = st.multiselect(
            "Select analysis type",
            options=Sales.analysis_options
            )
        else:            analysis_type = st.multiselect(
            "Select analysis type",
            options=["Summary Statistics", "Correlation Matrix", "Distribution Plots", "Time Series Analysis", "Custom Analysis"]
            )

        st.markdown("### Insights")
        st.info("Add your insights here")

        st.markdown("### Charts")
        chart_area = st.container()
        if base is "Traffic":
            Traffic(df,st,analysis_type)
        if base is "Weather":
            Weather(df,st,analysis_type)
        if base is "Sales":
            Sales(df,st,analysis_type)
        st.markdown("### Advanced Analysis")
        analysis_area = st.container()

        st.markdown("### Results / Predictions")
        result_area = st.container()

    else:
        st.info("Upload data to view analytics.")
