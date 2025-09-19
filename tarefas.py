import json
import os

TODO_FILE = 'todos.json'

def carregar_tarefas():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

def listar_tarefas(tarefas, colorama=None):
    if not tarefas:
        if colorama:
            print(colorama.Fore.YELLOW + 'Nenhuma tarefa encontrada.')
        else:
            print('Nenhuma tarefa encontrada.')
    for i, tarefa in enumerate(tarefas, 1):
        if colorama:
            print(colorama.Fore.CYAN + f"{i}. {tarefa}")
        else:
            print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas, colorama=None):
    if colorama:
        tarefa = input(colorama.Fore.GREEN + 'Digite a nova tarefa: ' + colorama.Style.RESET_ALL)
    else:
        tarefa = input('Digite a nova tarefa: ')
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    if colorama:
        print(colorama.Fore.GREEN + 'Tarefa adicionada!')
    else:
        print('Tarefa adicionada!')

def remover_tarefa(tarefas, colorama=None):
    listar_tarefas(tarefas, colorama)
    try:
        if colorama:
            idx = int(input(colorama.Fore.RED + 'Digite o número da tarefa para remover: ' + colorama.Style.RESET_ALL)) - 1
        else:
            idx = int(input('Digite o número da tarefa para remover: ')) - 1
        if 0 <= idx < len(tarefas):
            removida = tarefas.pop(idx)
            salvar_tarefas(tarefas)
            if colorama:
                print(colorama.Fore.RED + f'Tarefa removida: {removida}')
            else:
                print(f'Tarefa removida: {removida}')
        else:
            if colorama:
                print(colorama.Fore.YELLOW + 'Índice inválido.')
            else:
                print('Índice inválido.')
    except ValueError:
        if colorama:
            print(colorama.Fore.YELLOW + 'Entrada inválida.')
        else:
            print('Entrada inválida.')
