dia1 = int(input("Entre com o dia da primeira data: ")) 
mes1 = int(input("Entre com o mês da primeira data: ")) 
ano1 = int(input("Entre com o ano da primeira data: "))
print("*" * 9)
dia2 = int(input("Entre com o dia da segunda data: "))
mes2 = int(input("Entre com o mês da segunda data: ")) 
ano2 = int(input("Entre com o ano da segunda data: "))
if ano1 < ano2:
    print(dia1, mes1, ano1, sep="/")
elif ano2 < ano1:
    print(dia2, mes2, ano2, sep="/")
elif mes1 < mes2:
    print(dia1, mes1, ano1, sep="/")
elif mes2 < mes1:
    print(dia2, mes2, ano2, sep="/")
elif dia1 < dia2:
    print(dia1, mes1, ano1, sep="/")
else:
    print(dia2, mes2, ano2, sep="/")