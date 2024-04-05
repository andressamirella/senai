#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
mes = []
ac = 0 # aculmula as temperaturas de cada mes
for m in range(12):#calcula a média das temperaturas de cada mes
    print(f"Digite as temperaturas do mes {m+1}")
    for d in range(30): #pegar as temperaturas diarias e guarda numa váriavel.
        t = float(input(f"Digite o valor da temperatura do dia {d+1}:"))
        ac = ac + t
    media = ac/30
    mes.append(media)
    ac = 0
ex = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro","Novembro", "Dezembro"] #dicionario de mes
media_anual = round(sum(mes)/12,2)
print(f"A média de temperature anual foi: {media_anual}º")
for i in range(len(mes)):
    if mes[i] > media_anual:
        print(f" {ex[i]} com uma temperatura acima da média anual, com o valor de:{mes[i]}")
