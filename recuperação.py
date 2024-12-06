from colorama import init, Fore, Style
import matplotlib.pyplot as plt

# Inicializa o colorama (necessário para funcionar em Windows)
init(autoreset=True)

# Lista de alunos em recuperação
recuperacao = [
    "ANA JULIA LIBORIO SOUZA",
    "BEATRIZ VICTORIA CARIAS DA SILVA",
    "CAIO VICTOR DA COSTA SANTOS",
    "GABRIEL ALVES MENDES DA SILVA",
    "GUILHERME DOS SANTOS DA SILVA",
    "ISABELLY APARECIDA DA SILVA",
    "KAUAN REGIS DOS SANTOS NASCIMENTO",
    "MIGUEL FERNANDES OLIVEIRA",
    "MURILO MATIAS DOS SANTOS",
    "ANA GABRIELE DA SILVA NEIVA DE LIMA",
    "BIANCA FERREIRA DOS SANTOS",
    "CLAUDIO DIAS DE OLIVEIRA JUNIOR",
    "DAVID LUIS OLIVEIRA DE BARROS",
    "DOUGLAS DE MORAES LOPES DA SILVA",
    "ELAINE ROCHA COSTA",
    "EMILLY ARAUJO SANTOS",
    "GABRIEL RICARDO GONCALVES DA SILVA",
    "KELVIN XAVIER DE SOUZA",
    "LUCAS DE SOUZA GONCALVES",
    "FLAVIA EDUARDA DE OLIVEIRA SANTOS",
]

# Função para validar o nome do aluno
def validar_nome(nome):
    nome_formatado = nome.strip().upper()
    nome_formatado = ''.join(e for e in nome_formatado if e.isalnum() or e.isspace())  # Remove caracteres especiais
    if nome_formatado == "":
        print(f"{Fore.RED}Nome inválido! Por favor, insira um nome válido.{Style.RESET_ALL}")
        return None
    return nome_formatado

# Função para solicitar as notas
def solicitar_notas():
    notas = []
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"{Fore.YELLOW}Digite a nota do {i}º bimestre (0 a 10): {Style.RESET_ALL}"))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print(f"{Fore.RED}A nota deve ser um número entre 0 e 10.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Entrada inválida. Digite um número.{Style.RESET_ALL}")
    return notas

# Função para calcular soma e média das notas
def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return soma, media

# Função para exibir gráficos das notas
def exibir_grafico(notas):
    bimestres = ['1º', '2º', '3º', '4º']
    plt.bar(bimestres, notas, color='skyblue')
    plt.xlabel('Bimestres')
    plt.ylabel('Notas')
    plt.title('Desempenho Bimestral do Aluno')
    plt.ylim(0, 10)
    plt.show()

# Função para exibir o resultado
def exibir_resultado(nome, soma, media, notas):
    print(f"\n{Fore.CYAN}Soma das notas: {soma:.2f}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Média: {media:.2f}{Style.RESET_ALL}")

    # Determinar aprovação com base na média
    if media >= 5:
        print(f"{Fore.GREEN}✔️ Parabéns, o aluno está aprovado! 🎉{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}❌ Infelizmente, o aluno está reprovado. 😔{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Dica: Revise os conteúdos dos bimestres para melhorar!{Style.RESET_ALL}")

    # Verificar se o aluno está na lista de recuperação
    if nome in recuperacao:
        print(f"{Fore.YELLOW}⚠️ Observação: O aluno está na lista de recuperação.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Isso não afeta a aprovação direta, mas atenção é necessária! 💪{Style.RESET_ALL}")

    # Exibir gráfico das notas
    exibir_grafico(notas)

# Função para revisar as notas
def revisar_notas(notas):
    print(f"{Fore.YELLOW}Você pode revisar as notas agora.{Style.RESET_ALL}")
    for i in range(4):
        while True:
            try:
                nova_nota = float(input(f"{Fore.CYAN}Digite a nova nota para o {i+1}º bimestre (atual: {notas[i]}): {Style.RESET_ALL}"))
                if 0 <= nova_nota <= 10:
                    notas[i] = nova_nota
                    break
                else:
                    print(f"{Fore.RED}A nota deve ser um número entre 0 e 10.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Entrada inválida. Digite um número.{Style.RESET_ALL}")
    return notas

# Função principal
def main():
    print(f"{Fore.CYAN}Bem-vindo ao sistema de gerenciamento de notas!{Style.RESET_ALL}")
    nome = validar_nome(input("Digite o nome do aluno: "))
    if not nome:
        return

    notas = solicitar_notas()
    soma, media = calcular_media(notas)
    exibir_resultado(nome, soma, media, notas)

    opcao = input(f"{Fore.YELLOW}Deseja revisar as notas? (S/N): {Style.RESET_ALL}").strip().upper()
    if opcao == 'S':
        notas = revisar_notas(notas)
        soma, media = calcular_media(notas)
        exibir_resultado(nome, soma, media, notas)

if _name_ == "_main_":
    main()
