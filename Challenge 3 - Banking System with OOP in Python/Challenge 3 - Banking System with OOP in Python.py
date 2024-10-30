#importando a biblioteca para facilitar o processamento de strings
import textwrap


#Estruturando o sistema em classes e seus métodos
class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.agencia = "0001"
    
    def criar_usuario(self, nome, cpf, data_nascimento, endereco):
        if not self.filtrar_usuario(cpf):
            novo_usuario = Usuario(nome, cpf, data_nascimento, endereco)
            self.usuarios.append(novo_usuario)
            print("\nUsuário criado com sucesso.")
        else:
            print("\nO CPF informado já existe.")

    def criar_conta(self, cpf):
        usuario = self.filtrar_usuario(cpf)
        if usuario:
            nova_conta = Conta(self.agencia, len(self.contas) + 1, usuario)
            self.contas.append(nova_conta)
            print("\nConta criada com sucesso.")
        else:
            print("Usuário não encontrado. Operação encerrada.")

    def filtrar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def listar_contas(self):
        for conta in self.contas:
            print(conta)

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
class Conta:
    LIMITE_SAQUES = 3

    def __init__(self, agencia, numero, usuario):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso.")
        else:
            print("\nOperação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Você não tem saldo suficiente.")
        elif valor > self.limite:
            print("O valor do saque excede o limite.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

    def __str__(self):
        return f"Agência: {self.agencia}, Conta: {self.numero}, Titular: {self.usuario.nome}"
class Menu:
    def __init__(self, banco):
        self.banco = banco

    def exibir_menu(self):
        while True:
            opcao = input(textwrap.dedent("""\n
            ================ MENU ================
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [nc] Nova Conta
            [lc] Listar Contas
            [nu] Novo Usuário
            [q] Sair
            => """))

            if opcao == "d":
                self.realizar_deposito()
            elif opcao == "s":
                self.realizar_saque()
            elif opcao == "e":
                self.exibir_extrato()
            elif opcao == "nc":
                self.criar_nova_conta()
            elif opcao == "lc":
                self.listar_contas()
            elif opcao == "nu":
                self.criar_novo_usuario()
            elif opcao == "q":
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

    def realizar_deposito(self):
        numero_conta = int(input("Informe o número da conta: "))
        conta = self.buscar_conta(numero_conta)
        if conta:
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
    
    def realizar_saque(self):
        numero_conta = int(input("Informe o número da conta: "))
        conta = self.buscar_conta(numero_conta)
        if conta:
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)

    def exibir_extrato(self):
        numero_conta = int(input("Informe o número da conta: "))
        conta = self.buscar_conta(numero_conta)
        if conta:
            conta.exibir_extrato()

    def criar_novo_usuario(self):
        nome = input("Informe seu nome completo: ")
        cpf = input("Informe o CPF (apenas números): ")
        data_nascimento = input("Informe sua data de nascimento (ex. 01-01-2000): ")
        endereco = input("Informe seu endereço (R. Brasil, 77 - Centro - São Paulo/SP): ")
        self.banco.criar_usuario(nome, cpf, data_nascimento, endereco)

    def criar_nova_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        self.banco.criar_conta(cpf)

    def listar_contas(self):
        self.banco.listar_contas()

    def buscar_conta(self, numero_conta):
        for conta in self.banco.contas:
            if conta.numero == numero_conta:
                return conta
        print("Conta não encontrada.")
        return None
if __name__ == "__main__":
    banco = Banco()
    menu = Menu(banco)
    menu.exibir_menu()
