import os


class Menu:
    def __init__(self, saldo, depositos, saques, limite_diario, quantidade_saques):
        self.saldo = saldo
        self.depositos = depositos
        self.saques = saques
        self.limite_diario = limite_diario
        self.quantidade_saques = quantidade_saques

    def exibir(self):
        while True:
            self.limpar_tela()
            print('-----------------MENU-----------------')
            print('1 - Depósito')
            print('2 - Saque')
            print('3 - Extrato')
            print('4 - Sair')
            print('--------------------------------------\n')
            selecao = input('Digite o número da opção desejada: ')

            if selecao == '1':
                self.limpar_tela()
                self.depositar()
                self.retornar_menu()
            elif selecao == '2':
                self.limpar_tela()
                self.sacar()
                self.retornar_menu()
            elif selecao == '3':
                self.limpar_tela()
                self.exibir_extrato()
                self.retornar_menu()
            elif selecao == '4':
                break
            else:
                print('Opção inválida.\nPor favor, digite uma das opções do menu.')
                self.retornar_menu()
            
        
    def retornar_menu(self):
        input('\n\nPressione Enter para continuar...')

    def limpar_tela(self):
         os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do console

    def depositar(self): 
        self.limpar_tela()      
        print('----------------------------------')
        print('            DEPÓSITO')
        print('----------------------------------\n')
        deposito = float(input('Insira o valor do depósito: R$ '))

        if deposito <= 0:
            print('Não é possível depositar valores negativos ou iguais a R$ 0.00')
        else:
            self.saldo += deposito
            self.depositos.append(deposito)
            print(f'\nOperação realizada com sucesso. \nSaldo Atual: R$ {self.saldo:.2f}')
       
    def sacar(self):
        self.limpar_tela()
        print('----------------------------------')
        print('            SAQUE')
        print('----------------------------------\n')
        saque = float(input('Insira o valor do saque: R$ '))

        if saque > self.saldo:
            print('Saldo insuficiente.')           
            return

        if saque > self.limite_diario:
            print('\nOperação inválida.\nVocê excedeu o limite máximo de R$ 500.00.')            
            return

        if self.quantidade_saques >= 3:
            print('\nOperação inválida.\nVocê excedeu a quantia de 3 saques diários.')            
            return

        self.saldo -= saque
        self.saques.append(saque)
        self.quantidade_saques += 1
        print(f'\nOperação realizada com sucesso.\nSaldo Atual: R$ {self.saldo:.2f}')
       
    def exibir_extrato(self):
        self.limpar_tela()
        print('----------------------------------')
        print('            EXTRATO')
        print('----------------------------------\n')
        
        if self.depositos:            
            for i, deposito in enumerate(self.depositos, start=1):
                print(f'Depósito {i}: R$ {deposito:.2f}')
            print('---------------------------')
        if self.saques:           
            for i, saque in enumerate(self.saques, start=1):
                print(f'Saque {i}: R$ {saque:.2f}')
            print('---------------------------')
        if not self.depositos and not self.saques:
            print('Nenhum registro de depósito ou saque.')

        print(f'\nSaldo Atual: R$ {self.saldo:.2f}')
       

saldo = 100.00
depositos = []
saques = []
limite_diario = 500.00
quantidade_saques = 0

menu = Menu(saldo, depositos, saques, limite_diario, quantidade_saques)
menu.exibir()