# iterator kullanımı

class EvenNumbers:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.max_value:
            raise StopIteration
        return self.current
    
even_numbers = EvenNumbers(10)
for number in even_numbers:
    print(number)


# Generator kullanımı --------------------------------------------

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# İlk 10 Fibonacci sayısını ekrana yazdır
for number in fibonacci(10):
    print(number)