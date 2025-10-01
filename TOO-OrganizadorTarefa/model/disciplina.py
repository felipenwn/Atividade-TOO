class Disciplina:
    def __init__(self, nome_disc, curso, carga, professor):
        self.nome =nome_disc
        self.curso = curso
        self.carga = carga
        self.professor = professor

    def __str__(self):
        return f"{self.nome} ({self.curso})"