#importando a biblioteca para facilitar o processamento de strings
import textwrap

#Criando o menu da aplicação
def menu():
    menu = """\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso.")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nO CPF informado já existe.")
        return

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (ex. 01-01-1000): ")
    endereco = input("Informe seu endereço (R. Brasil, 77 - Centro - São Paulo/SP): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\nUsuário criado com sucesso.")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado. Operação encerrada.")

def listar_contas(contas):
    if contas:
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")
    else:
        print("Nenhuma conta encontrada.")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
