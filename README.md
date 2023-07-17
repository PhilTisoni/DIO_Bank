# Bootcamp Potência Tech - DIO Bank

<img style = "width: 200px" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdjqTkPkxvNF5yqLhPRNhYXnwXuW422OWMGMyn2KkNTjRyuqZriAq26YEAK35FIOgKAwY&usqp=CAU" alt = "DIO"> <img style = "width: 200px" src = "https://hermes.dio.me/files/assets/57ee4023-b3ef-4dd5-b403-c9107fda7723.png" alt = "Potência Tech powered by iFood | Ciência de Dados com Python Bootcamp"> <img style = "width: 200px" src = "https://logospng.org/download/ifood/logo-ifood-1024.png" alt = "IFood">


# Sobre o Projeto

Desenolvido em Julho de 2023 durante o bootcamp **Potência Tech Powered by iFood | Ciência de Dados com Python!** oeferecido pela **Digital Innovation One (DIO)** em parceria com a **IFood**, o projeto apresenta uma aplicação console de um banco, sendo realizado em duas versões: A primeira apresenta ações de Depósito, Saque e Extrato, enquanto a segunda, implementa as funções de Cadastro Usuários e Conta, além de Listar as contas do sistema. Foram aplicados conceitos de orientação a objetos, seguindo as regras de negócio disponibilizadas pelo desafio.

<details><summary>Versão 1</summary>

# Índice

- <a href = "#Regras-de-Negócio-v1">Regras de Negócio v1</a>
- <a href = "#Projeto-v1">Projeto v1</a>
- <a href = "##Implementações-para-a-Versão-2">Implementações para a Versão 2</a>

  
# Regras de Negócio v1

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a línguagem Python. Para a primeira versão do sistema, devemos implementar apenas 3 operações: depósito, saque e extrato. A primeira versão do projeto trabalha com apenas um usuário, dessa forma, não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 

## Depósito:

- Deve ser possível depositar valores positivos para a conta bancária.
- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

## Saque:

- O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500.00 por saque
- Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
 
## Extrato:

- Essa operação deve listar todos os depósitos e saques realizados na conta
- No fim da listagem, deve ser exibido o saldo atual da conta
- Os valores devem ser exibidos utilizando o formato R$ xxxx.xx, por exemplo: 1500.45 = R$ 1500.45


# Projeto v1

O código está divido em 4 partes: Menu, Funções do Sistema, Funções Bancárias e Exemplo. Procurou-se manter as boas práticas de programação e a aplicação de princípios [SOLID](https://www.dio.me/articles/mentoria-codigo-limpo-solid-e-boas-praticas) para a construção de um código limpo e de fácil manutenção.

## Menu

A lógica central do programa está na função **exibir()** da classe **Menu**, ele mostra as opções propostas pelo desafio e realiza algumas validações.

<img style = "width: 300px" src="./Assets/Menu.PNG" alt = "Menu">

## Funções do Sistema

Essas duas funções são responsáveis por otimizar a execução e evitar a repetição de códigos:

```python
def retornar_menu(self):
        input('\n\nPressione Enter para continuar...')

    def limpar_tela(self):
         os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do console
```

A função **retornar_menu()** espera que o usuário aperte **Enter** para continuar a próxima etapa do processo, deixando o programa mais interativo. A segunda função **limpar_tela()** verifica através de uma condicional ternária qual é o sistema operacional utilizado pelo usuário, pois o comando de limpeza do terminal é diferente em relação ao Windows, Linux ou Mac.


## Funções Bancárias

Todas as funções possuem um cabeçalho informando o seu tipo (Depósito, Saque ou Extrato) e realizam as devidas verificações seguindo a regra de negócio proposta no desafio. Pensando na manutenção do código a longo prazo, optou-se por substituir a utilização de variáveis por listas, deste modo, ao executar um depósito ou saque, os dados foram adicionados através do **append()** na sua respectiva lista. Abaixo, é possível visualizar um exemplo na função **depositar()**.

```python
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
```

A função **exibir_extrato()** utilizou **enumerates** para facilitar a impressão dos dados na tela:

```python
 if self.depositos:            
            for i, deposito in enumerate(self.depositos, start=1):
                print(f'Depósito {i}: R$ {deposito:.2f}')
            print('---------------------------')
```

Como se tratam de dados com chave e valor, adicionou-se um laço **for** com dois contadores, assim, é possível imprimir o número do depósito e a quantia adicionada na conta:

<img style = "width: 300px" src="./Assets/Extrato.PNG" alt = "Extrato - Exemplo de Formatação">


## Exemplo

Para exemplificar, ao final do código, foi inserido o valor de 100.00 para o saldo e preencheu-se as variáveis com as informações da regra de negócio, como o limite diário de R$ 500.00 e a quantidade de saques realizados.

```python
saldo = 100.00
depositos = []
saques = []
limite_diario = 500.00
quantidade_saques_realizados = 0

menu = Menu(saldo, depositos, saques, limite_diario, quantidade_saques)
menu.exibir()
```

# Implementações para a Versão 2

- [x] Separar o código em funções
- [x] Incluir implementações do Desafio 2 após a finalização das aulas

</details>



<details><summary>Versão 2</summary>

# Índice

- <a href = "#Regras-de-Negócio-v2">Regras de Negócio v2</a>
- <a href = "#Projeto-v2">Projeto v2</a>
- <a href = "##Implementações-para-a-Versão-3">Implementações para a Versão 3</a>

  
# Regras de Negócio v2

Afim de deixar o código mais modularizado, será necessário criar funções para todas as operações existentes (Sacar, Depoistar e Extrato), além de incluir duas novas funções: Cadastrar Usuário (cliente do banco) e Cadastrar Conta (vincular com o usuário). Cada função terá uma regra na passagem de argumento, o retorno e a forma de como serão chamadas poderá ser definida pelo desenvolvedor:

## Depósito:

- Deve ser possível depositar valores positivos para a conta bancária.
- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato
- **Receber argumentos apenas por posição (positional only)**

## Saque:

- O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500.00 por saque
- Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
- **Receber argumentos apenas por nome (keyword only)** 
 
## Extrato:

- Essa operação deve listar todos os depósitos e saques realizados na conta
- No fim da listagem, deve ser exibido o saldo atual da conta
- Os valores devem ser exibidos utilizando o formato R$ xxxx.xx, por exemplo: 1500.45 = R$ 1500.45
- **Receber argumentos por posição (positional only) e nome (keyword only). Argumentos posicionais: Saldo, argumentos nomeados: Extrato**

## Criar Usuário (cliente):

- Deve armazenar os usuários em uma lista
- Um usuário é comporto por: Nome, CPF, Data de Nascimento e Endereço
- O Endereço é uma string com o formato: Logradouro, número - Bairro - Cidade/Estado
- Devem ser armazenados somente números no CPF
- A Data de Nascimento é no formato: dd/mm/aaaa
- Não podemos cadastrar dois usuários com o mesmo CPF

## Criar Contas:

- Deve armazenar as contas em uma lista
- Uma conta é comporto por: Agência, Número da Conta e Usuário
- O Número da Conta é sequencial iniciando em 1
- O número da Agência é fixo: "0001"
- O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário


# Projeto v2

Houveram implementações e reestruturações no código da <a href = "#Projeto-v1">versão 1</a>. Procurou-se manter as boas práticas de programação e a aplicação de princípios [SOLID](https://www.dio.me/articles/mentoria-codigo-limpo-solid-e-boas-praticas) para a construção de um código limpo e de fácil manutenção.

## Menu

Foram inseridas as novas opções, havendo poucas modificações. A classe Menu foi substituida por uma função, deixando o código mais padronizado para essa versão:

```python
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

        if selecao == '1':
            limpar_tela()
            usuarios = cadastrar_usuario(usuarios)
            retornar_menu()
        elif selecao == '2':
            limpar_tela()
            contas = cadastrar_conta(contas, numero_conta, usuarios)
            numero_conta += 1
            retornar_menu()

      [...]       
```


## Funções Bancárias

Foram inseridas as alterações nos atributos seguindo a regra de negócio, mantendo suas tarefas anteriores operacionais.

```python
    def depositar(saldo, lista_depositos):
       limpar_tela()
       print('----------------------------------')
       print('            DEPÓSITO')
       print('----------------------------------\n')
       deposito = float(input('Insira o valor do depósito: R$ '))

      [...]
```

## Funções de Cadastro

Para evitar a repetição de código, foi criada uma função **procura_usuario()** que através de [list comprehensions](https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions) filtra o usuário através do CPF, dessa forma, evita-se duplicidade de dados e colabora com a manipulação das listas.

```python
def procura_usuario(cpf, usuarios):
    usuario_procurado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]  
    return usuario_procurado[0] if usuario_procurado else None
```

Após a filtragem e as devidas validações, as funções **cadastrar_usuario()** e **cadastrar_conta()** salvam os dados em suas respecticas listas, como exigido no desafio.

## Listar Contas

Como uma função bônus, foi criada a **listar_contas()** que exibe todas as contas cadastradas no sistema:

```python
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
```

# Próximos Passos

- [ ] Separar as funções em classes
- [ ] Organizar o Menu em Sub-Menus


</details>

# Tecnologias Utilizadas

- [Python 3.11.4](https://www.python.org/downloads/) 
- [Google Colab](https://colab.google/)
- [Visual Studio Code](https://code.visualstudio.com/download)

# Como Clonar o Projeto

- Instale o [Git](https://git-scm.com/downloads) no seu computador. Durante a instalação, certifique-se se a opção **Git Bash** está adicionada.
- Após a instalação, crie uma pasta em sua área de trabalho
- Dentro da pasta, clique com o botão direito e selecione **Git Bash Here**
- Após abrir o terminal, copie o seguinte comando:
   
```bash
git clone https://github.com/PhilTisoni/DIO_Bank.git
```
O projeto deverá ser clonado para a sua pasta. Abra o arquivo .py em seu compilador de preferência.


# Autor

- [Phelipe Augusto Tisoni](https://www.linkedin.com/in/phelipetisoni "Phelipe Linkedin")
