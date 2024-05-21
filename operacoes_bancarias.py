from datetime import datetime #imporação da função de data e hora

def menu(): #Menu de Opções com o nome do Banco
    print('*' * 30)
    print('U.R. MONEY BANK MENU'.center(30, '*'))
    print('*' * 30)
    print('''*       [1] - Saque          *
*       [2] - Extrato        *
*       [3] - Depósitar      *
*       [4] - Encerrar       *''')
    print('*' * 30)    

saldo = saldo_anterior = 500
LIMITE_SAQUE = 500
numero_saque_diario = 3
extrato = list()
menu()

while True:        
    while True:
        operacao = input('Digite a opção desejada: ')
        if not operacao in ('1234567890'): # Verifica se as opções foram digitadas corretamente
            print(('Opção inválida').center(30,'*'))
            print(('Digite novamente!').center(30,'*'))
            menu()# chama a função do menu
        else:
            break

    print('*' * 30)

    match operacao: # Opções de Operações case 1 = Saque case 2 = Extrato case 3 = Depósito case 4 Encerrar
        case '1':
            print('Saque'.center(30))
            if numero_saque_diario > 0 : #Verifica se o limite de saque foi excedido ao tentar realizar saque
                while True:
                    saque = float(input('Digite o valor para o saque!\nR$ '))
                    if saque <= saldo:
                        if saque <= LIMITE_SAQUE:                                                    
                                print(f'Valor sacado R${saque:15.2f}')
                                saldo -= saque
                                data_hora = datetime.now() #variavel para receber a data e a hora
                                data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M') #variável para receber e formatar a data e hora
                                extrato.append(f'{data_hora_formatada} - R${saque:.2f}')
                                numero_saque_diario -= 1
                                break                        
                        else:
                            print(f'Operação negada.\nSeu limite por saque é\nR$ {LIMITE_SAQUE:.2f}\nLembrando de que você possui\n{numero_saque_diario} saque(s) diario restante(s).')
                            break
                    else:
                        print('Saldo insuficiente para saque!')                    
                        break
            else:
                print('Limite de saques diario esgotado!\nEntre em contato com a gerência\npara mais informações.')                
            menu()# chama a função do menu
        case '2':
            print('Extrato'.center(30))
            print(f'Saldo Anterior R${saldo_anterior:13.2f}')

            for cont in range(0, len(extrato)): # cont contador auxiliar para percorrer a lista do extrato
                print(f'{extrato[cont]}'.rjust(30))
            else:
                print(f'Saldo Atual R${saldo:16.2f}')
            
            menu()# chama a função do menu
        case '3':
            print('Depósitar'.center(30))
            while True:
                deposito = float(input('Digite o valor para depositar \nR$ '))

                if deposito <= 0 :
                    print('Valor para depósito inválido!')
                    cancelar = input('Deseja depositar outro valor?\n[S/N] ').lower().strip()
                    if cancelar in 'sn':
                        if cancelar == 'n':
                            break
                else:                    
                    saldo += deposito
                    data_hora = datetime.now()#variavel para receber a data e a hora
                    data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M')#variável para receber e formatar a data e hora
                    extrato.append(f'{data_hora_formatada} + R${deposito:.2f}')
                    break
            menu()# chama a função do menu
        case '4':
            print('Volte sempre!'.center(30))
            print(('*' * 13).center(30))
            break
        case _:
            print('Opção inválida!')
            menu()# chama a função do menu

