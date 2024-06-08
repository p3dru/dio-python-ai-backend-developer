class Veiculo:
    def __init__(self, cor: str, placa:str, numero_rodas:int):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} -> {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado


    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta('preta', 'gdis-9731', 2)
moto.ligar_motor()
info_moto = moto.__str__()
print(info_moto)

carro = Carro('prata', 'fris-9331', 4)
carro.ligar_motor()
info_carro = carro.__str__()
print(info_carro)


caminhao = Caminhao('roxo', 'csbt-0931', 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao.cor)
info_caminhao = caminhao.__str__()
print(info_caminhao)