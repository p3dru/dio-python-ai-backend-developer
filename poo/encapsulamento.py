class Conta:
    def __init__(self, numero_agencia, saldo: int = 0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo

conta = Conta("0001", 230)
conta.depositar(100)
print(conta.numero_agencia)
print(conta.mostrar_saldo())