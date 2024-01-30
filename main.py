import os
import shutil
import logging

logging.basicConfig(filename='renomeador.log', level=logging.INFO)

try:
    diretorios = ['/storage/emulated/0/Download/teste']  # Lista de diretórios para renomeação

    for diretorio in diretorios:
        os.chdir(diretorio)
        
        logging.info(f'Diretório: {os.getcwd()}')
        
        padrao_nome = input("Qual o padrão de nomes de arquivo a usar (sem extensão)? ")

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

        logging.info(f'\nRenomeações realizadas em {diretorio}: {renomeacoes}')

    print(f'\nArquivos renomeados com sucesso.')

except Exception as e:
    print(f'Ocorreu um erro: {e}')
    logging.error(f'Ocorreu um erro: {e}')

try:
    # Reverter renomeações
    for diretorio in diretorios:
        for antigo_nome, novo_nome in renomeacoes:
            os.rename(novo_nome, antigo_nome)

    print('\nRenomeações revertidas com sucesso.')

except Exception as e:
    print(f'Ocorreu um erro ao reverter as renomeações: {e}')
    logging.error(f'Ocorreu um erro ao reverter as renomeações: {e}')
