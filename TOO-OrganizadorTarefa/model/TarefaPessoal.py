from .Tarefa import Tarefa

class TarefaPessoal(Tarefa):
    def __init__(self, nome_tarefa, descricao=None, data_realizaca=None, tipo=None):
        super().__init__(nome_tarefa, descricao, data_realizaca)
        self.__tipo = tipo


    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo.title()
    
    def exibir_dados(self):
        dados_iniciais = super().exibir_dados()
        if self.__tipo is not None:
            dados_iniciais += f"\nTipo: {self.__tipo}"
        return dados_iniciais