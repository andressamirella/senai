# Solicita que o jogador A entre com sua escolha
jogadorA = input("Entre com a primeira escolha: ")

# Solicita que o jogador B entre com sua escolha
jogadorB = input("Entre com a segunda escolha: ")

# Verifica se a escolha do jogadorA é "pedra"
if jogadorA == "pedra": 
    # Se a escolha do jogadorB também for "pedra", é um empate
    if jogadorB == "pedra":
        print("Empate")
    # Se a escolha do jogadorB for "tesoura", jogador A ganha
    elif jogadorB == "tesoura":
        print("O jogador A ganhou") 
    # Caso contrário, jogador B ganha
    else:
        print("O jogador B ganhou")
# Verifica se a escolha do jogadorA é "tesoura"
elif jogadorA == "tesoura": 
    # Se a escolha do jogadorB for "pedra", jogador B ganha
    if jogadorB == "pedra":
        print("O jogador B ganhou") 
    # Se a escolha do jogadorB também for "tesoura", é um empate
    elif jogadorB == "tesoura":
        print("Empate") 
    # Caso contrário, jogador A ganha
    else:
        print("O jogador A ganhou")
# Verifica se a escolha do jogadorA é "papel"
elif jogadorA == "papel": 
    # Se a escolha do jogadorB for "pedra", jogador A ganha
    if jogadorB == "pedra":
        print("O jogador A ganhou")
    # Se a escolha do jogadorB for "tesoura", jogador B ganha
    elif jogadorB == "tesoura":
        print("O jogador B ganhou")
    # Caso contrário, é um empate
    else:
        print("Empate")
# Se nenhuma das opções anteriores foi escolhida pelos jogadores
else: 
    # Se a escolha do jogadorB for "pedra", jogador A ganha
    if jogadorB == "pedra": 
        print("O jogador A ganhou")
    # Se a escolha do jogadorB for "tesoura", jogador B ganha
    elif jogadorB == "tesoura": 
        print("O jogador B ganhou")
    # Caso contrário, é um empate
    else: 
        print("Empate")
