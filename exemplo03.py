#exercícios função

import random

def gerar_numeros(ini, fin, qtd): #não esquecer de colocar : (dois pontos) no final
    lst_num = [random.randint(ini, fin) for i in range(qtd)] #quando é escrito assim, ou seja, n]ao só operação com simbolos, tem que colocar []
    return lst_num

def somar_numeros(ini, fin): #não esquecer de colocar : (dois pontos) no final
    soma = ini + fin
    return soma

def subtrair_numeros(ini, fin): #não esquecer de colocar : (dois pontos) no final
    sub = ini - fin
    return sub

def multiplicar_numeros(ini, fin): #não esquecer de colocar : (dois pontos) no final
    mult = ini * fin
    return mult

def dividir_numeros(ini, fin): #não esquecer de colocar : (dois pontos) no final
    div = ini / fin
    return div

inicio = 1
final = 100
quantidade = 2
lst_numeros = gerar_numeros(inicio, final, quantidade)
resultado1 = somar_numeros(lst_numeros[0], lst_numeros[1])
resultado2 = subtrair_numeros(lst_numeros[0], lst_numeros[1])
resultado3 = multiplicar_numeros(lst_numeros[0], lst_numeros[1])
resultado4 = dividir_numeros(lst_numeros[0], lst_numeros[1])
print(lst_numeros)
print(f' a soma de {lst_numeros[0]} + {lst_numeros[1]} é {resultado1}')
print(f' a subtração de {lst_numeros[0]} - {lst_numeros[1]} é {resultado2}')
print(f' a multiplicação de {lst_numeros[0]} x {lst_numeros[1]} é {resultado3}')
print(f' a divisão de {lst_numeros[0]} / {lst_numeros[1]} é {resultado4:.2f}') #:.xf é para formatar a quantidade de número após a vírgula

