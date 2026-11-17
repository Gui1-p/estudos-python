"""
    Leia uma temperatura em Celsius e imprima em Fahrenheit e Kelvin com 2 casas decimais.
"""

tempCelcius = input("Digite a temperatura: ")
tempCelcius = float(tempCelcius)

tempFahrenheit = (tempCelcius * 9/5) + 32

tempKelvin = tempCelcius + 273.15


print(f"Temperatura em Fahrenheit: {tempFahrenheit}")
print(f"Temperatura em Kelvin: {tempKelvin}")