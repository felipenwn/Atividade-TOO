
from model.Tarefa import Tarefa
from model.TarefaEscolar import TarefaEscolar
from model.disciplina import Disciplina


too = Disciplina("Tecnologia de Orientação à Objetos", "Curso BCC", 80, "Professora Vanessa")
calc = Disciplina("Cálculo II", "Curso BCC", 120, "Professor Marcelo ")
bd = Disciplina("Banco de Dados I", "Análise de Sistemas", 80, "Professor Lazzareti")


t1 = Tarefa(
    nome_tarefa="Fazer exercício físico", 
    descricao="1h de jiu-jitsu", 
    data_realizaca="25-09-2025"
)



te1 = TarefaEscolar(
    nome_tarefa="Introdução à Herança",
    disciplina_obj = too,
    data_realizaca="24-09-2025",
    peso=2.0
)

te2 = TarefaEscolar(
    nome_tarefa="Modelagem Entidade-Relacionamento",
    disciplina_obj = bd,
    data_realizaca="30-10-2025",
    data_entrega="10-11-2025",
    peso=3.5
)





print(t1.exibir_dados())

print(te1.exibir_dados())

print(te2.exibir_dados())
