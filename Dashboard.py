import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Bike Sharing Dashboard 🚲')

day_df = pd.read_csv('day.csv')
day_df['weather_label'] = day_df['weathersit'].map({1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'})

st.sidebar.header("Filter")
selected_season = st.sidebar.multiselect("Pilih Musim", options=day_df['season'].unique(), default=day_df['season'].unique())

col1, col2 = st.columns(2)

with col1:
    total_rentals = day_df['cnt'].sum()
    st.metric("Total Penyewaan", f"{total_rentals:,}")

with col2:
    avg_temp = day_df['temp'].mean()
    st.metric("Rata-rata Suhu (Norm)", f"{avg_temp:.2f}")

st.subheader("Pengaruh Cuaca terhadap Penyewaan")
fig, ax = plt.subplots()
sns.barplot(x='weather_label', y='cnt', data=day_df, ax=ax)
st.pyplot(fig)

st.write("### Insight Utama")
st.write("- Penyewaan mencapai puncak pada cuaca cerah.")
st.write("- Suhu berpengaruh signifikan terhadap minat pengguna.")
