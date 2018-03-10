import math
from datetime import datetime

#Funções
#def f(x):
#    return x**2

#print(f(3))
#print(math.pi)

def verifica_primo(x):
    for div in range(2,int(math.sqrt(x))+1):
        if x % div == 0:
            return False
    return True

f = open('primos.txt','a')
numero_final = int(input("Até qual numero você quer testar?"))
inicio = datetime.now()
for numero in range(2,numero_final+1):
    if (verifica_primo(numero)):
        f.write(str(numero) + "  ")
final = datetime.now()
f.close()
print(final-inicio)
