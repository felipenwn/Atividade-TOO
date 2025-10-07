from .Tarefa import Tarefa
from datetime import datetime

class TarefaProfissional(Tarefa):
    def __init__(self,  data_entrega, nome_tarefa, descricao=None, data_realizacao=None, projeto_relacionado=None):
        super().__init__(nome_tarefa, descricao, data_realizacao)
        self.__projeto_relacionado = projeto_relacionado
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
        return f"[Tarefa Profissional] {super().__str__()}"

    @property
    def projeto_relacionado(self):
        return self.__projeto_relacionado
    
    def exibir_dados(self):
        dados_iniciais = super().exibir_dados()
        if self.__projeto_relacionado is not None:
            dados_iniciais += f"\nProjeto relacionado: {self.__projeto_relacionado}"

        if self.data_entrega is not None:
            data_formatada = self.data_entrega.strftime("%d-%m-%Y")
            dados_iniciais += f"\nData de entrega: {data_formatada}"
        return dados_iniciais