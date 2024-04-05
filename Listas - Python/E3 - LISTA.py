#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
for i in range(4):
    n = float(input(f"Digite a {i+1} nota: "))
    notas.append(n)
media = sum(notas)/ len(notas)
print(notas)
print(f"A média é {media} {notas}")