import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np


# Proyek Analisis Data: Order Payment Dataset
# Nama:Kurnia Raihan Ardian
# Email: raihanardila22@gmail.com
# ID Dicoding: raihanardila

# Pastikan path dataset selalu benar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "cleaned_dataset.csv")

# Load Dataset
df = pd.read_csv(DATA_PATH)

# Pastikan order_date ada, jika tidak, buat simulasi tanggal
if "order_date" not in df.columns:
    np.random.seed(42)  # Untuk konsistensi
    df["order_date"] = pd.to_datetime("2023-01-01") + pd.to_timedelta(np.random.randint(0, 365, size=len(df)), unit="D")

# Konversi order_date ke format string agar Streamlit tidak error
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce").dt.strftime('%Y-%m-%d')

# Dashboard Title
st.title("📊 Dashboard E-Commerce Payment Analysis")

# Tambahkan Sidebar untuk Fitur Interaktif
st.sidebar.header("🛠️ Filter Data")

# Fitur 1: Filter berdasarkan metode pembayaran
payment_options = df["payment_type"].unique().tolist()
selected_payment = st.sidebar.multiselect("🔍 Pilih Metode Pembayaran:", payment_options, default=payment_options)

# Fitur 2: Slider untuk memilih rentang pembayaran
min_payment, max_payment = df["payment_value"].min(), df["payment_value"].max()
selected_range = st.sidebar.slider("💰 Pilih Rentang Pembayaran", min_value=min_payment, max_value=max_payment, value=(min_payment, max_payment))

# Fitur 3: Filter berdasarkan rentang tanggal transaksi dengan layout lebih optimal
df["order_date"] = pd.to_datetime(df["order_date"])  # Konversi kembali ke datetime untuk filtering
min_date, max_date = df["order_date"].min(), df["order_date"].max()

# Menggunakan column layout untuk memastikan sidebar tidak tertutup pada tampilan kecil
col1, col2 = st.sidebar.columns(2)

with col1:
    st.write("📅 Dari:")
    start_date = st.date_input("", min_date, min_value=min_date, max_value=max_date, key="start_date")

with col2:
    st.write("📅 Hingga:")
    end_date = st.date_input("", max_date, min_value=min_date, max_value=max_date, key="end_date")

# Pastikan format tanggal benar & tidak error
if start_date > end_date:
    st.sidebar.error("⚠️ Tanggal mulai tidak boleh lebih besar dari tanggal akhir!")

# Terapkan Filter, Jika Tidak Ada yang Dipilih, Tampilkan Data Awal
df_filtered = df  # Default ke dataset awal
if selected_payment:
    df_filtered = df_filtered[df_filtered["payment_type"].isin(selected_payment)]

df_filtered = df_filtered[
    (df_filtered["payment_value"].between(selected_range[0], selected_range[1])) &
    (df_filtered["order_date"].between(pd.to_datetime(start_date), pd.to_datetime(end_date)))
]

# Jika tidak ada data yang cocok dengan filter, tampilkan data awal
if df_filtered.empty:
    st.warning("⚠️ Tidak ada data yang sesuai dengan filter yang dipilih. Menampilkan semua data.")
    df_filtered = df  # Kembali ke dataset awal jika kosong

# Statistik Dasar
st.subheader("📊 Statistik Dasar dari Data Terfilter")
st.write(df_filtered.describe())

# Visualisasi 1: Metode Pembayaran
st.subheader("📌 Distribusi Metode Pembayaran")
fig, ax = plt.subplots()
df_filtered["payment_type"].value_counts().plot(kind="bar", color="orange", ax=ax)
ax.set_title("Metode Pembayaran Terbanyak")
ax.set_xlabel("Metode Pembayaran")
ax.set_ylabel("Jumlah Transaksi")
st.pyplot(fig)

# Visualisasi 2: Rata-rata Pembayaran per Metode
st.subheader("💰 Rata-rata Nilai Pembayaran per Metode")
fig, ax = plt.subplots()
df_filtered.groupby("payment_type")["payment_value"].mean().plot(kind="bar", color="skyblue", ax=ax)
ax.set_title("Rata-rata Pembayaran per Metode")
ax.set_xlabel("Metode Pembayaran")
ax.set_ylabel("Rata-rata Nilai Pembayaran")
st.pyplot(fig)

# Visualisasi 3: Cicilan
st.subheader("💳 Distribusi Cicilan dalam Pembayaran")
fig, ax = plt.subplots()
df_filtered["payment_installments"].value_counts().sort_index().plot(kind="bar", color="lightcoral", ax=ax)
ax.set_title("Jumlah Cicilan dalam Pembayaran")
ax.set_xlabel("Jumlah Cicilan")
ax.set_ylabel("Jumlah Transaksi")
st.pyplot(fig)

st.write("© 2025 - Data Analysis Project")
