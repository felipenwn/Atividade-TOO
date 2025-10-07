class Agendamento:
    def __init__(self, data_inicio, data_final, atividades, nome, local):
        self.__data_inicio = data_inicio
        self.__data_final = data_final
        self.__atividades = atividades
        self.__nome = nome
        self.__local = local

    @property
    def data_inicio(self):
        return self.__data_inicio

    @property
    def data_final(self):
        return self.__data_final

    @property
    def atividades(self):
        return self.__atividades

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome_agendamento):
        self.__nome = nome_agendamento.title() 

    @property
    def local(self):
        return self.__local
    
    def exibir_dados(self):
        dados = f"Agendamento: {self.nome}\nLocal: {self.local}\nData Início: {self.data_inicio}\nData Final: {self.data_final}\nAtividades: {', '.join(self.atividades)}"
        return dados