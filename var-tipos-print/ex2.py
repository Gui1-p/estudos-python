"""
    Leia nome e ano de nascimento com input() e imprima "Fulano faz N anos em 2026" usando f-string.
"""

name = input("nome: ")
age = input("idade: ")

print(f"{name} irá fazer {int(age) + 1}  anos")