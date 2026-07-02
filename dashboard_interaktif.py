import streamlit as st

st.title("📍 Cerita Interaktif")
st.image("anak.jpeg", caption="Foto Anak", use_column_width=True)

st.write("Anak sekecil itu berkelahi dengan waktu, demi satu impian yang kelak ganggu tidurmu.")

st.subheader("Pertanyaan:")
st.write("Apakah yang membuat takut anak itu?")

jawaban = st.radio("Pilih salah satu:", ("wowo", "wewe"))

if jawaban == "wowo":
    st.markdown("[👉 Lihat Berita Aliansi Ormas Madiun Raya](https://www.jpnn.com/news/aliansi-ormas-madiun-raya-dan-garda-prabowo-keluarkan-6-poin-sikap)")
elif jawaban == "wewe":
    st.markdown("[👉 Lihat Review Putu Jumbo](https://www.google.com/search?q=putu+jumbo+jalan+bali+madiun&oq=putu+jumbo+jalan+bali+madiun&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCggCEAAYgAQYogQyCggDEAAYgAQYogQyCggEEAAYgAQYogQyBwgFEAAY7wUyBwgGEAAY7wXSAQg1NjAwajBqOagCBrACAfEFeNzlOrKc0jQ&sourceid=chrome&ie=UTF-8)")
