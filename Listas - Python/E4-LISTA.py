#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
lista = []

for i in range(8): 
    c = str(input(f"Digite {i+1} caractere: ").lower())
    lista.append(c)

consoantes = 0
conso_achadas = []
for i in lista:
   if i.isalpha() and i not in ['a', 'e', 'i', 'o', 'u']:
       consoantes += 1
       conso_achadas.append(i)
print(consoantes)
print(conso_achadas)

