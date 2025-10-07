
from model.Tarefa import Tarefa
from model.agendamento import Agendamento
from model.TarefaPessoal import TarefaPessoal
from model.TarefaProfissional import TarefaProfissional
from model.compromisso import Compromisso




tarefa_pessoal = TarefaPessoal(
    nome_tarefa="Fazer Compras",
    tipo="Doméstica",
    data_realizaca="07-10-2025"
)


tarefa_profissional = TarefaProfissional(
    nome_tarefa="Fazer Site do INF-IFSul",
    projeto_relacionado="Projeto Olhares Digitais",
    data_entrega="10-10-2025",
    descricao="Criar um site responsivo para o INF-IFSul",
)


agendamento_almoco = Agendamento(
    nome="Almoço em família",
    local="Restaurante na Gare",
    data_inicio="08-10-2025 12:30",
    data_final="08-10-2025 14:00",
    atividades=["Confraternização", "amigo-secreto"]
)


compromisso_medico = Compromisso(
    nome="ir ao médico",
    local="Clínica Saúde & Bem-estar, sala 10",
    data_inicio="09-10-2025 09:00",
    data_final="09-10-2025 10:00",
    atividades=["consultar", "pegar receita"],
    descricao="Não esquecer cartão do sus."
)



print("DADOS DA TAREFA PESSOAL:")
print(tarefa_pessoal.exibir_dados())

print("DADOS DA TAREFA PROFISSIONAL:")
print(tarefa_profissional.exibir_dados())


print("DADOS DO AGENDAMENTO:")
print(agendamento_almoco.exibir_dados())


print("DADOS DO COMPROMISSO:")
print(compromisso_medico.exibir_dados())

