"""
    Leia nome e ano de nascimento com input() e imprima "Fulano faz N anos em 2026" usando f-string.
"""

name = input("nome: ")
data = input("Ano de nascimento: ")

print(f"{name} faz {2026 - int(data)}  anos")