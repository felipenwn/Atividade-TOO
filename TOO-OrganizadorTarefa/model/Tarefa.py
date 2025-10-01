from datetime import datetime

class Tarefa:
    def __init__(self, nome_tarefa, descricao=None, data_realizaca=None):
        self.nome = nome_tarefa
        self.__concluido = False
        self.__descricao = descricao
        self.__data_realizacao = None  ## ja atribui none para a data de realização arrumando o erro quue dava ao exibir_dados sem data
        self.data_realizacao = data_realizaca

    
    ## encapsulamento: getter e setter
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome_tarefa):
        self.__nome = nome_tarefa.title()
        
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc
        
    @property
    def data_realizacao(self):
        return self.__data_realizacao
    
    @data_realizacao.setter
    def data_realizacao(self, data):
        if data is not None:
            try:
                self.__data_realizacao = datetime.strptime(data, "%d-%m-%Y")
            except ValueError as e:
                print(f"Data em formato inválido: {e}")
        
    
    
    ## outros métodos
    def concluir(self):
        self.__concluido = True    
    
    def exibir_dados(self):
        status = "CONCLUIDO" if self.__concluido == True else "A FAZER"
        dados = f"Tarefa cadastrada:\n{self.nome} [{status}]"

        if self.data_realizacao is not None:
            data_formatada = self.data_realizacao.strftime("%d-%m-%Y")
            dados += f"\nData de realização: {data_formatada}" 
        if self.descricao is not None:
            dados += f"\nDescrição: {self.descricao}"
        
        return dados

    
    
    def __str__(self):
        status = "CONCLUIDO" if self.__concluido == True else "A FAZER"
        return f"Tarefa cadastrada: {self.__nome} [{status}]"
    
    def __eq__(self, outro):
        if(self.nome == outro.nome and self.data_realizacao == outro.data_realizacao):
            return True
        else:
            return False