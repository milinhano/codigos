class Tarefa:
    tarefas = []
    quantidade = 0
    
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = False
        Tarefa.tarefas.append(self)
        Tarefa.quantidade += 1
        
    def __str__(self):
        return f'{self.titulo} | {self.descricao}'
    
    @classmethod
    def listarTarefas(cls):
        for tarefa in cls.tarefas:
            print(tarefa)
    
    @classmethod
    def quantidadeTarefas(cls):
            print(cls.quantidade)
            
tarefa_01 = Tarefa('Corrigir Provas', 'Corrigir provas 01')
tarefa_02 = Tarefa('Estudar Python', 'Estudar Orientação a objetos')

Tarefa.listarTarefas()
Tarefa.quantidadeTarefas()