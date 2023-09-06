print("Menghitung Volume Balok")
print("=======================")

print("Nama = Mahrus Solihin")
print("NIM = 230441100032")
print()

#coding untuk mengetahui tipe datanya
nama = "Mahrus Solihin"
print(nama, "Tipenya", type(nama))
NIM = 230441100032
print(NIM, "Tipenya", type(NIM))
print()

#coding untuk mengetahui tipe datanya
diketahui = "Diketahui"
print(diketahui, "Tipenya", type(diketahui))
panjang = 24
print(panjang, "Tipenya", type(panjang))
lebar = 18
print(lebar, "Tipenya", type(lebar))
tinggi = 10
print(tinggi, "Tipenya", type(tinggi))
print()

print("Diketahui")
print("Panjang balok = 24 cm")
print("Lebar balok = 18 cm")
print("Tinggi balok = 10 cm")
print()

print("Rumus volume balok adalah v = p*l*t")
print("Maka p*l*t = 24*18*10")
print()

#rumus volume balok
p = 24
l = 18
t = 10
volume = p*l*t
print("Jadi volune balok = ", format(volume),"cm")
print("=============================")
#selesai

#coding ke 2
print("Menghitung Volume Balok")
print("=============================")

Nama = "Mahrus Solihin"
print(Nama, "Tipe", type(Nama))
NIM = 230441100032
print(NIM, "Tipe", type(NIM))
print()

print("Diketahui")
print("Panjang Balok = 24 cm")
print("Lebar Balok = 18 cm")
print("Tinggi Balok = 10 cm")

#rumus
p = 24
l = 18
t = 10
Rumus_volume = p*l*t

def volume(p, l, t):
    hasil = 24 * 18 * 10
    return hasil
print()
print("Volume balok adalah =", volume(p, l, t),"cm")
print("============================")
print()
print()
#coding ke 2 selesai

#coding ke 3
print("Menghitung Volume Balok")
print("========================")
Nama = "Mahrus Solihin"
print(Nama, "Bertipe", type(Nama))
NIM = 230441100032
print(NIM, "Bertipe", type(NIM))
print()

Panjang = int(input("Masukkan Panjang Balok = "))
Lebar = int(input("Masukkan Lebar Balok = "))
Tinggi = int(input("Masukkan Tinggi Balok = "))

def volume(Panjang, Lebar, Tinggi):
    hasil = Panjang * Lebar * Tinggi
    return hasil
print("Volume balok adalah =", volume(Panjang, Lebar, Tinggi))
print("============================")
#coding ke 3 selesai