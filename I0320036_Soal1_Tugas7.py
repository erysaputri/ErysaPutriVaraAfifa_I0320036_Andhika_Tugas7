# header
a = "feedback webinar"
b = a.upper()
c = b.center(50, '*')
print(c)

# input nama
nama = input("\nSilahkan masukkan nama Anda di bawah ini :\n")
x = ("\nTerimakasih banyak, nama ! Telah mengikuti hingga akhir acara, silahkan isi pertanyaan berikut")
y = x.replace("nama", nama)
print(y)

# feedback
p = input("\nTuliskan review singkat mengenai acara webinar hari ini beserta kritik dan saran dalam paragraf singkat :\n")
q = p.count('.')
print("\nSuper sekali! %d kalimat yang Anda berikan telah kami terima ^^" % q)

# rate
rate = float(input("\nDari skala 1-5 seberapa puaskah Anda dengan keseluruhan webinar :\n"))
if rate <= 3:
    print("Kami memohon maaf atas segala kekurangan yang ada. Semoga saran yang telah Anda berikan dapat membantu kami menjadi lebih baik ke depannya.")
else :
    print("Terimakasih banyak! Nantikan webinar selanjutnya dari kami!")