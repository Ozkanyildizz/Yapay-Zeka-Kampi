# 1.1  Kalıtım (Inheritance) - Miras Alma
class Hayvan:

    def konus(self):
        print("Hayvan konuşuyor")

class Kedi(Hayvan):

    def konus(self):
        print("Kedi miyavlıyor")

class Kopek(Hayvan):

    def konus(self):
        print("Köpek havlıyor")    

hayvan = Hayvan()
hayvan.konus()

kedi = Kedi()
kedi.konus()

kopek = Kopek()
kopek.konus()

# 1.2 

class Araba:
    
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileriGoster(self):
        print(f"Araba: {self.marka} {self.model} {self.yil}")

class ElektrikliAraba(Araba):
    
    def __init__(self, marka, model, yil, pil_seviyesi):

        super().__init__(marka, model, yil) # Araba sınıfının __init__ metodunu da çağırır
        self.pil_seviyesi = pil_seviyesi

    def sarj_et(self, miktar):

        self.pil_seviyesi += miktar
        if self.pil_seviyesi > 100:
            self.pil_seviyesi = 100
        print(f"Pil seviyesi: {self.pil_seviyesi}%")

class Benzinliaraba(Araba):
    
    def __init__(self, marka, model, yil, yakit_seviyesi):

        super().__init__(marka, model, yil)
        self.yakit_seviyesi = yakit_seviyesi
    
    def yakit_ekle(self, miktar):

        self.yakit_seviyesi += miktar
        print(f"Yakıt seviyesi: {self.yakit_seviyesi} litre")
    
elektrikli_araba = ElektrikliAraba("Tesla", "Model S", 2021, 50)
elektrikli_araba.bilgileriGoster()
elektrikli_araba.sarj_et(30)

benzinli_araba = Benzinliaraba("Audi", "A4", 2021, 50)
benzinli_araba.bilgileriGoster()
benzinli_araba.yakit_ekle(200)
