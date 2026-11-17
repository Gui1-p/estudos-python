"""
    Antes de rodar, escreva num comentário o que você acha que cada linha imprime; depois confira: 7 / 2, 7 // 2, -7 // 2, -7 % 2, 2 ** 0.5, int(3.99), round(2.5), "3" * 3, 3 * "3", True + 1.
"""


"""
    round: aredonda um numero (num, digitos)
"""

print(f"{7 / 2}")       #printa 1 -> errado é 3.5 , pois float é valido

print(f"{7 // 2}")      #printa 3 

print(f"{-7 // 2}")     #printa -3  => errado é -4  -> em python o arredondamento de inteiros é para baixo e não para zero

print(f"{-7 % 2}")      #printa -1 -> errado é 1 -> isso se deve para que (a//b)*b + a%b = a

print(f"{2 ** 0.5}")    #printa o valor de raiz de 2 

print(f"{int(3.99)}")   #printa 4 ->errado é 3 -> em python o casting pra int corta a parte decimal, não arredonda

print(f"{round(2.5)}")  #printa 3 -> errado é 2 -> round arredonda para o par mais proximo

print(f"{"3" * 3}")     #printa 333

print(f"{3 * "3"}")     # printa 333

print(f"{True + 1}")    #printa 2