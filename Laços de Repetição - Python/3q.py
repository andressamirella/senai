'''Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';'''

nome = str(input("Digite seu nome: "))
while len(nome) <= 3:
    nome = str(input("Nome inválido! Digite um nome novamente: "))
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida! Digite sua idade novamente: "))
salario = float(input("Digite o seu salário: "))
while salario <= 0:
    salario = float(input("Valor inválido! Digite o seu salário novamente: "))
sexo = str(input("Digite o seu sexo (f) ou (m): ").lower())
while sexo not in ['f','m']:
    sexo = str(input("Letra inválida!Digite o seu sexo (f) ou (m): ").lower())
estado = str(input("Digite seu estado civil c/s/v/d: ").lower())
while estado not in["c","s","v","d"]:
    estado = str(input("Opção inválida! Digite seu estado civil c/s/v/d: ").lower())
print("Cadastro finalizado com sucesso!")


