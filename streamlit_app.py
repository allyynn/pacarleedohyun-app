import streamlit as st

st.title("🩰 pacar sunjae")
st.write(
 "mau punya pacar kaya sunjae"
)
st.image("IMG_20250414_210659_653.webp")

st.title("math")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
   st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
