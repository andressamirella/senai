# Solicita ao usuário para inserir três números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# Verifica qual número é o menor usando condicionais
if num1 <= num2 and num1 <= num3:
    menor_numero = num1
elif num2 <= num1 and num2 <= num3:
    menor_numero = num2
else:
    menor_numero = num3

# Imprime o menor número encontrado
print("O menor número é:", menor_numero)
