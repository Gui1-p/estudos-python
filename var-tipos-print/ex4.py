"""
    Leia um número de segundos e imprima no formato HH:MM:SS com zeros à esquerda. Use //, % e o formato :02d.
"""

segundos = input("Digite o tempo decorrido em segundos: ")
segundos = int(segundos)

horas = segundos // 3600

minutos = (segundos % 3600) // 60

segundos = (segundos % 3600) % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")