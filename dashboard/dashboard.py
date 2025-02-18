import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Proyek Analisis Data: Order Payment Dataset
# Nama:Kurnia Raihan Ardian
# Email: raihanardila22@gmail.com
# ID Dicoding: raihanardila

# ========== Pastikan path dataset selalu benar ==========
# Dapatkan lokasi absolut dari script yang sedang berjalan
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Buat path relatif agar selalu membaca dataset di folder dashboard/
DATA_PATH = os.path.join(BASE_DIR, "cleaned_dataset.csv")

# Load Dataset dengan path yang sudah diperbaiki
df = pd.read_csv(DATA_PATH)


# Judul Dashboard
st.title("📊 Dashboard E-Commerce Payment Analysis")

# Statistik Dasar
st.subheader("Statistik Dasar")
st.write(df.describe())

# Visualisasi 1: Metode Pembayaran
st.subheader("Distribusi Metode Pembayaran")
payment_counts = df["payment_type"].value_counts()

fig, ax = plt.subplots()
payment_counts.plot(kind="bar", color="orange", ax=ax)
ax.set_title("Metode Pembayaran Terbanyak")
ax.set_xlabel("Metode Pembayaran")
ax.set_ylabel("Jumlah Transaksi")
st.pyplot(fig)

# Visualisasi 2: Rata-rata Pembayaran per Metode
st.subheader("Rata-rata Nilai Pembayaran per Metode")
avg_payment = df.groupby("payment_type")["payment_value"].mean()

fig, ax = plt.subplots()
avg_payment.plot(kind="bar", color="skyblue", ax=ax)
ax.set_title("Rata-rata Pembayaran per Metode")
ax.set_xlabel("Metode Pembayaran")
ax.set_ylabel("Rata-rata Nilai Pembayaran")
st.pyplot(fig)

# Visualisasi 3: Cicilan
st.subheader("Distribusi Cicilan dalam Pembayaran")
installment_counts = df["payment_installments"].value_counts().sort_index()

fig, ax = plt.subplots()
installment_counts.plot(kind="bar", color="lightcoral", ax=ax)
ax.set_title("Jumlah Cicilan dalam Pembayaran")
ax.set_xlabel("Jumlah Cicilan")
ax.set_ylabel("Jumlah Transaksi")
st.pyplot(fig)

st.write("© 2025 - Data Analysis Project")