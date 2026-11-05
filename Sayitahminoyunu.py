import random

def tekrarsor():
 global zorluk
 global gizli_sayi
 soruaralik = input("Sayı Tahmin Aralığı Yazılılabilirmi Yoksa Zorluğu Seçilebilirmi Olsun? (Y/S): ")
 print()
 if soruaralik == "Y" or soruaralik == "y":
    sayiaralik1 = int(input("1.Sayı Aralığınız Kaç Olsun?: "))
    sayiaralik2 = int(input("2.Sayı Aralığınız Kaç Olsun?: "))
    gizli_sayi = random.randint(sayiaralik1,sayiaralik2)
    print()
 elif soruaralik == "S" or soruaralik == "s":
    zorluk = str(input("Sayı Tahmini Zorluğunuzu Seçin (Kolay,Orta,Zor):  "))
    print()
    if zorluk == "kolay" or zorluk == "KOLAY" or zorluk == "K" or zorluk == "k":
       gizli_sayi = random.randint(1, 10)
    elif zorluk == "orta" or zorluk == "ORTA" or zorluk == "O" or zorluk == "o":
      gizli_sayi = random.randint(1, 100)
    elif zorluk == "zor" or zorluk == "ZOR" or zorluk == "Z" or zorluk == "z":
      gizli_sayi = random.randint(1, 1000)
 else:
    print("Tekrar Deneyiniz!")
    print()
    print("-" * 50)
    print()
    tekrarsor()

tekrarsor()

def tahminkar():
 if tahmin < gizli_sayi:
    print("Tahmin Ettiğiniz Sayı Seçilen Sayıdan Daha Küçüktür.\n")
    tahmintek()
 elif tahmin > gizli_sayi:
    print("Tahmin Ettiğiniz Sayı Seçilen Sayıdan Daha Büyüktür.\n")
    tahmintek()
 else:
    print("Sayıyı Doğru Tahmin Ettiniz!\n")
    tekrar = str(input("Birdaha Oynamak İstermisiniz? (E/H):  "))
    print()
    if tekrar == "e" or tekrar == "E":
       print("-" * 50)
       print()
       tekrarsor()
       tahmintek()
    else:
       print("Tekrar Görüşmek Üzere!")
       print()
       print("-" * 50)
       print()
       


def tahmintek():
    global tahmin
    tahmin = int(input("Sayı Tahmininizi Girin:  "))
    print()
    tahminkar()

tahmintek()


   



