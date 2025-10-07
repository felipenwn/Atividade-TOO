from model.Tarefa import Tarefa
from model.TarefaEscolar import TarefaEscolar
from model.disciplina import Disciplina

t1 = Tarefa("Aula TOO", "teste")
print(t1.exibir_dados())
t1.concluir()
print(t1.exibir_dados())

t2 = Tarefa("Fazer compras mercado", "teste", "19-09-2025")
print(t2.exibir_dados())

print(t2)

t3 = Tarefa("Fazer compras mercado", "teste", "19-09-2025")

if(t2 == t3):
    print("Tarefas iguais")
else:
    print("Tarefas diferentes")
    
t4 = TarefaEscolar("introducao Herança, polimorfismo", "POO", 5, "teste herança", "20-09-2025", "25-09-2025")
print(t4)
