import streamlit as st
import joblib

# Muat model dan encoder
model, encoded = joblib.load('model_with_encoder.pkl')

# Judul aplikasi
st.title('Prediksi Profile Berdasarkan Aktivitas Belajar Pengguna')

# Input fitur dari pengguna
HOURS_DATASCIENCE = st.number_input('Masukkan Jam Belajar Data Science:')
HOURS_BACKEND = st.number_input('Masukkan Jam Belajar Beckend:')
HOURS_FRONTEND = st.number_input('Masukkan Jam Belajar Frontend:')
NUM_COURSES_BEGINNER_DATASCIENCE = st.number_input('Masukkan Jumlah Course Beginner Data Science: ')
NUM_COURSES_BEGINNER_BACKEND = st.number_input('Masukkan Jumlah Course Beginner Backend: ')
NUM_COURSES_BEGINNER_FRONTEND = st.number_input('Masukkan Jumlah Course Beginner Frontend: ')
NUM_COURSES_ADVANCED_DATASCIENCE = st.number_input('Masukkan Jumlah Course Advanced Data Science: ')
NUM_COURSES_ADVANCED_BACKEND = st.number_input('Masukkan Jumlah Course Advanced Backend: ')
NUM_COURSES_ADVANCED_FRONTEND = st.number_input('Masukkan Jumlah Course Advanced Frontend:')
AVG_SCORE_DATASCIENCE = st.number_input('Rata-Rata Nilai Data Science: ')
AVG_SCORE_BACKEND = st.number_input('Rata-Rata Nilai Backend: ')
AVG_SCORE_FRONTEND = st.number_input('Rata-Rata Nilai Frontend: ')


# Tambahkan input lainnya sesuai dengan fitur model Anda

# Tombol prediksi
if st.button('Prediksi'):
    # Lakukan prediksi
    prediction_encoded = model.predict([[HOURS_DATASCIENCE, HOURS_BACKEND,HOURS_FRONTEND, NUM_COURSES_BEGINNER_DATASCIENCE, 
                                         NUM_COURSES_BEGINNER_BACKEND,NUM_COURSES_BEGINNER_FRONTEND, NUM_COURSES_ADVANCED_DATASCIENCE, 
                                         NUM_COURSES_ADVANCED_BACKEND, NUM_COURSES_ADVANCED_FRONTEND, AVG_SCORE_DATASCIENCE, 
                                         AVG_SCORE_BACKEND, AVG_SCORE_FRONTEND,]])  # Sesuaikan dengan jumlah fitur
    # predicted_labels = encoded.inverse_transform(prediction_encoded)
    # st.write(f'Prediksi: {prediction_encoded[0]}')
    if prediction_encoded == 0:
        st.write('Advanced Backend')
    elif prediction_encoded == 1:
        st.write('Advanced Data Science')
    elif prediction_encoded == 2:
        st.write('Advanced Frontend')
    elif prediction_encoded == 3:
        st.write('Beginner Backend')
    elif prediction_encoded == 4:
        st.write('Beginner Data Science')
    elif prediction_encoded == 5:
        st.write('Beginner Front End')

