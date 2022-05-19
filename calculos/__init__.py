from math import sqrt, pow

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO!!! Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Calculadora V2.0')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\33[m - \033[34m{item}\033[m')
        c = c+1
    print(linha())
    opc = leiaint('\n\033[32mDigite sua opção de cálculo:\033[m ')
    return opc


def soma(x=0, y=0):
    print('Você escolheu a opção \033[33m1 - Somar\033[m:')
    x = leiaint('Entre com o primeiro número: ')
    y = leiaint('Entre com o segundo número: ')
    n = x + y
    print(linha())
    print(f'{x} + {y} = {n}')


def subt(x=0, y=0):
    print('Você escolheu a opção \033[33m2 - Subtrair\033[m:')
    x = leiaint('Entre com o primeiro número: ')
    y = leiaint('Entre com o segundo número: ')
    n = x - y
    print(linha())
    print(f'{x} - {y} = {n}')


def mult(x=0, y=0):
    print('Você escolheu a opção \033[33m3 - Multiplicar\033[m:')
    x = leiaint('Entre com o primeiro número: ')
    y = leiaint('Entre com o segundo número: ')
    n = x * y
    print(linha())
    print(f'{x} x {y} = {n}')


def divi(x=0, y=0):
    print('Você escolheu a opção \033[33m4 - Dividir\033[m:')
    x = leiaint('Entre com o primeiro número: ')
    y = leiaint('Entre com o segundo número: ')
    n = x / y
    print(linha())
    print(f'{x} / {y} = {n}')


def maior(x=0, y=0):
    print('Você escolheu a opção \033[33m5 - Qual é o maior entre dois números digitados\033[m:')
    x = leiaint('Entre com o primeiro número: ')
    y = leiaint('Entre com o segundo número: ')
    if x > y:
        maior == x
        print(linha())
        print(f'{x} é o maior número')
    elif x < y:
        maior == y
        print(linha())
        print(f'{y} é o maior número')
    else:
        print(linha())
        print(f'Os números digitados são iguais.')


def menor(x=0, y=0):
    print('Você escolheu a opção \033[33m6 - Qual é o menor entre dois números digitados\033[m:')
    x = leiaint('Entre com o primeiro número: ')
    y = leiaint('Entre com o segundo número: ')
    if x > y:
        print(linha())
        menor == y
        print(f'{y} é o menor número')
    elif x < y:
        print(linha())
        menor == x
        print(f'{x} é o menor número')
    else:
        print(linha())
        print(f'Os números digitados são iguais.')


def raiz(x=0, y=0):
    print('Você escolheu a opção \033[33m7 - Raiz Quadrada\033[m:')
    x = leiaint('Entre com o número: ')
    rx = sqrt(x)
    print(linha())
    print(f'A raiz de {x} é {rx}.')


def pote(x=0, y=0):
    print(f'Você escolheu a opção \033[33m8 - Exponenciar\033[m:')
    x = leiaint('Entre com o primeiro número: ')
    y = leiaint('Entre com o segundo número: ')
    px = pow(x, y)
    py = pow(y, x)
    print(linha())
    print(f'{x} elevado a {y}ª potência é {px}. {y} elevado a {x}ª potência é {py}.')