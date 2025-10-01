from .Tarefa import Tarefa

class TarefaEscolar(Tarefa):
    def __init__(self, nome_tarefa, disciplina, peso=0, descricao=None, data_realizaca=None, data_entrega=None):
        super().__init__(nome_tarefa, descricao, data_realizaca)
        self.__disciplina = disciplina
        self.__peso = peso
        self.data_entrega = data_entrega
        
    
    def __str__(self):
        return f"[Tarefa Escolar] {super().__str__()}"