import random

# 4.1 Ehliyet alma durumu
age = int(input("Yaşınızı giriniz: "))
print("Ehliyet alabilirsiniz." if age >= 18 else "Ehliyet almak için yaşınız tutmuyor.")

#4.2 Tahmin oyunu
guess = int(input("Bir sayı giriniz: "))
number = random.randint(1, 10)
print("Tebrikler! Doğru tahmin." if number == guess else f"Üzgünüm, doğru tahmin {number} olacaktı.")

#4.3.1 Amiral battı oyunu tek gemi

def one_ship():
    print("""
Amiral Battı Oyununa Hoş Geldiniz!
5x5 bir tahtada geminin yerini bulmaya çalışın.""")
    board = [random.randint(1, 5) , random.randint(1, 5)]
    try_count = 5
    while try_count != 0:
        row = int(input("Satır giriniz: "))
        column = int(input("Sütun giriniz: "))
        if row == board[0] and column == board[1]:
            print("Tebrikler! Gemiyi buldunuz.")
            break
        else:
            try_count -= 1
            if try_count == 0:
                print("Üzgünüm, hakkınız bitti. Gemiyi bulamadınız. Doğru konum: ", board)
                break
            else:
                print("Üzgünüm, gemiyi bulamadınız. Tekrar deneyin. Kalan deneme hakkınız: ", try_count)

#4.3.2 Amiral battı oyunu iki gemi


def check_ship(row, column,row_guess, column_guess):
    if row == row_guess and column == column_guess:
        return True
    else:
        return False

def two_ship():
    print("""
Amiral Battı Oyununa Hoş Geldiniz!
5x5 bir tahtada iki tane geminin yerini bulmaya çalışın.""")
    ship1 = [random.randint(1, 5) , random.randint(1, 5)]
    ship2 = [random.randint(1, 5) , random.randint(1, 5)]
    print(ship1, ship2)
    try_count = 5
    while try_count != 0:
        row_guess1 = int(input("İlk gemi için satır giriniz(1,5): "))
        column_guess1 = int(input("İlk gemi için sütun giriniz(1,5): "))
        row_guess2 = int(input("İkinci gemi için satır giriniz(1,5): "))
        column_guess2 = int(input("İkinci gemi için sütun giriniz(1,5): "))
        if check_ship(ship1[0], ship1[1], row_guess1, column_guess1) and check_ship(ship2[0], ship2[1], row_guess2, column_guess2):
            print("Tebrikler! Gemileri buldunuz.")
            break
        elif check_ship(ship1[0], ship1[1], row_guess1, column_guess1) and not check_ship(ship2[0], ship2[1], row_guess2, column_guess2):
            print("Birinci gemiyi buldunuz. İkinci gemiyi bulmaya devam edin.")
            while try_count != 0:
                row_guess2 = int(input("İkinci gemi için satır giriniz(1,5): "))
                column_guess2 = int(input("İkinci gemi için sütun giriniz(1,5): "))
                if check_ship(ship2[0], ship2[1], row_guess2, column_guess2):
                    print("Tebrikler! Gemileri buldunuz.")
                    break
                else:
                    try_count -= 1
                    if try_count == 0:
                        print("Üzgünüm, hakkınız bitti. Gemileri bulamadınız. Doğru konum: ", ship1 , ship2)
                        break
                    else:
                        print("Üzgünüm, gemileri bulamadınız. Tekrar deneyin. Kalan deneme hakkınız: ", try_count)
        elif check_ship(ship2[0], ship2[1], row_guess2, column_guess2) and not check_ship(ship1[0], ship1[1], row_guess1, column_guess1):
            print("İkinc gemiyi buldunuz. Birinci gemiyi bulmaya devam edin.")
            while try_count != 0:
                row_guess1 = int(input("Birinci gemi için satır giriniz(1,5): "))
                column_guess1 = int(input("Birinci gemi için sütun giriniz(1,5): "))
                if check_ship(ship1[0], ship1[1], row_guess1, column_guess1):
                    print("Tebrikler! Gemileri buldunuz.")
                    break
                else:
                    try_count -= 1
                    if try_count == 0:
                        print("Üzgünüm, hakkınız bitti. Gemileri bulamadınız. Doğru konum: ", ship1 , ship2)
                        break
                    else:
                        print("Üzgünüm, gemileri bulamadınız. Tekrar deneyin. Kalan deneme hakkınız: ", try_count)
        else:
            try_count -= 1
            if try_count == 0:
                print("Üzgünüm, hakkınız bitti. Gemileri bulamadınız. Doğru konum: ", ship1 , ship2)
                break
            else:
                print("Üzgünüm, gemileri bulamadınız. Tekrar deneyin. Kalan deneme hakkınız: ", try_count)

# one_ship()
two_ship()
