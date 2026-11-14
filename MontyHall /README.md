# 🚪 Problema de Monty Hall (*Let's Make a Deal*)

Simulação interativa em Python do clássico paradoxo probabilístico de **Monty Hall**, desenvolvida durante a trilha trainee do Núcleo de Dados da **Síntese Jr.**

## 📋 Sobre o Problema

Inspirado no programa de televisão norte-americano *Let's Make a Deal* (década de 1960), o desafio funciona da seguinte forma:

1. Existem **3 portas**: atrás de uma há um prêmio e atrás das outras duas não há nada.
2. O participante escolhe uma das portas.
3. O apresentador (que sabe onde está o prêmio) abre uma das portas restantes que está **vazia**.
4. O participante tem a opção de **manter** sua escolha inicial ou **trocar** para a outra porta fechada.

### O Paradoxo
Embora pareça intuitivo que ambas as portas restantes tenham 50% de chance cada, **trocar de porta dobra a probabilidade de vitória**:
* **Manter a porta inicial:** ~33,3% de chance de ganhar.
* **Trocar de porta:** ~66,6% de chance de ganhar.

## 🛠️ Conceitos Aplicados

* Geração de números pseudoaleatórios com a biblioteca nativa `random`
* Definição e chamada de funções
* Estruturas condicionais (`if`, `elif`, `else`)
* Entrada, tratamento e saída de dados no terminal (`input`, `print`, f-strings)
