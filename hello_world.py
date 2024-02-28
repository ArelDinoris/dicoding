import streamlit as st 
import matplotlib.pyplot as plt

st.title('Data Penyewa Sepeda bulan Januari - Maret')

mounth = ('Januari', 'Febuari', 'Maret')
register = (45076704, 11626410, 212162757)

# Chart
st.write("""
# Penyewa sepeda terbanyak bulan Januari - Maret
Bulan Maret adalah bulan terbanyak sepeda yang disewa
""")

plt.bar(x=mounth, height=register)
st.pyplot()

mounth = ('Januari', 'Febuari', 'Maret')
workingday = [20, 19, 70]

# Chart
st.write("""
# Penyewa sepeda terbanyak bulan Januari - Maret di hari kerja
Hari kerja di bulan Maret adalah  terbanyak sepeda yang disewa
""")

plt.bar(x=mounth, height=workingday)
st.pyplot()