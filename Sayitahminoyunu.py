import random
def tekrarsor():
 global zorluk
 global gizli_sayi
 zorluk = str(input("Sayı Tahmini Zorluğunuzu Seçin (Kolay,Orta,Zor):  "))
 print()
 if zorluk == "kolay" or zorluk == "KOLAY":
     gizli_sayi = random.randint(1, 10)
 elif zorluk == "orta" or zorluk == "ORTA":
     gizli_sayi = random.randint(1, 100)
 elif zorluk == "zor" or zorluk == "ZOR":
     gizli_sayi = random.randint(1, 1000)

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
       print("-" * 15)
       print()
       tekrarsor()
       tahmintek()
    else:
       print("Tekrar Görüşmek Üzere!")
       print()
       print("-" * 15)
       print()
       


def tahmintek():
    global tahmin
    tahmin = int(input("Sayı Tahmininizi Girin:  "))
    print()
    tahminkar()

tahmintek()


   



