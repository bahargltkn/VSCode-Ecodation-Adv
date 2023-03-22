print("hayatta","en","hakiki")#virgüllü ifadeler argümandır.Bu kodun 3 tane argüman var.Parametre de diyebiliriz. 
print("mürşit","ilimdir")
print("---------------")
print("hayatta","en","hakiki", end="\n")#End kullanmasak da aynı şekilde kod bitince diğer kodu alt satıra alır.
print("mürşit","ilimdir",end="...")#end in yanına 3 nokta koyarsak,herhangi bir şey yazarsak ya da parantezin içini boş bırakırsak alt satıra geçmez devam eder.
print("alfabe")
print("hayatta","en","hakiki", sep="-")#argümanların arasına parantez içindeki ifadeyi koyar, \n koyarsak hepsini alt satıra alır.
print("mürşit","ilimdir",end=">>",sep="-")#end ve sep sıraları fark etmez.sep komutu argümanlar arasına tire koyacak ve end komutu alt satırla üst satırı bir satırda yazdırıp kelimeler arasına iki büyüktür işareti koyacak
print("haya","hak",sep="*",end="\n")
print(21)#sayıları tırnaksız da yazabiliriz ama kelimeleri yazamayız
