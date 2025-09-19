pip install colorama sendgrid
# Microprojeto Sprint: Lista de Tarefas CLI

Este projeto é uma aplicação de linha de comando (CLI) para gerenciamento de tarefas, com persistência em arquivo JSON e recursos extras como saída colorida e envio de tarefas por e-mail via SendGrid.

## Funcionalidades
- Adicionar, listar e remover tarefas
- Persistência das tarefas em `todos.json`
- Saída colorida no terminal (usando Colorama)
- Envio da lista de tarefas por e-mail (SendGrid)

## Como executar
1. Instale as dependências:
   ```
   pip install colorama sendgrid
   ```
2. Execute o programa principal:
   ```
   python Principal.py
   ```

## Testes
Para rodar testes de casos extremos:
```
python -m unittest test_extremos.py
```

## Estrutura dos arquivos
- `Principal.py`: fluxo principal e menu
- `tarefas.py`: funções de manipulação de tarefas
- `email_utils.py`: envio de tarefas por e-mail
- `test_extremos.py`: testes automatizados

---
Desenvolvido para fins didáticos e de demonstração.
