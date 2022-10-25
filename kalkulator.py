#membuat fungsi untuk masing-masing operator

#membuat fungsi tambah
def tambah(a,b):
    return a + b

#membuat fungsi kurang
def kurang(a,b):
    return a - b

#membuat fungsi perkalian
def kali(a,b):
    return a * b

#membuat fungsi pembagian
def bagi(a,b):
    return a / b 


#membuat menu operasi
print("pilih operasi")
print("1. penjumlahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")

#meminta user menginput pilihan
choice = input("masukan pilihan (1): ")
choice = input("masukan pilihan (2): ")
choice = input("masukan pilihan (3): ")
choice = input("masukan pilihan (4): ")

bil1 = int(input("masukan bilangan pertama: "))
bil2 = int(input("masukan bilangan kedua: "))

if choice == "1":
    print(bil1, "+", bil2, "=", tambah(bil1, bil2))

if choice == "2":
    print(bil1, "-", bil2, "=", kurang(bil1, bil2))

if choice == "3":
    print(bil1, "*", bil2, "=", kali(bil1, bil2))

if choice == "4":
    print(bil1, "/", bil2, "=", bagi(bil1, bil2))
