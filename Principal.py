# Criar uma lista de tarefas a serem feitas (CLI) salva em JSON
from colorama import init, Fore, Style
import tarefas
import email_utils

init(autoreset=True)

def main():
    lista = tarefas.carregar_tarefas()
    while True:
        print(Fore.BLUE + '\n1. Listar tarefas')
        print(Fore.BLUE + '2. Adicionar tarefa')
        print(Fore.BLUE + '3. Remover tarefa')
        print(Fore.BLUE + '4. Enviar tarefas por e-mail (SendGrid)')
        print(Fore.BLUE + '5. Sair')
        opcao = input(Fore.MAGENTA + 'Escolha uma opção: ' + Style.RESET_ALL)
        if opcao == '1':
            tarefas.listar_tarefas(lista, colorama=__import__('colorama'))
        elif opcao == '2':
            tarefas.adicionar_tarefa(lista, colorama=__import__('colorama'))
        elif opcao == '3':
            tarefas.remover_tarefa(lista, colorama=__import__('colorama'))
        elif opcao == '4':
            email_utils.enviar_tarefas_email(lista, colorama=__import__('colorama'))
        elif opcao == '5':
            break
        else:
            print(Fore.YELLOW + 'Opção inválida.')



if __name__ == '__main__':
    main()
