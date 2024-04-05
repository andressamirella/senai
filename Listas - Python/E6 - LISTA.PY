#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
medias = [ ]
acumulo = 0
for i in range(2):
    for j in range(4):
        n = float(input(f"Digite a {j+1}º nota: "))
        acumulo = acumulo + n
    media = acumulo/4
    medias.append(media)
    print(medias)
    acumulo = 0
contador = 0
for i in range(len(medias)):
    if(medias[i] >= 7):
        contador+=1
print(f"O número de alunos com média maior ou igual a 7.0 é {contador}!")