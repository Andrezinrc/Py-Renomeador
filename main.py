import os
import logging
from PIL import Image
from colorama import init, Fore, Back, Style

init(autoreset=True) 

def banner():
    
    print(f"{Fore.MAGENTA}{Back.BLACK}{Style.BRIGHT}{'':^50}")
    print(f"{Fore.MAGENTA}{Back.BLACK}{Style.BRIGHT}{'':^50}")
    print(f"{Fore.MAGENTA}{Back.BLACK}{Style.BRIGHT}{'':^50}")
    print(f"{Fore.MAGENTA}{Back.BLACK}{Style.BRIGHT}{'----------------------------------------':^50}")
    print(f"{Fore.MAGENTA}{Back.BLACK}{Style.BRIGHT}{'* PROJETO RENOMEADOR DE ARQUIVOS *':^50}")
    print(f"{Fore.MAGENTA}{Back.BLACK}{Style.BRIGHT}{'----------------------------------------':^50}")
    print(f"{Fore.MAGENTA}{Back.BLACK}{Style.BRIGHT}{'':^50}")
    print(f"{Fore.MAGENTA}{Back.BLACK}{Style.BRIGHT}{'':^50}")
    print(f"{Fore.MAGENTA}{Back.BLACK}{Style.BRIGHT}{'':^50}")
    
banner()

logging.basicConfig(filename='renomeador.log', level=logging.INFO)

def converter_imagem(nome_arq, extensao_original, extensao_desejada):
    imagem = Image.open(nome_arq)
    novo_nome = os.path.splitext(nome_arq)[0] + extensao_desejada
    imagem.save(novo_nome)
    return novo_nome

def renomear():
    try:
        print(f"{Fore.BLUE}Exemplo: /caminho/do/diretorio")
        diretorio = input(f"{Fore.YELLOW}Informe o diretório: {Style.RESET_ALL}")

        print(f"{Fore.BLUE}Exemplo: jpg,png")
        escolha_tipo = input(f"{Fore.YELLOW}Escolha o tipo de arquivo ('todos' para todos): {Style.RESET_ALL}")

        print(f"{Fore.BLUE}Exemplo: imagem_")
        padrao_nome = input(f"{Fore.YELLOW}Qual o padrão de nome que deseja: {Style.RESET_ALL}")

        print(f"{Fore.BLUE}Exemplo: jpg")
        extensao_desejada = input(f"{Fore.YELLOW}Informe a extensão desejada para converter (deixe em branco se não quiser): {Style.RESET_ALL}")

        os.chdir(diretorio)
        logging.info(f'Diretório: {os.getcwd()}')

        renomeacoes = []

        for contador, arq in enumerate(os.listdir()):
            if os.path.isfile(arq):
                _, extensao = os.path.splitext(arq)
                extensao = extensao.lower().strip()

                if (escolha_tipo.lower().strip() == 'todos' or
                    extensao in escolha_tipo.split(',')):

                    if extensao_desejada:
                        arq = converter_imagem(arq, extensao, extensao_desejada)

                    nome_arq, exten_arq = os.path.splitext(arq)
                    nome_arq = padrao_nome + ' ' + str(contador + 1)
                    nome_novo = f'{nome_arq}{exten_arq}'

                    renomeacoes.append((arq, nome_novo))
                    os.rename(arq, nome_novo)

        logging.info(f'Renomeações realizadas em {diretorio}: {renomeacoes}')
        print(f"{Fore.GREEN}Renomeações realizadas com sucesso!")

    except Exception as e:
        error_message = f"{Fore.RED}Erro: {e}\nDiretório: {diretorio} não encontrado."
        print(error_message)


renomear()

print(f"{Fore.BLUE}Deseja continuar ou finalizar?")
continuar_ou_finalizar = input(f"{Fore.YELLOW}Digite {Fore.BLUE}S{Fore.YELLOW} para Continuar {Fore.BLUE}N{Fore.YELLOW} para Finalizar: [{Fore.BLUE}s{Fore.YELLOW}/{Fore.BLUE}n{Fore.YELLOW}]: {Style.RESET_ALL}")

if continuar_ou_finalizar.lower() == "s":
   renomear()
else:
   print(f"{Fore.MAGENTA}Obrigado por usar, volte sempre!")
        
