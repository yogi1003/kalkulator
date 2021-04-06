from time import sleep as slip

def penjumlahan():
	try:
		print('==PENJUMLAHAN==')
		angka1 = int(input('masukkan angka pertama: '))
		angka2 = int(input('masukkan angka kedua: '))
		hasil = angka1+angka2
		print(angka1, '+', angka2, '=', hasil)
	except ValueError:
		print('INPUT HARUS ANGKA!!')
		penjumlahan()

	pilihan = input('ingin mengulang? y/n ')
	if pilihan == 'y':
		penjumlahan()
	elif pilihan == 'n':
		menu()
	else:
		print('input salah')

def pengurangan():
	try:
		print('==PENGURANGAN===')
		angka1 = int(input('masukkan angka pertama: '))
		angka2 = int(input('masukkan angka kedua: '))
		hasil = angka1-angka2
		print(angka1, '-', angka2, '=', hasil)
	except ValueError:
		print('INPUT HARUS ANGKA!!')
		pengurangan()

	pilihan = input('ingin mengulang? y/n ')
	if pilihan == 'y':
		pengurangan()
	elif pilihan == 'n':
		menu()
	else:
		print('input salah')

def perkalian():
	try:
		print('==PERKALIAN==')
		angka1 = int(input('masukkan angka pertama: '))
		angka2 = int(input('masukkan angka kedua: '))
		hasil = angka1*angka2
		print(angka1, '*', angka2, '=', hasil)
	except ValueError:
		print('INPUT HARUS ANGKA!!')
		perkalian()

	pilihan = input('ingin mengulang? y/n ')
	if pilihan == 'y':
		perkalian()
	elif pilihan == 'n':
		menu()
	else:
		print('input salah')

def pembagian():
	try:
		print('==PEMBAGIAN==')
		angka1 = int(input('masukkan angka pertama: '))
		angka2 = int(input('masukkan angka kedua:'))
		hasil = angka1/angka2
		print(angka1, '/', angka2, '=', hasil)
	except ValueError:
		print('INPUT HARUS ANGKA!!')
		pembagian()

	pilihan = input('ingin mengulang? y/n ')
	if pilihan == 'y':
		pembagian()
	elif pilihan == 'n':
		menu()
	else:
		print('input salah')

def modulus():
	try:
		print('==MODULUS (hasil bagi)==')
		angka1 = int(input('masukkan angka pertama: '))
		angka2 = int(input('masukkan angka kedua: '))
		hasil = angka1%angka2
		print(angka1, '%', angka2, '=', hasil)
	except ValueError:
		print('INPUT HARUS ANGKA!!')
		modulus()

	pilihan = input('ingin mengulang? y/n ')
	if pilihan == 'y':
		modulus()
	elif pilihan == 'n':
		menu()
	else:
		print('input salah')

def pemangkatan():
	try:
		print('==PERPANGKATAN==')
		angka1 = int(input('masukkan angka pertama: '))
		angka2 = int(input('masukkan angka kedua: '))
		hasil = angka1**angka2
		print(angka1, '**', angka2, '=', hasil)
	except ValueError:
		print('INPUT HARUS ANGKA!!')
		pemangkatan()

	pilihan = input('ingin mengulang? y/n ')
	if pilihan == 'y':
		pemangkatan()
	elif pilihan == 'n':
		menu()
	else:
		print('input salah')

def menu():
	print("""
		SELAMAT DATANG DI PROGRAM SEDERHANA SAYA
		SILAHKAN PILIH FITUR YANG ANDA INGINKAN
		1. PENJUMLAHAN
		2. PENGURANGAN
		3. PERKALIAN
		4. PEMBAGIAN
		5. MODULUS(hasil bagi)
		6. PERPANGKATAN

		0. KELUAR""")
	pilih_menu = input('INPUT: ')
	if pilih_menu == '1':
		penjumlahan()
	elif pilih_menu == '2':
		pengurangan()
	elif pilih_menu == '3':
		perkalian()
	elif pilih_menu == '4':
		pembagian()
	elif pilih_menu == '5':
		modulus()
	elif pilih_menu == '6':
		pemangkatan()
	elif pilih_menu == '0':
		exit()
	else:
		print('input salah')
		slip(1)
		menu()

menu()
