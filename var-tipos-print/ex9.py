inteiro = input("Digite um inteiro para converter..: ")

inteiro = int(inteiro)

hexadecimal = hex(inteiro)
octal = oct(inteiro)
binario = bin(inteiro)

print(f"{hexadecimal}")
print(f"{octal}")
print(f"{binario}")

print("Retorno")

print(f"{int(hexadecimal, 16)}")
print(f"{int(octal, 8)}")
print(f"{int(binario, 2)}")