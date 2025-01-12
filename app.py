import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import numpy as np

data = pd.read_excel("Employees.xlsx")

st.set_page_config(
    page_title="Salary Prediction App",
    page_icon="💼",
    layout="wide"
)

st.title("Salary Prediction App")
st.divider()

st.write("With this App, you can get estimations for the salaries of the company employees.")

years = st.number_input("Enter the years in company", value=1, step=1, min_value=0)
jobrate = st.number_input("Enter the JobRate", value=3.5, step=0.5, min_value=0.0)

countries = ['United Arab Emirates', 'Syria', 'Saudi Arabia', 'Lebanon', 'Egypt']  
departments = ['Quality Control', 'Sales', 'Product Development', 'Manufacturing', 'Marketing', 'Account Management', 'IT', 'Quality Assurance']
genders = ['Male', 'Female']

selected_country = st.selectbox("Select the Country", options=countries)
selected_department = st.selectbox("Select the Department", options=departments)
selected_gender = st.selectbox("Select Gender", options=genders)

input_dict = {
    'Years': years,
    'Job Rate': jobrate,
    'Department': selected_department,
    'Country': selected_country,
    'Gender': selected_gender
}

input_df = pd.DataFrame([input_dict])

model = joblib.load("salary_prediction_model.pkl")

predict = st.button("Press the button for salary prediction")
st.divider()

if predict:
    st.balloons()

    prediction = model.predict(input_df)[0]
    st.write(f"Salary Prediction is {prediction:,.2f}")
    
    st.subheader("Average Salary by Department")
    avg_salary_by_dept = data.groupby("Department")["Annual Salary"].mean().sort_values(ascending=False)
    avg_salary_by_dept.plot(kind="bar", color='green')
    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Salary")
    st.pyplot(plt)

else:
    st.write("Press the button to make the prediction")
