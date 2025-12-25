from Crypto.Util.number import *
from sympy import factorint

n = int(input("n = "))
e = int(input("e = "))
c = int(input("c = "))

factors = factorint(n)

if len(factors) != 2:
    raise ValueError("Ce n\'est pas un produit de deux nombres premiers")

p, q = factors.keys()

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)

print(f"Message déchiffré ={m}")
