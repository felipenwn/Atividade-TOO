from .Tarefa import Tarefa
from .agendamento import Agendamento

class Compromisso(Agendamento, Tarefa):
    def __init__(self, data_inicio, data_final, atividades, nome, local, descricao=None, data_realizaca=None):
        Tarefa.__init__(self, nome, descricao, data_realizaca)
        Agendamento.__init__(self, data_inicio, data_final, atividades, nome, local)



def exibir_dados(self):
    status = "CONCLUIDO" if self._Tarefa__concluido else "A FAZER"
    dados_iniciais = f"Compromisso: {self.nome} [{status}]" 
    dados_iniciais += f"\nLocal: {self.local}"
    dados_iniciais += f"\nInício: {self.data_inicio} | Final: {self.data_final}"
    if self.atividades:
        dados_iniciais += f"\nAtividades: {', '.join(self.atividades)}"
    if self.descricao:
        dados_iniciais += f"\nDescrição: {self.descricao}"
    return dados_iniciais