#Strings
print (2**(3+6)%7)

palavra = 'termodinâmica'

print(palavra[2])
print(2*palavra[0])
print(palavra[1:8:3])

nova_palavra = 'algomaneiro'
print(nova_palavra[::-1])
print(nova_palavra[::-2])
print(nova_palavra[::-11])
print(nova_palavra[1:5:2])

palindromo = 'socorram me subi no onibus em marrocos'
print(palindromo[::-1])

#Listas
lista = [1,2,3]
print(lista)
print(lista[0])
print(lista[0]+lista[2])
lista = lista + [4]
lista = lista + [0,0,0]
print(lista[-1])
print(lista[2:-2])

#matriz
linha_1 = [1,2,3]
lista_2 = [0,-1,1]
lista_3 = [3,3,3]

matriz = [linha_1,lista_2,lista_3]
print(matriz)
print(matriz[1][2])

#input
nome = str(input('Qual seu nome?'))
print(nome)

raio = float(input('Qual raio?'))
print(type(raio))

#For
lista_nome = ['João', 'Rafael', 'Douglas']
for nome in lista_nome:
    print(len(nome))

#Range
print(range(1,11,2))
for i in range(len(lista_nome)):
    print(i,lista_nome[i])

#Teste Primo
n = int(input('Número a testar: '))
for i in range(2,n):
    if n % i == 0:
        print('Não é primo')
        break