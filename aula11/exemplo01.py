#bibliotecas
import random

#random.rendit -> Números inteiros
n = random.randint(1, 10)
m = random.randint(1, 10)
# print(n, m)

#radom.uniform -> Números decimais
n_decimal = random.uniform(1, 10)
print (n_decimal)
print (f'{n_decimal:.2f}') #formata o número

numero_decimal = round(n_decimal, 2) #arredonda o número "2" significa duas casas decimais
print (numero_decimal)