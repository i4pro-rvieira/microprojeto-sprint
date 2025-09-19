import unittest
import os
import json
from Principal import carregar_tarefas, salvar_tarefas, TODO_FILE

class TestTarefasExtremos(unittest.TestCase):
    def setUp(self):
        # Backup do arquivo original
        if os.path.exists(TODO_FILE):
            os.rename(TODO_FILE, TODO_FILE + '.bak')

    def tearDown(self):
        # Remove arquivo de teste e restaura backup
        if os.path.exists(TODO_FILE):
            os.remove(TODO_FILE)
        if os.path.exists(TODO_FILE + '.bak'):
            os.rename(TODO_FILE + '.bak', TODO_FILE)

    def test_lista_vazia(self):
        # Testa carregar tarefas quando o arquivo não existe
        tarefas = carregar_tarefas()
        self.assertEqual(tarefas, [])

    def test_tarefa_muito_longa(self):
        # Testa salvar e carregar uma tarefa com texto muito longo
        tarefa_longa = 'A' * 10000
        salvar_tarefas([tarefa_longa])
        tarefas = carregar_tarefas()
        self.assertEqual(tarefas[0], tarefa_longa)

    def test_tarefa_com_caracteres_especiais(self):
        # Testa salvar e carregar tarefa com caracteres especiais
        tarefa_esp = 'Tarefa com emoji 🚀 e acentuação: çãõé'
        salvar_tarefas([tarefa_esp])
        tarefas = carregar_tarefas()
        self.assertEqual(tarefas[0], tarefa_esp)

if __name__ == '__main__':
    unittest.main()
