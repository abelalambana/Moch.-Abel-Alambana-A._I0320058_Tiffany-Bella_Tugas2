#Kelahiran
tgllahir=int(input("Tanggal lahir :"))
blnlahir=int(input("Bulan lahir (dalam bentuk angka) : "))
thnlahir=int(input("Tahun lahir : "))
lahir=tgllahir+(blnlahir*30)+(thnlahir*365)

#sekarang
tglnow=int(input("Sekarang tanggal berapa : "))
blnnow=int(input("Sekarang bulan apa (dalam bentuk angka) : "))
thnnow = int(input("Sekarang tahun berapa : "))
skrng=tglnow+(blnnow*30)+(thnnow*365)

#masok_rumus
tahun = int(round(skrng-lahir)/365)
bulan= int(round((skrng-lahir) % 365)/30)
hari= str(round((skrng-lahir)%365)%30)

print("Umurmu {} tahun, {} bulan, {} hari.".format(tahun, bulan, hari))