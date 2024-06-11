class Estudante:
    #variável de classe
    escola = "Dio"

    def __init__(self, nome, matricula) -> None:
        #variáveis de objeto
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Gi", 2)

mostrar_valores(aluno_1, aluno_2)

aluno_1.matricula = 3

mostrar_valores(aluno_1, aluno_2)