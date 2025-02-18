# 📊 E-Commerce Payment Analysis

## 📝 **Deskripsi Proyek**

Proyek ini bertujuan untuk menganalisis pola pembayaran pelanggan pada platform e-commerce menggunakan dataset **order_payments_dataset.csv**. Analisis ini mencakup distribusi metode pembayaran, rata-rata nilai pembayaran per metode, serta distribusi jumlah cicilan dalam pembayaran.

## 📂 **Struktur Direktori**
```
analisis_data/
│── dashboard/                  # Folder untuk aplikasi dashboard
│   ├── cleaned_dataset.csv     # Dataset yang sudah dibersihkan
│   ├── dashboard.py            # File utama Streamlit
│── data/                       # Folder untuk dataset asli
│   ├── order_payments_dataset.csv
│── notebook.ipynb              # Jupyter Notebook untuk analisis eksploratif
│── README.md                   # Dokumentasi proyek ini
│── requirements.txt             # Dependensi Python
```

## 🔬 **Pertanyaan Bisnis**
1. **Metode pembayaran mana yang paling sering digunakan oleh pelanggan?**
2. **Berapa rata-rata nilai pembayaran berdasarkan metode pembayaran?**
3. **Berapa jumlah total pembayaran yang dilakukan dengan cicilan dan bagaimana distribusinya?**

## 🔍 **Insight dari Analisis**

### **1️⃣ Insight dari Gathering Data**
- Dataset terdiri dari **4 kolom utama**: `order_id`, `payment_type`, `payment_installments`, dan `payment_value`.
- Tidak ada nilai **missing** atau duplikat, sehingga data siap digunakan.

### **2️⃣ Insight dari Assessing Data**
- Metode pembayaran paling umum digunakan adalah **credit card**, diikuti oleh **boleto** dan **voucher**.
- Nilai pembayaran bervariasi, dengan beberapa transaksi menggunakan cicilan lebih dari **10 kali**.

### **3️⃣ Insight dari Cleaning Data**
- Semua data telah dikonversi ke tipe data yang sesuai (`int` untuk cicilan dan `float` untuk nilai pembayaran).
- Outlier telah diperiksa menggunakan **boxplot**, tetapi tidak ada anomali signifikan.

### **4️⃣ Insight dari Visualization & Explanatory Analysis**
- **Metode pembayaran paling populer:** **Credit Card**.
- **Rata-rata nilai pembayaran:** Metode **boleto** memiliki nilai pembayaran yang lebih tinggi dibandingkan metode lain.
- **Distribusi cicilan:** Kebanyakan pelanggan membayar dalam **1-6 kali cicilan**, sementara yang menggunakan **10 kali cicilan** adalah minoritas.

## 🚀 **Cara Menjalankan Aplikasi Dashboard**

1. **Pastikan sudah menginstal dependensi**
   ```bash
   pip install -r requirements.txt
   ```

2. **Jalankan aplikasi Streamlit**
   ```bash
   streamlit run dashboard/dashboard.py
   ```

3. **Akses dashboard di browser**
   - **Local URL:** `http://localhost:8501`
   - **Network URL:** `http://192.168.1.X:8501`
   - **Deploy URL:** `https://analystpay.streamlit.app`

## ⚙️ **Algoritma & Metode yang Digunakan**

### **1️⃣ Data Cleaning**
- Menghapus **missing values** dan **duplikasi**.
- Konversi tipe data ke bentuk yang sesuai (`int` untuk cicilan, `float` untuk nilai pembayaran).
- Deteksi **outlier** menggunakan **boxplot**.

### **2️⃣ Exploratory Data Analysis (EDA)**
- Menampilkan **statistik deskriptif** (`describe()` dari Pandas).
- Menganalisis distribusi data dengan **countplot dan bar chart**.
- Menggunakan **heatmap** untuk melihat korelasi antar variabel numerik.

### **3️⃣ Data Visualization**
- **Metode pembayaran paling sering digunakan** → **Bar chart**.
- **Rata-rata nilai pembayaran per metode** → **Bar chart**.
- **Distribusi cicilan dalam pembayaran** → **Histogram / Bar chart**.

## 🎯 **Kesimpulan**
- **Mayoritas pelanggan menggunakan metode pembayaran `credit_card`**.
- **Boleto memiliki nilai pembayaran rata-rata lebih tinggi dibandingkan metode lain**.
- **Sebagian besar transaksi dilakukan dengan cicilan 1-6 kali, sedangkan cicilan 10 kali jarang digunakan**.

## 📌 **Saran untuk Bisnis**
- Mengoptimalkan **promosi pembayaran cicilan** bagi pelanggan yang ingin menggunakan metode selain kartu kredit.
- Menawarkan **insentif untuk metode pembayaran tertentu** untuk meningkatkan adopsi metode pembayaran yang lebih menguntungkan.

📌 **Silakan jalankan Streamlit untuk melihat analisis secara interaktif!** 🚀

