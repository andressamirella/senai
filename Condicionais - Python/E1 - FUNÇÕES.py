def piramide(x):
    x = x + 1
    i = 0
    j = 0
    for i in range(x):
       for j in range(i):
        print(i, end = " ")
       print("\n") 
       
n = int(input("Digite um numero: "))
piramide(n)