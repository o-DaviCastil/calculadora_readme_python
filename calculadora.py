#Calculadora
print (f'{" Calculadora ":=^40}')
import math 

while True:
    def inicio():
        ini= input(''' 
[1] - Iniciar a calculadora
                
Digite 1 para começar a calcular: ''')
        
        print(('=-')*16)

        if ini not in ['1', '2']:
            print ('Opção inválida. Inicie novamente.')
        return ini
    ini = inicio()

    if ini == '1':
        esc= input('''[1] - Operações básicas
[2] - Cálculo de média
[3] - Equação 
[4] - Fatorial
[5] - Conversão de Unidades
[6] - Tabuada
[7] - fibonacci
                
Escolha uma calculadora: ''')
        
        if esc not in ['1', '2', '3', '4', '5', '6', '7']:
            print ('Opção inválida. Inicie novamente.')

    print ('=-'*16)
            
    def operaçoes_basicas():
            
            resultado = float(input('Insira um valor: '))

            while True:

                op= input('''Escolha a operação:
[+] - Soma
[-] - Subtração
[*] - Multiplicação
[/] - Divisão
[=] - Fim: ''')
                
                if op == '=':
                    break
                
                if op not in ['+', '-', '*', '/', '=']:
                    print('''OPÇÃO INVÁLIDA.
Insira uma das opções apresentadas''')
                    continue
                
                valor = float(input('Insira outro valor: '))
                if op == '+':
                    resultado += valor

                elif op == '-':
                    resultado -= valor

                elif op == '*':
                    resultado *= valor

                elif op == '/':
                    resultado /= valor

            print (f'Reultado: {resultado}')

    def média():
        opc = input('''[1] - Média Aritimética
[2] - Média Ponderada

Selecione o tipo de média: ''')
        
        if opc != '1' and opc != '2':

            print('''Escolha uma das opções acima.
Inicie novamente. ''')
            
        soma = 0
        quantidade = 0
        if opc == '1':

            while True:
                nota = input ("Insira o valor (ou 'sair' para finalizar): ")
                if nota.lower() == "sair" :
                    break

                soma += float (nota)
                quantidade += 1
            if quantidade > 0:
                media = soma / quantidade
                print(f"\nA média das notas é: {media:.2f}")
            else:
                print("nenhuma nota foi digitada.")

        if opc == '2':
            soma_valor = 0
            soma_pesos = 0

            while True:
                valor = input("Digite o valor(ou 'sair' para finalizar): ")

                if valor.lower() == "sair": 
                    break
                
                peso = float(input("digite o peso desse valor: "))
                valor = float(valor)
                soma_valor += valor * peso
                soma_pesos += peso

            if soma_pesos > 0:
                media = soma_valor / soma_pesos

                print(f"\nA média ponderada é: {media:.2f}")

            else:
                print("nenhuma nota foi digitada.")                                                                                                                                                                          
        
            
    def equação():

        
        eq= input('''[1] - 1° Grau
[2] - 2° Grau

Escolha o grau da equação: ''')

        if eq == '1':

            esc = input('Qual variável você quer descobrir? ').lower()

            if esc == 'x':

                a= float(input('Digite o valor do coeficiente angular (a): '))

                b= float(input('Digite o valor do coeficiente linear (b): '))

                y= float(input('Digite o valor de y: '))

                x= (y-b)/a

                print (f'O valor de X é {x}.')

            elif esc == 'y':
                a= float(input('Digite o valor do coeficiente angular (a): '))

                b= float(input('Digite o valor do coeficiente linear (b): '))

                x= float(input('Digite o valor de x: '))

                y= a*x+b

                print (f'O valor de Y é {y}.')

        elif eq == '2':
            a= float(input('Insira o valor do coeficiente quadrático (a): '))

            b= float(input('Insira o valor do coeficiente linear (b): '))

            c= float(input('Insira o valor do termo idependente (c): '))

            delta= math.pow(b, 2) - (4 * a * c)

            if delta < 0:
                print('''Valor não faz parte dos números reais.
Aguarde atualizações da calculadora...''')
                
            else:
                x1= ((-b) - math.sqrt(delta))/(2*a)
                x2= ((-b) + math.sqrt(delta))/(2*a)

                
                print (f'O valor de x1 é: {x1} e de x2 é: {x2}.')
        
    def fatorial():
        while True:
            numero = input("digite um número (ou 'sair' para finalizar): ")
            if numero.lower() == "sair":
                break
            numero = int(numero)
            fatorial = 1
            for i in range(1, numero + 1):
                fatorial *= i
            print(f"O fatorial de {numero} é: {fatorial}\n")

    def conversão_de_medidas():
        print('Escolha a conversão:')
        print('[1] Quilômetros (km)')
        print('[2] Decímetros (dm)')
        print('[3] Centímetros (cm)')
        print('[4] Milímetros (mm)')
        opcao = int(input('Sua opção: '))
        metros = float(input('Agora, digite a quantidade de metros:'))
        if opcao == 1:
            resultado = metros / 1000
            print(f'{metros}m equivale a {resultado} (km)')

        elif opcao == 2:
            resultado = metros * 10
            print(f'{metros}m equivale a {resultado} (dm)')

        elif opcao == 3:
            resultado = metros * 100
            print(f'{metros}m equivale a {resultado} (cm)')

        elif opcao == 4:
            resultado = metros * 1000
            print(f'{metros}m equivale a {resultado} (mm)')

        else:
            print('Opção inválida! Tente de 1 a 4.')

    def tabuada():
        num = int(input('Deseja ver a tabuada de qual número? '))
        print(f'Tabuada do {num}:')
        for i in range(1, 11):
            print(f'{num} x {i} = {num * i}')

    def fibonacci():
        lis= []
        a=0
        b=1
        for i in range (10):
            f= a
            a= b
            b= f+b
            lis.append(a)
        print (lis)
        
        

    print ('=-'*16)

    if esc == '1':
        operaçoes_basicas()

    elif esc == '2':
        média()

    elif esc == '3':
        equação()

    elif esc == '4':
        fatorial()

    elif esc == '5':
        conversão_de_medidas()

    elif esc == '6':
        tabuada()

    elif esc == '7':
        fibonacci()