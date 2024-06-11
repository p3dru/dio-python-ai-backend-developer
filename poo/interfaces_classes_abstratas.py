'''
Python não possui a palavra reservada "interface",
porém podemos criar classes abstratas que definem
apenas o que ela deve fazer e não como fazer
Apenas estabelece os contratos
'''
from abc import ABC, abstractmethod, abstractproperty


#assim, a classe ABC(abstrata), não pode ser chamada 
#diretamente
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    
    #informa que todas as classes filhas devem ter 
    #essa propriedade
    
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada")
        print()
    
    def desligar(self):
        print("Desligando a TV...")
        print("Desligada")
        print()
    
    @property
    def marca(self):
        return "Sanguessuga"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar...")
        print("Ligado")
        print()
    
    def desligar(self):
        print("Desligando o Ar...")
        print("Desligado")
        print()

    @property
    def marca(self):
        return "GL"


'''
Todas as classes que implementarem de um método
abstrato, precisam implementar seus métodos OBRIGATORIAMENTE.
Não importando se é uma filha, neta, bisneta...
'''

controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()
print(f"Marca do controle da Tv: {controle_tv.marca}")

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(f"Marca do controle do Ar: {controle_ar.marca}")
