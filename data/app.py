import pandas as pd
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="Business KPI Dashboard", page_icon="📊", layout="wide"
)

st.title("📊 Business Intelligence & KPI Dashboard")
st.markdown(
    "This interactive dashboard showcases real-time metrics, revenue trends,"
    " and product performance."
)

# قراءة البيانات
df = pd.read_csv("data/business_kpis.csv")

# عرض البيانات في جدول تفاعلي
st.subheader("📋 Transaction Records")
st.dataframe(df)

# حساب مؤشرات الأداء الرئيسية (KPIs)
total_revenue = df["Order_Value"].sum()
average_order = df["Order_Value"].mean()
total_transactions = len(df)

# عرض المؤشرات في أعمدة متجاورة
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Average Order Value (AOV)", f"${average_order:,.2f}")
col3.metric("Total Transactions", total_transactions)

# رسم بياني لمبيعات المنتجات
st.subheader("📈 Revenue by Product Category")
category_revenue = df.groupby("Product_Category")["Order_Value"].sum()
st.bar_chart(category_revenue)
