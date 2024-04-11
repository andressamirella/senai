'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.'''
def conversao(horas, minutos):
    if horas == 0:
        horas_12 = 12
        periodo = "A"
    elif horas < 12:
        horas_12 = horas
        periodo = "A"
    elif horas == 12:
        horas_12 = horas
        periodo = "P"
    else:
        horas_12 = horas - 12
        periodo = "P"
    return horas_12, minutos, periodo

def imprime_conversao(horas, minutos, periodo):
    print(f"{horas}:{minutos} {periodo}.M")


while True:
    h = int(input("Digite as horas no formato 24h (0 - 23): "))
    m = int(input("Digite os minutos (0 - 59): "))

    horas_12, minutos, periodo = (conversao(h,m))
    imprime_conversao(horas_12, minutos, periodo)

    continuar = input("Deseja continuar convertendo (s/n): ").lower()
    if (continuar != "s"):
        break