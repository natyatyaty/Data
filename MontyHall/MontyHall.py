#Função que sorteia a porta que contém o prêmio
import random
def portaPremiada():
  porta = random.randint(1,3)
  return porta

#Usuário escolhe a porta
portaEscolhida = int(input("Escolha uma das portas(1, 2 ou 3): "))
portaPremio = portaPremiada()

#Condicionais para revelar uma das portas que não contém o prêmio
if portaEscolhida == 2:
  if portaPremio == 1:
    print("A porta 3 não contém o prêmio!")
  else:
    print("A porta 1 não contém o prêmio!")
elif portaEscolhida == 3:
  if portaPremio == 1:
    print("A porta 2 não contém o prêmio!")
  else:
    print("A porta 1 não contém o prêmio!")
else:
  if portaPremio == 3:
    print("A porta 2 não contém o prêmio!")
  else:
    print("A porta 3 não contém o prêmio!")

#Pergunta se o usuário deseja mudar de porta
mudanca = input("Deseja mudar de porta?(S/N)").upper()

#Condicionais que revelam a porta premiada e se o usuário ganhou

#Caso em que o usuário não mudou de porta
if mudanca == 'N':
  if portaPremio == 1:
    print(f"A porta premiada era a porta número ... {portaPremio}!")
    if portaEscolhida == 1:
      print("Parabéns! Você ganhou o prêmio!")
    else:
      print("Você perdeu :(")
  elif portaPremio == 2:
    print(f"A porta premiada era a porta número ... {portaPremio}!")
    if portaEscolhida == 2:
      print("Parabéns! Você ganhou o prêmio!")
    else:
      print("Você perdeu :(")
  else:
    print(f"A porta premiada era a porta número ... {portaPremio}!")
    if portaEscolhida == 3:
      print("Parabéns! Você ganhou o prêmio!")
    else:
      print("Você perdeu :(")
#Caso em que o usuário mudou de porta
else:
  portaEscolhida = int(input("Escolha sua nova porta: "))
  if portaPremio == 1:
    print(f"A porta premiada era a porta número ... {portaPremio}!")
    if portaEscolhida == 1:
      print("Parabéns! Você ganhou o prêmio!")
    else:
      print("Você perdeu :(")
  elif portaPremio == 2:
    print(f"A porta premiada era a porta número ... {portaPremio}!")
    if portaEscolhida == 2:
      print("Parabéns! Você ganhou o prêmio!")
    else:
      print("Você perdeu :(")
  else:
    print(f"A porta premiada era a porta número ... {portaPremio}!")
    if portaEscolhida == 3:
      print("Parabéns! Você ganhou o prêmio!")
    else:
      print("Você perdeu :(")
