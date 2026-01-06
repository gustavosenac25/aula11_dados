#bibliotecas
import random
import os

#random.rendit -> Números inteiros
# n = random.randint(1, 10)
# m = random.randint(1, 10)
# # print(n, m)

# #radom.uniform -> Números decimais
# n_decimal = random.uniform(1, 10)
# print (n_decimal)
# print (f'{n_decimal:.2f}') #formata o número

# numero_decimal = round(n_decimal, 2) #arredonda o número "2" significa duas casas decimais
# print (numero_decimal)

#Gerar números aleatorios e criar uma lista (for) com x (range) itens
lst_numeros = [random.randint(1, 10) for num in range (5)]
os.system('cls') #Limpa a tela antes de printar
print(lst_numeros)