from .Tarefa import Tarefa
from .disciplina import Disciplina
from datetime import datetime

class TarefaEscolar(Tarefa):
    def __init__(self, nome_tarefa, disciplina_obj, peso=0, descricao=None, data_realizaca=None, data_entrega=None):
        super().__init__(nome_tarefa, descricao, data_realizaca)
        self.__disciplina = disciplina_obj
        self.__peso = peso
        self.__data_entrega = None 
        self.data_entrega = data_entrega
        
    @property
    def data_entrega(self):
        return self.__data_entrega

    @data_entrega.setter
    def data_entrega(self, data):
        if data is not None:
            try:
                self.__data_entrega = datetime.strptime(data, "%d-%m-%Y")
            except ValueError:
                print(f"Data de ENTREGA em formato inválido. Use dd-mm-yyyy.")
    def __str__(self):
        return f"[Tarefa Escolar] {super().__str__()}"
    
    def exibir_dados(self):
        dados_iniciais = super().exibir_dados()
        if self.__disciplina is not None:
            dados_iniciais += f"\nDisciplina: {self.__disciplina}"
        if self.__peso > 0:
            dados_iniciais += f"\nPeso: {self.__peso}"
        if self.data_entrega is not None:
            data_formatada = self.data_entrega.strftime("%d-%m-%Y")
            dados_iniciais += f"\nData de entrega: {data_formatada}"
        return dados_iniciais