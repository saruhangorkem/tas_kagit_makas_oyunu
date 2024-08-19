import random

def tas_kagit_makas_SARUHAN_TURKOZ():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Kurallar:")
    print("KURAL 1: Oyuncu ve Gamer taş, kağıt veya makas arasında seçim yapar.")
    print("KURAL 2: Taş, makası yener; kağıt, taşı yener; makas, kağıdı yener.")
    print("KURAL 3: İki turu kazanan oyunu kazanır.")
    print("KURAL 4: Olası bir beraberlik durumunda oyuncuya 2 seçenek sunulur bu seçenekler sonucunda o rauntun kazananı belirlenir(rulet oyunu / sayı seçme oyunu)")
    print("KURAL 5: Eğer oyuncu o raunt içinde kendini şanslı hissederse kendimi şanslı hissediyorum butonu olan s tuşuna basarak random bir seçenek sunabilir")
    print("Oyun başlamadan önce, çıkmak isterseniz 'q' tuşuna basabilirsiniz.")

    secenekler = ["taş", "kağıt", "makas"]
    oyun_sayisi = 0

    while True:
        oyun_sayisi += 1
        oyuncu_galibiyetleri = 0
        gamer_galibiyetleri = 0
        print(f"\nOyun {oyun_sayisi} başlıyor!")

        tur_sayisi = 0
        while oyuncu_galibiyetleri < 2 and gamer_galibiyetleri < 2:
            tur_sayisi += 1
            print(f"\nTur {tur_sayisi}")

            oyuncu_secimi = input("Taş, kağıt, makas? (Çıkmak için 'q', şanslı hissetmek için 's'): ").lower()

            if oyuncu_secimi == 'q':
                print("Oyundan çıkılıyor...")
                return

            elif oyuncu_secimi == 's':
                oyuncu_secimi = random.choice(secenekler)
                print(f"Kendinizi şanslı hissettiniz! Seçiminiz: {oyuncu_secimi}")

            elif oyuncu_secimi not in secenekler:
                print("Geçersiz seçim, tekrar deneyin.")
                continue

            gamer_secimi = random.choice(secenekler)
            print(f"Gamer'ın seçimi: {gamer_secimi}")

            if oyuncu_secimi == gamer_secimi:
                print("Beraberlik!")

                while True:
                    secim = input("Beraberlik durumunda bir seçenek seçin (1: 1-10 arası rastgele sayı seçimi, 2: Rus Ruleti): ")

                    if secim == '1':
                        rastgele_sayi = random.randint(1, 10)
                        print("Oyun, 1 ile 10 arasında rastgele bir sayı seçecek.")
                        
                        oyuncu_rastgele = int(input("1 ile 10 arasında bir sayı seçin: "))
                        gamer_rastgele = random.randint(1, 10)
                        print(f"Gamer'ın seçimi: {gamer_rastgele}")

                        oyuncu_mesafe = abs(oyuncu_rastgele - rastgele_sayi)
                        gamer_mesafe = abs(gamer_rastgele - rastgele_sayi)

                        print(f"Seçilen rastgele sayı: {rastgele_sayi}")

                        if oyuncu_mesafe < gamer_mesafe:
                            print(f"Oyuncunun seçimi: {oyuncu_rastgele}")
                            print(f"Gamer'ın seçimi: {gamer_rastgele}")
                            print("Seçilen rastgele sayıya en yakın olan oyuncu! Bu turu kazandınız!")
                            oyuncu_galibiyetleri += 1
                            break
                        elif gamer_mesafe < oyuncu_mesafe:
                            print(f"Oyuncunun seçimi: {oyuncu_rastgele}")
                            print(f"Gamer'ın seçimi: {gamer_rastgele}")
                            print("Seçilen rastgele sayıya en yakın olan Gamer! Bu turu Gamer kazandı!")
                            gamer_galibiyetleri += 1
                            break
                        else:
                            print("Her iki taraf da eşit uzaklıkta. Tekrar seçim yapılıyor...")

                    elif secim == '2':
                        mermi_yeri = random.randint(1, 5)
                        print(f"Rus Ruleti başlıyor! Mermi {mermi_yeri} numaralı atışta.")

                        for atis in range(1, 6):
                            if atis == mermi_yeri:
                                if atis % 2 == 1:
                                    print(f"{atis}. Atış: Oyuncuya isabet etti! Gamer kazandı!")
                                    gamer_galibiyetleri += 1
                                else:
                                    print(f"{atis}. Atış: Gamer'a isabet etti! Oyuncu kazandı!")
                                    oyuncu_galibiyetleri += 1
                                break
                            else:
                                if atis % 2 == 1:
                                    print(f"{atis}. Atış: Oyuncu kurtuldu!")
                                else:
                                    print(f"{atis}. Atış: Gamer kurtuldu!")
                        break

                    else:
                        print("Geçersiz seçenek. Lütfen '1' veya '2' girin.")

            else:
                if (oyuncu_secimi == "taş" and gamer_secimi == "makas") or \
                   (oyuncu_secimi == "kağıt" and gamer_secimi == "taş") or \
                   (oyuncu_secimi == "makas" and gamer_secimi == "kağıt"):
                    print("Bu turu kazandınız!")
                    oyuncu_galibiyetleri += 1
                else:
                    print("Bu turu Gamer kazandı!")
                    gamer_galibiyetleri += 1

        if oyuncu_galibiyetleri == 2:
            print("\nTebrikler! Oyunu kazandınız!")
        else:
            print("\nGamer oyunu kazandı.")

        while True:
            devam = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
            if devam in ["evet", "hayır"]:
                break
            print("Geçersiz giriş. Lütfen 'evet' veya 'hayır' yazın.")
        
        gamer_devam = random.choice(["evet", "hayır"])
        print(f"Gamer devam etmek istiyor mu? {gamer_devam}")

        if devam != "evet" or gamer_devam != "evet":
            print("Oyun sona eriyor.")
            break

if __name__ == "__main__":
    tas_kagit_makas_SARUHAN_TURKOZ()
