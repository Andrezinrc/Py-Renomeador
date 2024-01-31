import os
import shutil
import logging

logging.basicConfig(filename='renomeador.log', level=logging.INFO)

try:
    # Lista de diretórios para renomeação
    diretorios = []

    diretorio = input("\033[34mInforme o diretorio exemplo (diretorio/para/renomeacao): \033[m")

    diretorios.append(diretorio)
    # diretorios = ['/diretorio/para/renomeacao']

    for diretorio in diretorios:
        os.chdir(diretorio)

        logging.info(f'\033[32mDiretório: {os.getcwd()}\033[m')

        padrao_nome = input("\033[34mQual o padrão de nomes de arquivo a usar (sem extensão)? \033[m")

        # Lista para armazenar os antigos e novos nomes dos arquivos
        renomeacoes = []

        for contador, arq in enumerate(os.listdir()):
            if os.path.isfile(arq):
                nome_arq, exten_arq = os.path.splitext(arq)
                nome_arq = padrao_nome + ' ' + str(contador)

                nome_novo = f'{nome_arq}{exten_arq}'

                # Armazena os antigos e novos nomes
                renomeacoes.append((arq, nome_novo))

                # Renomeia o arquivo
                os.rename(arq, nome_novo)

        logging.info(f'\n\033[32mRenomeações realizadas em {diretorio}: {renomeacoes}\033[m')

    print(f'\n\033[32mArquivos renomeados com sucesso.\033[m')

    # Pergunta ao usuário se deseja reverter as renomeações
    reverter = input('\033[34mDeseja reverter as renomeações? (S/N): \033[m').lower()

    if reverter == 's':
        # Reverter renomeações
        for antigo_nome, novo_nome in renomeacoes:
            os.rename(novo_nome, antigo_nome)

        print('\n\033[32mRenomeações revertidas com sucesso.\033[m')

except Exception as e:
    print(f'\033[31mOcorreu um erro: {e}\033[m')
    logging.error(f'Ocorreu um erro: {e}')
