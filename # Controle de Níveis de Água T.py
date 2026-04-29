from colorama import Fore, Style, init

# Inicializa o colorama
init()

def definir_cor_nivel(nivel):
    """Retorna a cor baseada no nível informado."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

def monitorar_interativo():
    # Lista com as situações (índice 0 é Nível 1, índice 1 é Nível 2, etc.)
    situacoes = [
        "Muito baixo (crítico)",
        "Baixo",
        "Médio",
        "Alto",
        "Muito alto (alerta)"
    ]

    print("--- SISTEMA DE MONITORAMENTO ---")
    
    try:
        # 1. Pergunta o nível ao usuário
        escolha = int(input("Digite o nível da água (1 a 5): "))

        # 2. Verifica se o nível é válido (está entre 1 e 5)
        if 1 <= escolha <= 5:
            # Busca a mensagem na lista (subtraímos 1 pois a lista começa em 0)
            mensagem = situacoes[escolha - 1]
            cor = definir_cor_nivel(escolha)

            # 3. Exibe a mensagem com a cor e restaura o padrão
            print(f"\nSituação atual: {cor}{mensagem}{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}Erro: Nível inválido! Digite um número de 1 a 5.{Style.RESET_ALL}")

    except ValueError:
        # Caso o usuário digite algo que não seja um número inteiro
        print(f"\n{Fore.RED}Erro: Por favor, digite apenas números inteiros.{Style.RESET_ALL}")

if __name__ == "__main__":
    monitorar_interativo()