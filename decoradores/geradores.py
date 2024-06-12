#geradores são um tipo de interador, mas economiza memória de maneira otimizada
#https://docs.python.org/3/howto/functional.html#generators


#"Iteradores para estruturas mais complexas e geradores para mais simples"

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in meu_gerador(numeros=[1,2,3]):
    print(i)