#Iteradores servem como um recurso comum para looping e list comprehension
#para entrar mais à fundo: https://www.alura.com.br/artigos/o-que-sao-iteradores-no-python
class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
    #define que o objeto recebido seja iterado
    #caso não tenha, recebe o erro na execução de "object is not iterable" or "nonetype"
    def __iter__(self):
        return self

    #"segue" para o próximo, pela quantidade de itens recebidos
    #sem o StopIteration, continua executando eternamente
    def __next__(self):
        #tenta executar
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        #se não der certo, para a iteração
        except IndexError:    
            raise StopIteration

for i in MeuIterador(numeros = [38, 13, 11]):
    print(i)
