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

#Now I want the user to select the date column and converted it into strings
date = st.selectbox("Select date column:", df.columns)
month = st.selectbox("Select month column:", df.columns)
year = st.selectbox("Select year column", df.columns)

df["full_date"] = pd.to_datetime(
    dict(
        year=df[year],
        month=df[month],
        day=df[date]
    ),
    errors="coerce"
)


# Remove bad columns , missing price and date column
df[price] = pd.to_numeric(df[price], errors="coerce")

clean_df = df.dropna(subset=["full_date", price])


sales_over_time = clean_df.groupby("full_date")[price].sum()

st.subheader("Sales Over Time")

fig, ax = plt.subplots()
sales_over_time.plot(ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Sales")

st.pyplot(fig)





