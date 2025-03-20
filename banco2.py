import textwrap

def menu():
    menu = """\n
    ======= MENU =======
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("==== DEPÓSITO REALIZADO COM SUCESSO ====")
    else:
        print("\n@@@ Operação Falhou! O valor indicado é inválido.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        excede_saldo = valor > saldo
        excede_limite = valor > limite
        excede_saques = numero_saques > limite_saques

        if excede_saldo:
            print("Operação Falhou, valor excede o saldo.")
        elif excede_limite:
            print("Operação Falhou, o valor ultrapassa o limite.")
        elif excede_saques:
            print("Operação Falhou, você superou o limite de saques diários.")
        elif valor>0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            print("\n==== SAQUE REALIZADO COM SUCESSO ===")
        else:
            print("@@@ OPERAÇÂO FALHOU! VALOR INCORRETO. @@@")
        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF do Usuário (Somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("\n@@@ USUÁRIO JÁ EXISTE NA BASE DE DADOS")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-yyyy): ")
    endereco = input("Informe o endereço (lougradoro, nro - bairro - estado - cidade/UF): ")
    
    usuarios.append({ "cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco":endereco})
    
    print("=== USUARIO CRIADO CORRETAMENTE ===")
    
def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== CONTA CRIADA COM SUCESSO! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário não encontrado, fluxo de criação de contas encerrados! @@@")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    numero_saques = 0
    extrato = ""
    contas = []
    usuarios = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o Valor de saque: "))
            numero_saques += 1
            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato= extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
            
            
main()