import os


def exibir_menu(saldo, depositos, saques, saques_realizados, usuarios, contas, numero_conta):
    while True:
        limpar_tela()
        print('-----------------MENU-----------------')
        print('1 - Cadastrar Usuário')
        print('2 - Cadastrar Conta')
        print('3 - Listar Contas')
        print('4 - Depósito')
        print('5 - Saque')
        print('6 - Extrato')
        print('7 - Sair')
        print('--------------------------------------\n')
        selecao = input('Digite o número da opção desejada: ')

    def __init__(self, saldo, depositos, saques, limite_diario, quantidade_saques_realizados):
        self.saldo = saldo
        self.depositos = depositos
        self.saques = saques
        self.limite_diario = limite_diario
        self.quantidade_saques_realizados = quantidade_saques_realizados

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

        
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do console


def depositar(saldo, lista_depositos):
    limpar_tela()
    print('----------------------------------')
    print('            DEPÓSITO')
    print('----------------------------------\n')
    deposito = float(input('Insira o valor do depósito: R$ '))

    if deposito <= 0:
        print('Não é possível depositar valores negativos ou iguais a R$ 0.00')
    else:
        saldo += deposito
        lista_depositos.append(deposito)
        print(f'\nOperação realizada com sucesso. \nSaldo Atual: R$ {saldo:.2f}')
    return saldo, lista_depositos


def sacar(*, saldo, lista_saques, LIMITE_SAQUE, quantidade_saques_realizados):
    limpar_tela()
    print('----------------------------------')
    print('            SAQUE')
    print('----------------------------------\n')
    saque = float(input('Insira o valor do saque: R$ '))

    if saque > saldo:
        print('Saldo insuficiente.')
        return saldo, lista_saques, quantidade_saques_realizados

    if saque > LIMITE_SAQUE:
        print('\nOperação inválida.\nVocê excedeu o limite máximo de R$ 500.00.')
        return saldo, lista_saques, quantidade_saques_realizados

    if quantidade_saques_realizados >= 3:
        print('\nOperação inválida.\nVocê excedeu a quantia de 3 saques diários.')
        return saldo, lista_saques, quantidade_saques_realizados

    saldo -= saque
    lista_saques.append(saque)
    quantidade_saques_realizados += 1
    print(f'\nOperação realizada com sucesso.\nSaldo Atual: R$ {saldo:.2f}')

    return saldo, lista_saques, quantidade_saques_realizados


def exibir_extrato(saldo, lista_depositos, lista_saques):
    limpar_tela()
    print('----------------------------------')
    print('            EXTRATO')
    print('----------------------------------\n')

    if lista_depositos:
        for i, deposito in enumerate(lista_depositos, start=1):
            print(f'Depósito {i}: R$ {deposito:.2f}')
        print('---------------------------')
    if lista_saques:
        for i, saque in enumerate(lista_saques, start=1):
            print(f'Saque {i}: R$ {saque:.2f}')
        print('---------------------------')
    if not lista_depositos and not lista_saques:
        print('Nenhum registro de depósito ou saque.')

    print(f'\nSaldo Atual: R$ {saldo:.2f}')


def cadastrar_usuario(usuarios):
    limpar_tela()
    print('----------------------------------')
    print('            CADASTRAR USUÁRIO')
    print('----------------------------------\n')
    cpf = input('Insira o CPF (utilize apenas números): ')
    usuario = procura_usuario(cpf, usuarios)

    if usuario:
        print('Esse usuário já foi cadastrado.')
        return

    nome = input('Insira o Nome Completo: ')
    data_nascimento = input('Insira a Data de Nascimento (dd/mm/aaaa): ')
    endereco = input('Insira o Endereço (Logradouro, Número - Bairro - Cidade / Estado): ')

    usuario = {'nome': nome, 'cpf': cpf, 'data_nascimento': data_nascimento, 'endereco': endereco}
    usuarios.append(usuario)      
    print('Usuário Cadastrado com Sucesso.')           
    return usuarios

def procura_usuario(cpf, usuarios):
    usuario_procurado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]  
    return usuario_procurado[0] if usuario_procurado else None


def cadastrar_conta(contas, numero_conta, usuarios):
    limpar_tela()
    print('----------------------------------')
    print('            CADASTRAR CONTA')
    print('----------------------------------\n')
    cpf = input('Insira o CPF do titular da conta (utilize apenas números): ')  
    usuario = procura_usuario(cpf, usuarios) 

    if usuario:
        numero_conta += 1
        contas.append({'usuario': usuario['nome'], 'AGENCIA': '0001', 
                    'numero_conta': numero_conta})
        print('Conta Cadastrada com Sucesso.')    
        return contas   
        
    print('Esse usuário ainda não foi cadastrado. Por favor, insira os dados no sistema')    
    return contas


def listar_contas(contas):
    limpar_tela()
    print('----------------------------------')
    print('            LISTAR CONTAS')
    print('----------------------------------\n')

    if not contas:
        print('Nenhuma conta cadastrada.')
    else:
        for i, conta in enumerate(contas, start=1):
            cliente = conta['usuario']
            numero_conta = conta['numero_conta']
            agencia = conta['AGENCIA']

            print(f'Cliente: {cliente}')
            print(f'Conta: {i}')
            print(f'Agência: {agencia}')
            print('----------------------------------\n')


saldo = 100.00
depositos = []
saques = []
saques_realizados = 0

usuarios = []
contas = []
numero_conta = 0

exibir_menu(saldo, depositos, saques, saques_realizados, usuarios, contas, numero_conta)