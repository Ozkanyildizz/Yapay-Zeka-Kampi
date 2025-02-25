# 2.1
sayi1 = float(input("birinci sayı: "))
sayi2 = float(input("ikinci sayı: "))

try:
    print(sayi1/sayi2)

except ZeroDivisionError as a :
    print("Bölen sayı sıfır olamaz: ", a)

#2.2 My eror message 

class MyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    if sayi2 == 0:
        raise MyError("Bölen sayı sıfır olamaz.")
    print(sayi1 / sayi2)
except MyError as e:
    print(e)