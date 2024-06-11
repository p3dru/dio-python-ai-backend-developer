class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade
    
    @classmethod
    #transforma em método de classe (troca self pelo cls), pode alterar a classe, nesse caso como construtor
    #se precisa de acesso ao contexto de classe
    def criar_data_nasc(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    #cria uma função estática (não altera a classe)
    #se não precisa de um contexto de classe, nem de classe e nem da instância
    def eh_maior_idade(idade):
        return idade >= 18


    
p = Pessoa("Guilherme", 28)
print(p.nome, p.idade)

p2 = Pessoa.criar_data_nasc(2000, 11, 12, "Pedro")
print(p2.nome, p2.idade)
print(Pessoa.eh_maior_idade(17))
print(Pessoa.eh_maior_idade(28))