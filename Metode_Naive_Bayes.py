from collections import Counter

#
# Muhammad Azmi / 17 Maret 2021
# 
# Python Version : 3.7.4
#

print ("------------------------------------------------")
print ("--------------- METODE NAIVE BAYES -------------")
print ("------------------------------------------------")
print ("--------------- Play Golf ? Yes/No -------------")
print ("------------------------------------------------")

print ("Masukkan Data Uji (Huruf Kapital Harus Sesuai !!)")
outlook_input = input("Masukkan Outlook [Rainy | Overcast |Sunny] : ")
temp_input = input("Masukkan Temp [Hot | Mild |Cool] : ")
humidity_input = input("Masukkan Humidity [High |Normal] : ")
windy_input = input("Masukkan Windy [FALSE | TRUE] : ")


          # ['Outlook','Temp','Humidity','Windy','Play Golf']
dataset =  [['Rainy','Hot','High','FALSE','No'],          # 1
            ['Rainy','Hot','High','TRUE','No'],
            ['Overcast','Hot','High','FALSE','Yes'], 
            ['Sunny','Mild','High','FALSE','Yes'],       #yes
            ['Sunny','Cool','Normal','FALSE','Yes'],      # 5
            ['Sunny','Cool','Normal','TRUE','No'],
            ['Overcast','Cool','Normal','TRUE','Yes'],
            ['Rainy','Mild','High','FALSE','No'],
            ['Rainy','Cool','Normal','FALSE','Yes'],
            ['Sunny','Mild','Normal','FALSE','Yes'],      # 10
            ['Rainy','Mild','Normal','TRUE','Yes'],
            ['Overcast','Mild','High','TRUE','Yes'],    #yes
            ['Overcast','Hot','Normal','FALSE','Yes'],
            ['Sunny','Mild','High','TRUE','No']]          # 14



def cek_kasus_sama_dgn_klas(isi_atribut_apa, dataset, isi_label_apa) :  # "raini | yes" , ada berapa?
    jumlah = 0
    for i in range(len(dataset)):
        apakah_ada = isi_atribut_apa in dataset[i] and isi_label_apa in dataset[i]
        if apakah_ada == True :
            jumlah = jumlah + 1

    return jumlah


# mendapatkan isi kolom dalam dataset # dengan cara merubah bentuk list
def mendapatkan_isi_tiap_kolom(dataset) :
    isi_kolom_ke = []
    for i in range(jumlah_kolom) :
        tampung = []
        for j in range(len(dataset)) :
            tampung.append(dataset[j][i])

        isi_kolom_ke.append(tampung)

    # print(isi_kolom_ke) # print semua isi kolom, yg terdiri dari 5 indek, masing-masing indek punya 14 indeks
    return isi_kolom_ke


# Mencari P(X|Ci) atau jumlah kasus yang sama dengan class yang sama
def mencari_jumlah_kasus_sama(data_uji, dataset, isi_label) :
    hasil_jumlah_kasus_sama = []
    for i in range(len(data_uji)) :
        tampung = []
        for j in range(len(isi_label)):
            tampung.append(cek_kasus_sama_dgn_klas(data_uji[i], dataset, isi_label[j])) 

        hasil_jumlah_kasus_sama.append(tampung)

    # print "DATA KASUS YANG SAMA : ", hasil_jumlah_kasus_sama
    return hasil_jumlah_kasus_sama


# Menghitung P(Ci) atau jumlah class / label 
def mencari_prob_label(label, jumlah_dataset) :
    probabilitas_label = []
    for i in range(len(label)) :
        probabilitas_label.append(label[i]/float(jumlah_dataset))

    # print "PROBABILITAS LABEL :" ,probabilitas_label
    return probabilitas_label


# cek nilai probabilitas atribut ke-n
def menghitung_prob_atribut(hasil_jlh_kasus_sama, label) :
    probabilitas_atribut = []
    for n in range(len(hasil_jlh_kasus_sama)):
        probabilitas_satu = []
        for i in range(len(banyak_label)):
            probabilitas_satu.append(float(hasil_jlh_kasus_sama[n][i])/banyak_label[i])

        probabilitas_atribut.append(probabilitas_satu)

    # print "PROBABILITAS ATRIBUT :", probabilitas_atribut
    return probabilitas_atribut


# ubah bentuk array # baris jadi kolom, kolom jadi baris supaya dapat dikalikan
def ubah_bentuk_prob_atribut(label, probabilitas_atribut) :
    ubah_bentuk_prob_atribut = []
    for i in range(len(label)):
        tampung_prob = []
        for j in range(len(probabilitas_atribut)) :
            tampung_prob.append(probabilitas_atribut[j][i])

        ubah_bentuk_prob_atribut.append(tampung_prob)

    # print "SETELAH DIRUBAH BENTUK ATR PROB :", ubah_bentuk_prob_atribut
    return ubah_bentuk_prob_atribut


# mengalikan tiap probabilitas atribut
def kalikan_prob_atribut(label, probabilitas, probabilitas_atribut) :
    hasil_kali_atribut = []
    for i in range(len(banyak_label)):
        m=1
        for j in range(len(probabilitas)):
            m = m*probabilitas_atribut[i][j]
        hasil_kali_atribut.append(m)    

    # print "HASIL KALI PROBABILITAS ATRIBUT :",hasil_kali_atribut
    return hasil_kali_atribut


# mengalikan probabilitas atribut dengan probabilitas label
def kalikan_prob_label_dan_prob_atribut(label, probabilitas_label, hasil_kali_atribut) :
    hasil_kali_all_prob = []
    for i in range(len(banyak_label)):
        hasil_kali_all_prob.append(hasil_kali_atribut[i]*probabilitas_label[i])

    # print "HASIL KALI SEMUA PROBABILITAS   :", hasil_kali_all_prob
    return hasil_kali_all_prob
        

# hasil probabilitas tertinggi
def mencari_nilai_prob_tertinggi(hasil_kali_all_prob, isi_label) :
    index_tertinggi = hasil_kali_all_prob.index(max(hasil_kali_all_prob))
    print ("HASIL KLASIFIKASI : " , isi_label[index_tertinggi])


########################################################
#--------------- START METODE NAIVE BAYES -------------

# mendapatkan jumlah atribut/kolom
jumlah_kolom = len(dataset[0])

# mendapatkan jumlah dataset
jumlah_dataset = len(dataset)

# mendapatkan isi tiap kolom
isi_kolom_ke = mendapatkan_isi_tiap_kolom(dataset)

# mendapatkan isi label/kelas dengan fungsi Counter # return Dictionary
counter_label = Counter(isi_kolom_ke[len(isi_kolom_ke) - 1]) # get label {'Yes': 9, 'No': 5}
# print "DICT :", counter_label

# mendapatkan isi label/kelas   # return List()
isi_label = list(counter_label)
# print "ISI LABEL    :", isi_label

# mendapatkan banyak label
banyak_label = []
for i in range(len(isi_label)):
    banyak_label.append(counter_label[isi_label[i]])
# print "BANYAK LABEL :", banyak_label

# Memasukkan data inputan user kedalam list data_uji
data_uji = [outlook_input, temp_input, humidity_input, windy_input]
# data_uji = ['Rainy', 'Mild', 'High', 'FALSE']  # data testing, "yes" atau "no" ??

hasil_jumlah_kasus_sama = mencari_jumlah_kasus_sama(data_uji, dataset, isi_label)

probabilitas_label = mencari_prob_label(banyak_label, jumlah_dataset)

probabilitas_atribut = menghitung_prob_atribut(hasil_jumlah_kasus_sama, banyak_label)

hasil_ubah_bentuk_prob_atribut = ubah_bentuk_prob_atribut(banyak_label, probabilitas_atribut)

hasil_kali_atribut = kalikan_prob_atribut(banyak_label, probabilitas_atribut, hasil_ubah_bentuk_prob_atribut)

hasil_kali_all_prob = kalikan_prob_label_dan_prob_atribut(banyak_label, probabilitas_label, hasil_kali_atribut)

mencari_nilai_prob_tertinggi(hasil_kali_all_prob, isi_label) # Hasil Klasifikasi


