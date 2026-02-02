import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# from utils import generate_ai_insight

#Telling streamlit what to display first on my web app

st.title("AI Sales Insights Assistant")
st.write("Upload your sales CSV file to get started")

#creating a button for file upload in the UI

uploaded_file = st.file_uploader("Upload your sales CSV" , type=["csv"])


# Read csv into pandas, read only when file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

# Telling streamlit to display data first for user to confirm the file upload
st.subheader("Preview of Your Data")
st.dataframe(df.head())

# So I wanted to show available columns first instead of assuming column names
st.write("Columns in dataset: ")
st.write(list(df.columns))

price = st.selectbox(
    "Select the column that represents the price:",
    df.columns
    )

#calculating total sales and the average order value.
total_sales = df[price].sum()
average_order_value = df[price].mean()

# I then saw figured that columns data type might be string so I decided to format it .

st.write(f"Total sales: ${total_sales:,.2f}")
st.write(f"Average Order Value: ${average_order_value:,.2f}")

#Now I want the user to select the 




