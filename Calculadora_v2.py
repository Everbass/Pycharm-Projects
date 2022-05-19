from time import sleep
from ex115.lib.calculos import *

while True:
    opcao = menu(['Somar', 'Subtrair', 'Multiplicar', 'Dividir', 'Maior', 'Menor', 'Raiz', 'Exponenciar', 'Sair da Calculadora'])
    if opcao == 1:
        soma()
    elif opcao == 2:
        subt()
    elif opcao == 3:
        mult()
    elif opcao == 4:
        divi()
    elif opcao == 5:
        maior()
    elif opcao == 6:
        menor()
    elif opcao == 7:
        raiz()
    elif opcao == 8:
        pote()
    elif opcao == 9:
        print()
        cabeçalho('Saindo... Volte Sempre!!!')
        break
    else:
        print('\033[31mERRO!!! Digite uma opção válida.\033[m')
    sleep(1.5)
