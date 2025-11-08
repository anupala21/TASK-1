# pandas_localhost_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Employee Data Dashboard", layout="wide")

# --- Title ---
st.title("📊 Employee Data Analysis Dashboard")
st.markdown("This web app uses **Pandas** and **Streamlit** to analyze and visualize employee data interactively.")

# --- Create Sample DataFrame ---
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 22],
    "Salary": [50000, 60000, 80000, 90000, 45000],
    "Department": ["HR", "IT", "Finance", "IT", "HR"]
}
df = pd.DataFrame(data)

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filters")
min_salary = st.sidebar.slider("Minimum Salary", int(df["Salary"].min()), int(df["Salary"].max()), 50000)
selected_dept = st.sidebar.multiselect("Select Department(s)", df["Department"].unique(), df["Department"].unique())

# --- Filter Data ---
filtered_df = df[(df["Salary"] >= min_salary) & (df["Department"].isin(selected_dept))]

# --- Display Data ---
st.subheader("📋 Filtered Employee Data")
st.dataframe(filtered_df)

# --- Descriptive Statistics ---
st.subheader("📈 Descriptive Statistics")
st.write(filtered_df.describe())

# --- Add Bonus Column ---
filtered_df["Bonus"] = filtered_df["Salary"] * 0.10

# --- Visualizations ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Salary by Employee")
    fig1, ax1 = plt.subplots()
    ax1.bar(filtered_df["Name"], filtered_df["Salary"], color="skyblue")
    ax1.set_xlabel("Employee Name")
    ax1.set_ylabel("Salary")
    ax1.set_title("Salary Comparison")
    st.pyplot(fig1)

with col2:
    st.subheader("🏢 Average Salary by Department")
    avg_salary = filtered_df.groupby("Department")["Salary"].mean()
    fig2, ax2 = plt.subplots()
    avg_salary.plot(kind="bar", color="orange", ax=ax2)
    ax2.set_xlabel("Department")
    ax2.set_ylabel("Average Salary")
    ax2.set_title("Average Salary by Department")
    st.pyplot(fig2)

# --- Export Option ---
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_employees.csv",
    mime="text/csv"
)

