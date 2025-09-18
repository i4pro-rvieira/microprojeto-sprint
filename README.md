# Google Tasks CSV Exporter

## Descrição
Este microprojeto implementa integração com a API do Google Tasks e funcionalidade de exportação para CSV. O projeto permite buscar todas as suas tarefas do Google Tasks e exportá-las para um arquivo CSV para análise e backup.

## Funcionalidades
- 🔐 Autenticação OAuth2 com Google Tasks
- 📋 Busca de todas as listas de tarefas
- ✅ Recuperação de todas as tarefas de todas as listas
- 💾 Exportação para CSV com formatação adequada
- 📊 Visualização resumida das tarefas no console
- 🔍 Listagem de listas de tarefas disponíveis

## Configuração

### 1. Pré-requisitos
- Python 3.7+
- Conta Google com Google Tasks habilitado

### 2. Instalação
```bash
# Instalar dependências
pip install -r requirements.txt
```

### 3. Configuração da API Google
1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Habilite a Google Tasks API
4. Crie credenciais OAuth 2.0:
   - Vá para "Credenciais" → "Criar credenciais" → "ID do cliente OAuth"
   - Tipo de aplicação: "Aplicação para computador"
   - Baixe o arquivo JSON de credenciais
5. Renomeie o arquivo para `credentials.json` e coloque na pasta do projeto

## Instalação Rápida

### Script de Setup Automático
```bash
# Execute o script de setup automático
./setup.sh
```

## Uso

### Comandos Básicos
```bash
# Exportar todas as tarefas para CSV
python main.py

# Exportar com nome de arquivo específico
python main.py --output minhas_tarefas.csv

# Mostrar resumo das tarefas no console
python main.py --summary

# Apenas listar as listas de tarefas disponíveis
python main.py --list-only

# Combinar opções
python main.py --summary --output backup_tarefas.csv
```

### Exemplos de Uso
```bash
# Exemplo 1: Exportação simples
python main.py
# Gera arquivo: google_tasks_export_20231218_143052.csv

# Exemplo 2: Com resumo e arquivo personalizado
python main.py -s -o minhas_tarefas_2023.csv
# Mostra resumo no console e salva em minhas_tarefas_2023.csv
```

## Estrutura do CSV
O arquivo CSV exportado contém as seguintes colunas:
- `title`: Título da tarefa
- `notes`: Notas/descrição da tarefa
- `status`: Status (needsAction, completed)
- `due`: Data de vencimento
- `completed`: Data de conclusão
- `updated`: Data da última atualização
- `taskListTitle`: Nome da lista de tarefas
- `id`: ID único da tarefa

## Uso com Docker

### Construir a imagem
```bash
docker build -t google-tasks-exporter .
```

### Executar com Docker
```bash
# Criar diretório para dados (credenciais e exports)
mkdir -p ./data

# Copiar suas credenciais para o diretório de dados
cp credentials.json ./data/

# Executar exportação
docker run -v $(pwd)/data:/app/data google-tasks-exporter

# Executar com opções específicas
docker run -v $(pwd)/data:/app/data google-tasks-exporter --summary --output /app/data/minhas_tarefas.csv
```

## Exemplos de Uso Programático

Consulte o arquivo `example.py` para ver como usar os módulos programaticamente em seus próprios scripts.

```bash
# Executar exemplo
python example.py
```

## Arquivos do Projeto
- `main.py`: Script principal da aplicação
- `google_tasks.py`: Cliente para integração com Google Tasks API
- `csv_exporter.py`: Módulo de exportação para CSV
- `config.py`: Configurações da aplicação
- `requirements.txt`: Dependências do projeto
- `setup.sh`: Script de instalação automática
- `example.py`: Exemplo de uso programático
- `test.py`: Suite de testes
- `Dockerfile`: Configuração para uso com Docker
- `credentials.json.template`: Template para credenciais OAuth
- `credentials.json`: Credenciais OAuth (criado pelo usuário)
- `token.json`: Token de acesso (gerado automaticamente)

## Variáveis de Ambiente (Opcionais)
```bash
export GOOGLE_CREDENTIALS_FILE=caminho/para/credentials.json
export GOOGLE_TOKEN_FILE=caminho/para/token.json
```

## Licença
Este projeto é parte de um curso e está disponível para fins educacionais.
