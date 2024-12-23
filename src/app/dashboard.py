import streamlit as st
import pandas as pd

# Title
st.title("🧬 GeneScope AI Dashboard")

# Upload Dataset
uploaded_file = st.file_uploader("Upload Genetic Dataset", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview:")
    st.dataframe(data.head())

    # Display basic analytics
    st.write("### Basic Data Analytics:")
    st.write(data.describe())

    # Visualization
    st.write("### Gene Expression Distribution:")
    st.bar_chart(data['gene_expression'])

    # Simulated Prediction
    st.write("### AI Prediction Example:")
    st.write("Health Status Prediction: **Healthy**")
    st.write("Disease Risk Prediction: **Low Risk**")
