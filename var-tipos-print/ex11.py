"""
    == compara apenas os valores
    is compara os objetos
    c = 1 e d = 1, é possivel que o c is d seja true por um reaproveitamento de memoria feito pelo python
    entretanto caso haja mudança desse valor eles passam a ser objetos diferentes
    matrizes ou tipos que exigem ponteiros não terão este probklema já que o endereço de memoria ja os diferencia

"""

a = 256
b = 256

a is b

c = [1,2,3]
d = [1,2,3]

c is d

a+= 1

a is b
