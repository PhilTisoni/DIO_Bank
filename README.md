# Bootcamp Potência Tech - DIO Bank

<img style = "width: 200px" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdjqTkPkxvNF5yqLhPRNhYXnwXuW422OWMGMyn2KkNTjRyuqZriAq26YEAK35FIOgKAwY&usqp=CAU" alt = "DIO"> <img style = "width: 200px" src = "https://hermes.dio.me/files/assets/57ee4023-b3ef-4dd5-b403-c9107fda7723.png" alt = "Potência Tech powered by iFood | Ciência de Dados com Python Bootcamp"> <img style = "width: 200px" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSffOmWF-YkHmhQbndbPuETKRHMggsmDVaHstIRifhNi3JCi78WSv9ykImK6HDxXEIUJas&usqp=CAU" alt = "IFood">



## Sobre o projeto

Desenolvido em Julho de 2023 durante o bootcamp **Potência Tech powered by iFood | Ciência de Dados com Python!** oeferecido pela **DIO** em parceria com a **IFood**, o projeto apresenta uma aplicação console em Python que possibilita as ações de Depósito, Saque e Extrato de um cliente. Foram aplicados conceitos de orientação a objetos, seguindo as regras de negócio disponibilizadas durante o desafio.


## Como Clonar o Projeto

- Instale o Git no seu computador e durante a instalação, certifique-se se a opção Git Bash está adicionada.
- Após a instalação, crie uma pasta em sua área de trabalho
- Dentro da pasta, clique com o botão direito e selecione Git Bash Here
- Após abrir o terminal, copie o seguinte comando:
   
```bash
# clonar repositório
git clone https://github.com/PhilTisoni/DIO_Bank.git
```
Após clonar o projeto, abra o arquivo py em seu compilador de preferência.


# Índice

- <a href = "##Tecnologias-Utilizadas">Tecnologias Utilizadas</a>
- <a href = "##Regras-de-Negócio">Regras de Negócio</a>
- <a href = "##Autor">Autor</a>



## Tecnologias Utilizadas

- [Python 3.11.4](https://www.python.org/downloads/) 
- [Google Colab](https://colab.google/)
- [Visual Studio Code](https://code.visualstudio.com/download)

  
# Regras de Negócio

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

# Projeto

O código está divido em 4 partes: Menu, Funções do Sistema, Funções Bancárias e Exemplo. Procurou-se manter as boas práticas de programação para nomenclaturas, repetição de códigos e code smells. Também buscou-se a aplicação de princípios SOLID para a construção de um código limpo e de fácil manutenção.

## Menu

A lógica central do programa está na função Menu, ele exibe as opções propostas pelo desafio e procurou-se realizar algumas validações.

## Funções do Sistema

Essas duas funções são utilizadas no código todo, deste modo, otimizou-se a execução e evitou-se a repetição de código desnecessária:

```python
def retornar_menu(self):
        input('\n\nPressione Enter para continuar...')

    def limpar_tela(self):
         os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do console
```

A primeira função espera que o usuário aperte Enter para continuar, enquanto a segunda verifica através de uma condicional ternária qual é o sistema operacional utilizado pelo usuário, pois o comando de limpeza de tela no Windows e no Linux ou Mac são diferentes.


## Funções Bancárias

Todas as funções exibem um cabeçalho informando o seu tipo (Depósito, Saque ou Extrato) e realiza as devidas verificações seguindo a rera de negócio proposta no desafio. Para a função exibir_extrato(), ressalta-se a escolha de listas e da utilização de enumerate para facilitar a manipulação de dados no sistema:

```python
 if self.depositos:            
            for i, deposito in enumerate(self.depositos, start=1):
                print(f'Depósito {i}: R$ {deposito:.2f}')
            print('---------------------------')
```

Assim, ao invés de utilizar variáveis como foi proposto, optou-se por adicionar os dados em uma lista através do append() e ao exibir os dados do extrato, utilizou-se um for com dois contadores, assim, devido o enumerate guardar uma chave e valor, pode-se imprimir qual era o depósito e sua quantia:

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


# Autor

- [Phelipe Augusto Tisoni](https://www.linkedin.com/in/phelipetisoni "Phelipe Linkedin")
