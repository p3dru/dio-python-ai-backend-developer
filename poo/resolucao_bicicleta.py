class Bicicleta:
    def __init__(self, cor: str, modelo: str, ano: int, valor: float): 
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1
    
    def buzinar(self):
        print('fon fon')
    
    def parar(self):
        print('Bicicleta parando...')
        print('Bicicleta parou')
    
    def correr(self):
        print('Bicicleta andando')
    
    def trocar_marcha(self, numero_marcha):
        #melhorar a leitura para referenciar a instancia do objeto
        _self = self

        def _trocar_marcha():
            if numero_marcha != _self.marcha:
                print("Trocando marcha...")
                print("Marcha trocada para a marcha: ", numero_marcha)
                _self.marcha = numero_marcha
            else:
                print("Marcha não trocada, pois a solicitada é a mesma atual")
        
        _trocar_marcha()

    def get_cor(self):
        return self.cor
    
    def __str_dados__(self):
        return f'\nDados da bike:\nCor: {monark.get_cor()}\nMarca: {monark.modelo}\nAno: {monark.ano}\nValor: {monark.valor}'
    
    def __str__(self):
        #criar padrão para todas as classes criadas
        #retorna o nome da classe e as chaves e valores utilizando list-comprehension
        #__dict__.items() = para "tagear" com chave e valor os dados apresentados
        return f"Nome da classe: {self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



monark = Bicicleta('azul', 'Monark', 2010, 250.00)
#monark.buzinar()
#monark.correr()
#monark.parar()

#print(f'\nDados da bike:\nCor: {monark.get_cor()}\nMarca: {monark.modelo}\nAno: {monark.ano}\nValor: {monark.valor}')
dados = monark.__str_dados__()
#dados = monark.__str__()
print(dados)
classe = monark.__str__()
print(classe)

print()
monark.trocar_marcha(1)
monark.trocar_marcha(2)
monark.trocar_marcha(2)
monark.trocar_marcha(3)