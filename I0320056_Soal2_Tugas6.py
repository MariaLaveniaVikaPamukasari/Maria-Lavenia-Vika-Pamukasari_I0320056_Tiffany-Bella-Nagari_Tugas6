print(" ")
print("\t\t\tProgram menghitung nilai rata-rata menggunakan perintah perulangan while")
print(" ")
print("\t\t\tSelamat datang di RataRataz, mesin penghitung nilai rata-rata")
print("\t\t======================================================================")
print(" ")
print("NOTE: Klik ENTER jika telah selesai menginputkan nilai")
nilai = []
a = int(input("Silahkan masukkan nilai yang ingin di rata-ratakan : "))
while a != '':
    nilai.append(int(a))
    a = input("Silahkan masukkan nilai Anda selanjutnya:")
avg = sum(nilai) / len(nilai)
print("Nilai rata-rata Anda adalah:", avg)