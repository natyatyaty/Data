import random


def sortear_porta_premiada():
    """Sorteia aleatoriamente qual das três portas (1, 2 ou 3) contém o prêmio."""
    return random.randint(1, 3)


# 1. Configuração inicial do jogo
porta_premio = sortear_porta_premiada()
porta_escolhida = int(input("Escolha uma das portas (1, 2 ou 3): "))

# 2. Apresentador revela uma porta vazia (que não foi escolhida e não tem o prêmio)
if porta_escolhida == 1:
    porta_revelada = 2 if porta_premio == 3 else 3
elif porta_escolhida == 2:
    porta_revelada = 1 if porta_premio == 3 else 3
else:
    porta_revelada = 1 if porta_premio == 2 else 2

print(f"A porta {porta_revelada} não contém o prêmio!")

# 3. Jogador decide se mantém a escolha inicial ou troca de porta
mudanca = input("Deseja mudar de porta? (S/N): ").strip().upper()

# 4. Resultado final
print(f"\nA porta premiada era a porta número {porta_premio}!")

if mudanca == "N":
    # Mantendo a porta, vence apenas se acertou logo na primeira escolha
    if porta_escolhida == porta_premio:
        print("Parabéns! Você ganhou o prêmio!")
    else:
        print("Você perdeu :(")
else:
    # Trocando de porta, vence sempre que a escolha inicial NÃO era a premiada
    if porta_escolhida != porta_premio:
        print("Parabéns! Você ganhou o prêmio!")
    else:
        print("Você perdeu :(")
