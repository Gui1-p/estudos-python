"""
    Dada s = "Engenharia de Computacao", imprima: o tamanho, tudo em maiúsculas, a primeira palavra, os 3 últimos caracteres, a string invertida e quantas vezes aparece a letra a.
"""

s = "Engenharia de Computacao"

print(f"Tamanho: {len(s)}")

print(f"{s.upper()}")

print(f"{s.split()[0]}")

print(s[len(s) - 3: len(s)])

print(s[:: -1])

print(s.count("a"))