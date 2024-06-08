class Foo:
    def __init__(self, x=None) -> None:
        self._x = x
    
    @property
    #passando property, podemos chamar a função como atributo
    def x(self):
        return self._x or 0
    
    @x.setter
    #permite uma atribuição direta como se fosse um método não protegido
    def x(self, value):
        self._x += value

    @x.deleter
    #permite a execução direta da "deleção" como atributo
    def x(self):
        self._x = 0

foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
#print(foo.x()) funcionaria caso não tivésssemos colocado o decorator
