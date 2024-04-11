'''Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.'''

def soma(x,y,z):
    sum = x + y + z
    return sum

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite mais um numero: "))

print("A soma é igual a: ", soma(a,b,c))