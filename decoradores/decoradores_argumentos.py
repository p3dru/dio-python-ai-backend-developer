"""
Definimos uma função decoradora, passando uma outra função como
argumento que permitem adicionar
funcionalidades extras em uma função sem modificar seu código
"""

#vantagens de uso: https://blog.rocketseat.com.br/decoradores-em-python-domine-essa-estrategia/


def meu_decorador(funcao):
    #criamos uma função dentro do decorador que irá executar o que for passado
    #*args, **kwargs são qualquer atributos que podem ser passados por qualquer para a função
    def envelope(*args, **kwargs):
        print("Executa algo antes de executar a função passada")
        #inserindo args e kwags, o código fica facilmente adaptável à alterações
        funcao(*args, **kwargs)
        print("Executa algo depois de executar a função passada")
    
    #retorna a execução de envelope pelo decorador 
    return envelope

#chama o decorador sobre a função passada, dizendo que ela será executada de acordo com os parâmetros do decorador

@meu_decorador
def ola_mundo(nome, idade):
    print(f"Olá {nome}, sua idade é de {idade} anos")

ola_mundo("João", 23)