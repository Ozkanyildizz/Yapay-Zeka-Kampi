from my_math_module import HesapMakinesi
import math

toplama = HesapMakinesi([15, 6, 5], "+")
print(toplama.dort_islem())

cikarma = HesapMakinesi([15, 6, 5], "-")
print(cikarma.dort_islem())

carpma = HesapMakinesi([15, 6, 5], "*")
print(carpma.dort_islem())

bolme = HesapMakinesi([15, 6, 5], "/")
print(bolme.dort_islem())

us = HesapMakinesi([2, 3], "**")
print(us.dort_islem())

trigonometrik_islem = HesapMakinesi([math.pi],"sin")
print(trigonometrik_islem.trigonmetri())