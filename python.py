## ============================================================
## motor.py  —  Pessoa A
## Responsabilidade: a LÓGICA do jogo
## Funções: fazer_pergunta, jogar, mostrar_resultado
## ============================================================


## ------------------------------------------------------------
## fazer_pergunta(pergunta)
##
## Recebe UM dicionário de pergunta e:
##   1. Mostra o enunciado
##   2. Mostra as opções numeradas (1, 2, 3...)
##   3. Lê a resposta do jogador
##   4. Valida: se digitar letra ou número fora da faixa,
##      pede de novo até receber algo válido
##   5. Devolve o número digitado (int)
## ------------------------------------------------------------

def fazer_pergunta(pergunta):
    print("\n" + pergunta["enunciado"])

    for i in range(len(pergunta["opcoes"])):
        print(str(i + 1) + ". " + pergunta["opcoes"][i])

    total_opcoes = len(pergunta["opcoes"])
    resposta_valida = False

    while not resposta_valida:
        resposta_texto = input("Sua resposta (1 a " + str(total_opcoes) + "): ")

        ## verifica se o que foi digitado é número
        if resposta_texto.isdigit():
            resposta_int = int(resposta_texto)

            ## verifica se está dentro da faixa de opções
            if resposta_int >= 1 and resposta_int <= total_opcoes:
                resposta_valida = True
            else:
                print("Número fora da faixa. Digite entre 1 e " + str(total_opcoes) + ".")
        else:
            print("Entrada inválida. Digite apenas o número da opção.")

    return resposta_int


## ------------------------------------------------------------
## jogar(perguntas)
##
## Recebe a LISTA de perguntas (vinda do banco.py) e:
##   1. Percorre cada pergunta com for + range(len(...))
##   2. Chama fazer_pergunta() para cada uma
##   3. Compara a resposta com o campo "correta" (índice base 0)
##   4. Avisa se acertou ou errou (mostrando a resposta certa)
##   5. Acumula os pontos
##   6. Devolve o total de acertos
## ------------------------------------------------------------

def jogar(perguntas):
    pontos = 0

    for i in range(len(perguntas)):
        resposta = fazer_pergunta(perguntas[i])

        indice_escolhido = resposta - 1
        indice_certo = perguntas[i]["correta"]

        if indice_escolhido == indice_certo:
            print("Correto!")
            pontos = pontos + 1
        else:
            opcao_certa = perguntas[i]["opcoes"][indice_certo]
            print("Errado! A resposta certa era: " + opcao_certa)

    return pontos


## ------------------------------------------------------------
## mostrar_resultado(pontos, total)
##
## Recebe quantos pontos o jogador fez e o total de perguntas.
## Mostra o placar e uma mensagem conforme o desempenho:
##   - acertou tudo        -> "Ótimo!"
##   - acertou metade ou + -> "Bom!"
##   - acertou menos       -> "Continue treinando!"
## ------------------------------------------------------------

def mostrar_resultado(pontos, total):
    print("\n===========================")
    print("Resultado: " + str(pontos) + " de " + str(total) + " pontos")

    if pontos == total:
        print("Ótimo! Você gabaritou!")
    elif pontos >= total / 2:
        print("Bom! Mas dá pra melhorar.")
    else:
        print("Continue treinando!")

    print("===========================")