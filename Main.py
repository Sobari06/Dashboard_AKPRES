import streamlit as st
import pandas as pd
import plotly_express as px
from streamlit_lottie import st_lottie
import requests
import os
# Mengatur konfigurasi tampilan Streamlit
def set_page_config():
        st.set_page_config(
            page_title="Gantari Prestasi",
            page_icon='Foto Prestasi/LOGO EKSE1.png',
            layout="wide",
            initial_sidebar_state="expanded",
        )

# Memanggil fungsi set_page_config()
set_page_config()


dfa= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(Fakultas)',
    usecols='A:B')
names = dfa['Fakultas'].apply(str)
values = dfa['Count'].apply(int)

fig1= px.bar(
dfa, y= values,  x=names,
title= 'Fakultas')

fig1.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

dfb= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(Jenis Kelamin)',
    usecols='A:B')

names = dfb['JenisKelamin'].apply(str)
values = dfb['Count'].apply(int)

fig2= px.pie(dfb, values= values, 
names= names, 
title= 'Jenis Kelamin')


dfc= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(JenisPrestasi)',
    usecols='A:B')
names = dfc['JenisPrestasi'].apply(str)
values = dfc['Count'].apply(int)

fig3= px.bar(dfc, y= values, x=names,
title= 'Jenis Prestasi')

fig3.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

dfd= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(Bulan)',
    usecols='A:B')
names = dfd['Bulan'].apply(str)
values = dfd['Count'].apply(int)

fig4= px.line(dfd, y= values, 
x= names, 
title= 'Jumlah Prestasi Berdasarkan Bulan')

fig4.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

dfe= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(SkalaLomba)',
    usecols='A:B')
names = dfe['SkalaLomba'].apply(str)
values = dfe['Count'].apply(int)

fig5= px.bar(dfe, x= values, y=names,
title= 'Jumlah Prestasi Berdasarkan Skala Lomba')

fig5.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

dff= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(PelaksanaanLomba)',
    usecols='A:B')
names = dff['PelaksanaanLomba'].apply(str)
values = dff['Count'].apply(int)

fig6= px.pie(dff, values= values, 
names= names, 
title= 'Jenis Perlombaan')

dfg= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(KategoriPrestasi)',
    usecols='A:B')
names = dfg['KategoriPrestasi'].apply(str)
values = dfg['Count'].apply(int)

dfh= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='Table',
    usecols=[1,2,3,4,5,6,7,8,9,10,11,12,13])
dfh = dfh.set_index(pd.Index(range(1, len(dfh) + 1)))



# Mengubah kolom 12 menjadi tipe data datetime
dfh['Waktu Pelaksanaan'] = pd.to_datetime(dfh['Waktu Pelaksanaan'])

# Membuat fungsi untuk mengubah format tanggal
def ubah_format_tanggal(date):
    return date.strftime('%d-%B-%Y')

# Mengaplikasikan fungsi pada kolom 12
dfh['Waktu Pelaksanaan'] = dfh['Waktu Pelaksanaan'].apply(ubah_format_tanggal)




fig7= px.pie(dfg, values= values, 
names= names, 
title= 'Kategori Prestasi')

#Visualisasi Grafik Prestasi Eksekutif Ormawa
#Mendefinisikan fungsi untuk menampilkan animasi Lottie
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Mendefinisikan URL animasi Lottie yang akan ditampilkan
url = "https://assets8.lottiefiles.com/packages/lf20_sy6mqjxk.json"


# Menampilkan animasi Lottie di tampilan utama Streamlit
st_lottie(load_lottie_url(url))

col1, col2= st.columns([2,1])
with col1:
            st.title('Dashboard Prestasi Mahasiswa PKU IPB Angkatan 59')
            st.subheader("Ormawa Eksekutif PKU IPB Kabinet Gantari Arti")   
with col2:
        # Tampilkan informasi nilai mutu
             st.image('Foto Prestasi/RISBANG X AKPRES.png', width=300)

st.markdown('-------------') 
st.write("Dashboard Prestasi Mahasiswa PKU IPB Angkatan 59 ini bertujuan untuk memberikan pemahaman yang lebih baik tentang pencapaian akademik dan non-akademik mahasiswa PKU IPB, serta mengapresiasi prestasi yang telah mereka raih. Dengan adanya dashboard ini, diharapkan dapat memberikan informasi terkait perkembangan prestasi mahasiswa, sehingga dapat memberikan motivasi dan inspirasi dalam mengejar prestasi lebih baik.")
#=============================== Skala Lomba ===========================================
st.markdown('-------------')   
st.subheader('Metriks Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah metriks terkait total prestasi yang diperoleh dan jumlah prestasi berdasarkan skala lomba.')

dfg= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='MX(Jumlah Prestasi)',
    usecols='A:B')
names = dfg['Jumlah Prestasi'].apply(str)
metrik = dfg['count'].apply(int)



col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Jumlah Prestasi", metrik[0])
with col2:
    st.metric("Internasional", metrik[3])
with col3:
    st.metric("Nasional", metrik[1])
with col4:
    st.metric("Regional", metrik[2])
st.markdown('-------------')

#=============================== Bulan ===========================================
st.subheader('Line Chart Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah Line Chart terkait perkembangan jumlah prestasi yang diperoleh tiap bulannya.')
left_column,middle_column, Right_Column = st.columns([1,4,1])
with left_column:
    st.image("Foto Prestasi/Add.png")
middle_column.plotly_chart(fig4,use_container_width=True)
with Right_Column:
     st.image("Foto Prestasi/Add.png")
st.markdown('-------------')


#=============================== Jenis Perlombaan ===========================================
#=============================== Jenis Kelamin ===========================================
st.subheader('Pie Chart Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah tiga pie chart terkait jumlah prestasi mahasiswa berdasarkan jenis perlombaan, kategori prestasi, dan jenis kelamin.')
left_column,middle_column, Right_Column = st.columns([4,4,4])
left_column.plotly_chart(fig6, use_container_width=True)
middle_column.plotly_chart(fig7,use_container_width=True)
Right_Column.plotly_chart(fig2,use_container_width=True)
st.markdown('-------------')

#=============================== Fakultas ===========================================
#=============================== Jenis Prestasi ===========================================
st.subheader('Bar Chart Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

left_column, Right_Column = st.columns([4,4])
left_column.plotly_chart(fig1, use_container_width=True)
Right_Column.plotly_chart(fig3,use_container_width=True)

#=============================== Data Foto ===========================================


# Membuat FIltrasi menggunakan Selectbox


st.markdown('-------------')
st.subheader('Dataframe Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Terdapat sistem filtrasi data yang bisa membantu anda untuk mencari data dengan lebih cepat')

# Menambahkan filter
filter_options = {
    'Fakultas': dfh['Fakultas'].unique(),
    'Jenis Prestasi': dfh['Jenis Prestasi'].unique(),
    'Skala Lomba/Pertandingan': dfh['Skala Lomba/Pertandingan'].unique(),
}

selected_filters = {}

for option, values in filter_options.items():
    selected_filters[option] = st.multiselect(f"Pilih {option}", values)

# Memfilter data berdasarkan filter yang dipilih
filtered_df = dfh.copy()

for option, selected_values in selected_filters.items():
    if selected_values:
        filtered_df = filtered_df[filtered_df[option].isin(selected_values)]


# Menampilkan data yang terfilter
st.write("Data Terfilter:")
st.write(filtered_df)

st.markdown('-------------')
st.subheader('Prestasi Mahasiswa PKU IPB Angkatan 59')

# Menghapus duplikasi data berdasarkan kolom 'Nama Mahasiswa'
filtered_df = filtered_df.drop_duplicates(subset='Nama Lengkap')

# Menghitung jumlah orang yang terfilter
num_filtered_people = filtered_df.shape[0]

# Menghitung jumlah kolom yang diperlukan berdasarkan jumlah orang yang terfilter
num_columns = min(4, num_filtered_people)

# Menghitung jumlah tumpukan kolom yang diperlukan berdasarkan jumlah orang yang terfilter
num_stacks = (num_filtered_people + 3) // 4

for stack in range(num_stacks):
    
    columns = st.columns(4)

    for i in range(4):
        if i + stack * 4 < num_filtered_people:
            row = filtered_df.iloc[i + stack * 4]
            foto_path = f"Foto Prestasi/{row['Fakultas']}/{row['Path foto']}"
            if os.path.exists(foto_path):
                columns[i].image(foto_path, use_column_width=True)
            else:
                columns[i].write(f"Tidak ada foto untuk {row['Nama Lengkap']}")
        else:
            columns[i].image("Foto Prestasi/Add.png", use_column_width=True)