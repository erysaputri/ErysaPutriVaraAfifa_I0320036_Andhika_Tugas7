import math
# nama kelompok
kel = input("Silahkan masukkan nomor kelompok : ")
jd = "Tinggi Badan Kelompok %s" % kel
h = jd.center(40, '-')
print(h)

# jumlah anggota
jml = int(input("\nJumlah anggota kelompok : "))
data = []

# data tinggi
for a in range(0, jml):
    print("Masukkan tinggi dalam bentuk desimal dan satuan cm")
    tinggi = float(input("Tinggi badan siswa ke-%d : " % (a+1)))
    data.append(tinggi)

# tertinggi dan terendah
print("\nTinggi badan anggota kelompok tertinggi adalah", max(data), "cm")
print("Tinggi badan anggota kelompok terendah adalah", min(data), "cm")

# rata rata tinggi badan anggota kelompok
total = float(sum(data))
mean = float(total/jml)
print("\nRata-rata tinggi badan dalam kelompok adalah %d" % math.ceil(mean), "cm")

import random
# random
print("\nTinggi badan anggota kelompok yang harus presentasi adalah", random.choice(data), "cm")
