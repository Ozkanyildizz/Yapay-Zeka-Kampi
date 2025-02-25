#------------- bellekte yer tutmadan sayıların ortalamasını hesaplama -----------------------------------

def number_generator(n):
    """0'dan n'e kadar olan tüm sayıları üreten generator."""
    for num in range(n + 1):  # 0'dan n'e kadar (n dahil) üret
        yield num  

def calculate_average(n):
    """0'dan n'e kadar olan sayıların ortalamasını generator ile hesaplar."""
    total = 0
    count = -1
    for num in number_generator(n):  # Generator kullanarak sayıları üret
        total += num
        count += 1
    return total / count if count > 0 else 0

while True:
    try:
        n = int(input("Bir sayı girin: "))  # Kullanıcıdan giriş al
        average = calculate_average(n)
        print(f"0'dan {n}'e kadar olan sayıların ortalaması: {average:.2f}") # average:.2f = virgülden sonra iki basamağını al
    except Exception:
        print("Lütfen sadece bir tam sayı girin!")  # Hata mesajı ver ve tekrar sor
