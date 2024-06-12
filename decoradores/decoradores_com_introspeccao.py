"""
Definimos uma função decoradora, passando uma outra função como
argumento que permitem adicionar
funcionalidades extras em uma função sem modificar seu código
"""

#vantagens de uso: https://blog.rocketseat.com.br/decoradores-em-python-domine-essa-estrategia/
import functools


def meu_decorador(funcao):
    #torna o código mais mantenível por editar os metadados
    @functools.wraps(funcao)
    #criamos uma função dentro do decorador que irá executar o que for passado
    #*args, **kwargs são qualquer atributos que podem ser passados por qualquer para a função
    def envelope(*args, **kwargs):
        print("Executa algo antes de executar a função passada")
        #inserindo args e kwags, o código fica facilmente adaptável à alterações e armazenando
        resultado = funcao(*args, **kwargs)
        print("Executa algo depois de executar a função passada")
        #podemos usar posteriormente o valor
        return resultado
    
    #retorna a execução de envelope pelo decorador 
    return envelope

#chama o decorador sobre a função passada, dizendo que ela será executada de acordo com os parâmetros do decorador

@meu_decorador
def ola_mundo(nome, idade):
    print(f"Olá {nome}, sua idade é de {idade} anos")
    return nome.upper()

resultado = ola_mundo("João", 23)
print(resultado)
#sem o decorator, a saída seria "envelope"
print(ola_mundo.__name__)