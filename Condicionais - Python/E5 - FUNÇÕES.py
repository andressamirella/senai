'''Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.'''

def somaImposto(taxa, custo):
    p = (custo * taxa)/100
    custoTotal = p + custo
    print("O custo total do item é: ",custoTotal)

t = float(input("Digite o valor do Imposto:"))
c = float(input("Digite o valor do Produto:"))
somaImposto(t,c)


