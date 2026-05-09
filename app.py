'''import streamlit as st
import pandas as pd
from collections import Counter

# Load and clean data
df = pd.read_excel("Boys quiz.xlsx", engine="openpyxl")
df.columns = df.columns.str.strip()
df["Events"] = df["Events (Max 3 per person) :*"].str.split(";")

# Dashboard
st.title("Student Event Participation Dashboard")
st.metric("Total Students", len(df))

st.subheader("Students per Department")
st.bar_chart(df["Department"].value_counts())

event_counts = Counter([event.strip().title() for sublist in df["Events"].dropna() for event in sublist])
st.subheader("Event Participation")
st.bar_chart(pd.Series(event_counts))'''
import pandas as pd
import streamlit as st
import plotly.express as px

# Load your Excel file
data = pd.read_excel("sales_data.xlsx")

# Convert Excel date numbers to proper datetime
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')


# Dashboard Title
st.title("📊 Sales & Revenue Analysis Dashboard")

# KPIs
st.metric("Total Units Sold", int(data['Units Sold'].sum()))
st.metric("Total Revenue", f"₹{data['Revenue'].sum():,.2f}")

# Filters
product_filter = st.selectbox("Select Product", options=["All"] + list(data['Product'].unique()))
category_filter = st.selectbox("Select Category", options=["All"] + list(data['Category'].unique()))

filtered_data = data.copy()
if product_filter != "All":
    filtered_data = filtered_data[filtered_data['Product'] == product_filter]
if category_filter != "All":
    filtered_data = filtered_data[filtered_data['Category'] == category_filter]

# Revenue Trend
fig = px.line(filtered_data, x="Date", y="Revenue", title="Revenue Trend Over Time")
st.plotly_chart(fig)

# Top Products
top_products = filtered_data.groupby("Product")["Revenue"].sum().nlargest(5)
fig2 = px.bar(top_products, x=top_products.index, y=top_products.values, title="Top 5 Products by Revenue")
st.plotly_chart(fig2)

# Category Share
fig3 = px.pie(filtered_data, names="Category", values="Revenue", title="Revenue Share by Category")
st.plotly_chart(fig3)

