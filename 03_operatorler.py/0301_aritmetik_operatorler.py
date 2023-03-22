print(2+4)
print(4-5)
print(20/3)  # bölme
print(20//3)  # tam bölme,ondalıklı sonucu bir küçük tam sayıya yuvarlar,sonuç -3.5 ya da üzeri olursa -4e yuvarlar.pozitif olsaydı 3.5 sonucunu 3e yuvarlardı
print(20//3.)  # tam bölmede floatlı ifade varsa sonuç ondalıklı olur
print(20*5)
print(4**2)  # üs alma
print(10 % 3)  # 10 un 3 e bölümünden kalan.Mod alma işlemidir
print(10 % 3.5)  # 10 un 3.5 ten kalanı ondalıklı gösterir
print(-5. + 15)  # sonucu ondalıklı gösterir
# unary,sayıların işareti
print(16**(1/2))#karekök alır
print(16**0.5)
print(-14//5)
#region islem_onceligi
"""
unary yani işaretleri
üst alma(işlem önceliği sağdan sola doğrudur)
çarpma,bölme,mod alma(üç işlem aynı anda varsa işlem önceliği soldan sağa doğrudur,kendi arasında da soldan sağa doğrudur)
toplama,çıkarma

"""
#endregion
print(2**2**3)#sonuç 256dır,2 üssü 3 =8 ve 2 üssü 8=256dır
