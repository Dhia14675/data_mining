# Sleep Disorder Prediction 

**DHIA TAWAKALNA**

**NIM**: A11.2022.14675
        
 **Mata Kuliah** : DATA MINING

STREAMLIT : [Prediksi Sleep Disorder] (https://prediksi-sleep-disorder.streamlit.app)

DESKRIPSI PROYEK : 
Proyek ini bertujuan untuk membuat prediksi sleep disorder berdasarkan lifestyle menggunakan algoritma XGBoost. Proyek ini mencakup tahapan analisis EDA,visualisasi data, prepoccesing, training model, dan deployment menggunakan **STREAMLIT** 

---

## **Tujuan Proyek**
Proyek ini bertujuan untuk melakukan prediksi kelainan tidur menggunakan dataset Sleep dan gaya hidup. Dataset telah melalui beberapa tahap :
1. Eksplorasi dan Visualisasi data.
2. Prepocessing untuk membersihkan data.
3. Training menggunakan algoritma XGBoost.
4. Melakukan Hyper-parameter Tuning - XGBoost
5. Evaluasi Model
6. Deployment menggunakan Streamlit untuk kemudahan akses.

---

## **Struktur File**
Berikut adalah struktur file dalam repository dan penjelasannya :
1. **'Dataset: Sleep_health_and_lifestyle_dataset.csv'**
   Dataset utama yang digunakan untuk melatih model prediksi. Dataset ini berisi informasi gaya hidup dan pola tidur individu.
2. **'dataset_baru.csv'**
   Dataset tambahan yang sudah di preprocessing untuk uji coba sebagai validasi model.
3. **'Prediksi_studentsleep.ipynb'**
   Notebook utama untuk training model, evaluasi performa, dan anlisis hasil.
4. **'app.py'**
   File Phyton yang digunakan untuk membuat aplikasi web dengan **Streamlit**.
5. **'XGB_model.pkl'**
   Model yang telah dilatih menggunakan algoritma XGBoost dan disimpan dalam format '.pkl'.
6. **'requirements.txt'**
   File yang berisi daftar library python yang dibutuhkan oleh proyek ini, seperti :
   - pandas
   - numpy
   - streamlit
   - XGBoost
   - Joblib
7. **'test.py'**
   File Python yang digunakan untuk menguji performa model dengan inputan baru sebagai dataset validasi.

---

## **CARA MENJALANKAN PROYEK**
Berikut adalah langkah-langkah untuk menjalankan proyek :
1. Clone repository :
        '''bash
           git clone https://github.com/username/repository-name.git
2. INSTALL DEPENDENCIES :
        pip install -r requirements.txt
3. Jalankan Aplikasi Streamlit :
        streamlit run app.py
4. Akses aplikasi di browser melalui URL :
        http://localhost:8501

   ---

# PENJELASAN DATASET
Dataset: Sleep_health_and_lifestyle_dataset.csv :
- Fitur :
- Gender, Berisi jenis kelamin ( Male dan Female )
- Age , Berisi usia pengguna
- Occupation , Berisi profesi seperti ( Nurse,Doctor,Engineer,Software Engineer, dll)
- Sleep Duration , Berisi lama waktu tidur seseorang dari 1 - 10
- Quality of Sleep , Berisi kualitas tidur seseorang dari 1 - 10
- Physical Activity Level , Berisi banyaknya aktifitas fisik yang dikerjakan skala 0 - 100
- Stress Level , Berisi level stress seseorang skala 1 - 10
- BMI Category , Berisi berat badan seseorang ( Normal,Overweight,Underweight,dan Obese )
- Heart Rate , berisi rate detak jantung manusia
- Daily Steps , berisi jumlah langkah kaki seseorang setiap hari
- Blood Pressure , Berisi tekanan darah manusia SYSTOLIC dan DIASTOLIC
  Target :
- Sleep Disorder , Berisi hasil prediksi berupa ( No Disorder, Sleep Apnea, Insomnia )
Dataset diproses untuk memastikan kebersihan data sebelum digunakan dalam moodel.

---

# MODEL DAN EVALUASI 
- Model : XGBoost dipilih karena kemampuannya yang unggul dalam menangani data kategori dan performanya yang konsisten baik untuk dataset berukuran kecil maupun besar.
- Hyper-Parameter-Tuning : Proses hyperparameter tuning dilakukan untuk memastikan model dapat memberikan performa terbaiknya pada dataset.
- Evaluasi : Model dilatih dan diuji menggunakan metrik seperti akurasi, precision, recall,dan F1-score.
- Hasil akhir : Model mencapai akurasi sebesar 91% pada data validasi.

![image](https://github.com/user-attachments/assets/43e50ed6-9432-4d01-8ebc-9bb2c9a47de7)

![image](https://github.com/user-attachments/assets/0fc5518e-5539-4781-a606-9747722dba7a)



