import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout="wide")

st.markdown(
    """
    <style>
        .main {
            background-color: #0d1117;
        }
        .block-container {
            padding: 3rem 2rem;
            border-radius: 12px;
            background-color: #161b22;
            box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1);
        }
        h1, h2, h3, h4, h5, h6 {
            color: #58a6ff;
        }
        .stButton>button {
            border: none;
            border-radius: 8px;
            background-color: #238636;
            color: white;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #2ea043;
            cursor: pointer;
        }
        .stDataFrame, .stTable {
            border-radius: 10px;
            overflow: hidden;
            background-color: #0d1117;
            color: white;
        }
        .stRadio>label, .stCheckbox>label {
            font-weight: bold;
            color: #c9d1d9;
        }
        .stDownloadButton>button {
            background-color: #1f6feb;
            color: white;
        }
        .stDownloadButton>button:hover {
            background-color: #3b82f6;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚀 Advanced Data Sweeper")
st.write("Easily transform and clean your CSV and Excel files with powerful tools.")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_extension = os.path.splitext(file.name)[-1].lower()
        
        if file_extension == ".csv":
            df = pd.read_csv(file)
        elif file_extension == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_extension}")
            continue
        
        with st.expander(f"📂 File: {file.name} ({file.size / 1024:.2f} KB)"):
            st.dataframe(df.head())
            
            st.subheader("🛠️ Data Cleaning Options")
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"🧹 Remove Duplicates", key=f"dedup_{file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("Duplicates removed!")
            with col2:
                if st.button(f"📊 Fill Missing Values", key=f"fillna_{file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("Missing values filled!")
            
            st.subheader("🎯 Select Columns to Convert")
            columns = st.multiselect(f"Choose Columns", df.columns, default=df.columns, key=f"cols_{file.name}")
            df = df[columns]
            
            st.subheader("📊 Data Visualization")
            if st.checkbox(f"Show Visualization", key=f"viz_{file.name}"):
                numeric_cols = df.select_dtypes(include='number').columns
                if not numeric_cols.empty:
                    st.bar_chart(df[numeric_cols].iloc[:, :2])
                else:
                    st.warning("No numeric columns available for visualization.")
            
            st.subheader("🔄 Convert File")
            conversion_type = st.radio(f"Convert to:", ["CSV", "Excel"], key=f"convert_{file.name}")
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_extension, ".csv")
                    mime_type = "text/csv"
                elif conversion_type == "Excel":
                    df.to_excel(buffer, index=False, engine='openpyxl')
                    file_name = file.name.replace(file_extension, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                buffer.seek(0)
                st.download_button(label=f"⬇️ Download {file_name}", data=buffer, file_name=file_name, mime=mime_type)

st.success("✅ Processing complete!")
