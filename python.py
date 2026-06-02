## ============================================================
## banco.py  —  Pessoa B
## Conteúdo do quiz (perguntas) + memória do jogo (ranking)
## ============================================================

import json
import os

# ------------------------------------------------------------
# CONTRATO com motor.py
# Cada pergunta é um dicionário com ESTAS chaves exatas:
#   "enunciado"   : str  — texto da pergunta
#   "opcoes"      : list — lista de strings com as alternativas
#   "correta"     : int  — índice (começa em 0) da opção certa
#   "categoria"   : str  — ex: "Geografia", "Cinema", "Ciência"
#   "dificuldade" : str  — "facil", "medio" ou "dificil"
#
# IMPORTANTE: não mude os nomes das chaves sem avisar a Pessoa A!
# ------------------------------------------------------------

PERGUNTAS = [

    # ── Futebol ──────────────────────────────────────────────
    {
        "enunciado": "Em apostas esportivas, o que significa a odd 2.00 numa aposta simples?",
        "opcoes": [
            "Você perde o dobro se errar",
            "Você recebe o dobro do valor apostado se acertar",
            "A probabilidade é de 200%",
            "A aposta é inválida",
        ],
        "correta": 1,
        "categoria": "Futebol",
        "dificuldade": "facil",
    },
    {
        "enunciado": "O que é uma aposta 'handicap' no futebol?",
        "opcoes": [
            "Aposta feita por pessoas com deficiência",
            "Vantagem ou desvantagem de gols aplicada a um time para equilibrar as odds",
            "Aposta no número de escanteios",
            "Aposta feita antes do jogo começar",
        ],
        "correta": 1,
        "categoria": "Futebol",
        "dificuldade": "medio",
    },
    {
        "enunciado": "Em qual mercado de apostas você aposta no total de gols de uma partida?",
        "opcoes": ["1X2", "Ambas marcam", "Over/Under", "Placar exato"],
        "correta": 2,
        "categoria": "Futebol",
        "dificuldade": "facil",
    },
    {
        "enunciado": "O que significa 'cash out' numa aposta?",
        "opcoes": [
            "Sacar o dinheiro da conta",
            "Encerrar a aposta antes do fim do evento para garantir lucro ou reduzir perda",
            "Apostar tudo de uma vez",
            "Receber o bônus de boas-vindas",
        ],
        "correta": 1,
        "categoria": "Futebol",
        "dificuldade": "medio",
    },

    # ── Cassino ──────────────────────────────────────────────
    {
        "enunciado": "No jogo de roleta europeia, quantos números existem na mesa (incluindo o zero)?",
        "opcoes": ["36", "37", "38", "40"],
        "correta": 1,
        "categoria": "Cassino",
        "dificuldade": "medio",
    },
    {
        "enunciado": "No blackjack, qual é o objetivo principal do jogador?",
        "opcoes": [
            "Ter exatamente 21 pontos",
            "Ter mais pontos que o dealer sem passar de 21",
            "Ter menos pontos que o dealer",
            "Conseguir três cartas iguais",
        ],
        "correta": 1,
        "categoria": "Cassino",
        "dificuldade": "facil",
    },
    {
        "enunciado": "O que é o 'RTP' em jogos de cassino online?",
        "opcoes": [
            "Real Time Payment (pagamento em tempo real)",
            "Return To Player (percentual médio devolvido ao jogador)",
            "Risk To Play (risco da aposta)",
            "Reward To Partner (recompensa ao afiliado)",
        ],
        "correta": 1,
        "categoria": "Cassino",
        "dificuldade": "medio",
    },
    {
        "enunciado": "Qual carta vale 11 pontos no blackjack (podendo valer também 1)?",
        "opcoes": ["Rei", "Dama", "Valete", "Ás"],
        "correta": 3,
        "categoria": "Cassino",
        "dificuldade": "facil",
    },

    # ── Regras e Conceitos ───────────────────────────────────
    {
        "enunciado": "O que é uma aposta 'múltipla' (ou acumuladora)?",
        "opcoes": [
            "Apostar no mesmo jogo mais de uma vez",
            "Combinar dois ou mais eventos numa só aposta, onde todos precisam acertar",
            "Apostar em múltiplas casas ao mesmo tempo",
            "Dobrar o valor a cada rodada perdida",
        ],
        "correta": 1,
        "categoria": "Regras e Conceitos",
        "dificuldade": "facil",
    },
    {
        "enunciado": "O que significa 'odd' em apostas esportivas?",
        "opcoes": [
            "O valor mínimo para apostar",
            "O número do jogo na plataforma",
            "O multiplicador que define quanto você recebe se acertar",
            "O tempo restante para fechar a aposta",
        ],
        "correta": 2,
        "categoria": "Regras e Conceitos",
        "dificuldade": "facil",
    },
    {
        "enunciado": "Se a odd de um evento é 5.00, qual é a probabilidade implícita de vitória segundo a casa?",
        "opcoes": ["5%", "10%", "20%", "50%"],
        "correta": 2,
        "categoria": "Regras e Conceitos",
        "dificuldade": "dificil",
    },
    {
        "enunciado": "O que é 'apostas ao vivo' (live betting)?",
        "opcoes": [
            "Apostas feitas pessoalmente num cassino físico",
            "Apostas feitas durante o andamento do evento em tempo real",
            "Apostas transmitidas ao vivo nas redes sociais",
            "Apostas com odds fixas que não mudam",
        ],
        "correta": 1,
        "categoria": "Regras e Conceitos",
        "dificuldade": "facil",
    },
]


# ------------------------------------------------------------
# Funções de acesso às perguntas
# ------------------------------------------------------------

def listar_categorias():
    """Retorna uma lista com todas as categorias disponíveis (sem repetição)."""
    categorias = []
    for p in PERGUNTAS:
        if p["categoria"] not in categorias:
            categorias.append(p["categoria"])
    return categorias


def carregar_perguntas(categoria=None, dificuldade=None):
    """
    Devolve a lista de perguntas filtrada.

    Parâmetros:
        categoria   (str | None) — filtra por categoria; None = todas
        dificuldade (str | None) — filtra por dificuldade; None = todas

    Retorno:
        list de dicionários no formato do contrato
    """
    resultado = PERGUNTAS

    if categoria is not None:
        resultado = [p for p in resultado if p["categoria"] == categoria]

    if dificuldade is not None:
        resultado = [p for p in resultado if p["dificuldade"] == dificuldade]

    return resultado


# ------------------------------------------------------------
# Ranking — salvo num arquivo JSON local
# ------------------------------------------------------------

ARQUIVO_RANKING = "ranking.json"


def _carregar_ranking():
    """Lê o arquivo de ranking e devolve a lista. Uso interno."""
    if not os.path.exists(ARQUIVO_RANKING):
        return []
    with open(ARQUIVO_RANKING, "r", encoding="utf-8") as f:
        return json.load(f)


def _salvar_ranking(dados):
    """Grava a lista de ranking no arquivo. Uso interno."""
    with open(ARQUIVO_RANKING, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def salvar_pontuacao(nome, pontos):
    """
    Adiciona a pontuação do jogador ao ranking e mantém
    a lista ordenada da maior para a menor pontuação.

    Parâmetros:
        nome   (str) — nome do jogador
        pontos (int) — quantidade de acertos
    """
    ranking = _carregar_ranking()
    ranking.append({"nome": nome, "pontos": pontos})
    ranking.sort(key=lambda entrada: entrada["pontos"], reverse=True)
    _salvar_ranking(ranking)


def mostrar_ranking():
    """
    Exibe no terminal as 10 melhores pontuações já registradas.
    Se o ranking estiver vazio, avisa o jogador.
    """
    ranking = _carregar_ranking()

    print("\n" + "=" * 35)
    print("        🏆  RANKING  🏆")
    print("=" * 35)

    if not ranking:
        print("  Nenhuma pontuação registrada ainda.")
    else:
        top10 = ranking[:10]
        for posicao, entrada in enumerate(top10, start=1):
            print(f"  {posicao:2}.  {entrada['nome']:<20} {entrada['pontos']} ponto(s)")

    print("=" * 35 + "\n")
    