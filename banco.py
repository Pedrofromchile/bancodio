menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
# escolha = input() #d = deposito, 
print(menu)

saldo = 0
limite = 500
numero_saque = 0
extrato = ""
limite_saques = 3

while True:
    opcao = input("Operação desejada: ")
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Valor do saque: "))      
        excede_saldo = valor > saldo
        excede_limite = valor > limite
        excede_limite_saque = numero_saque >= limite_saques
        
        if excede_saldo:
            print("Operação Falhou, valor excede o saldo.")
        elif excede_limite:
            print("Operação Falhou, o valor ultrapassa o limite.")
        elif excede_limite_saque:
            print("Operação Falhou, você superou o limite de saques diários.")
        elif valor > 0:
            numero_saque += 1
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
    elif opcao == "q":
        break
    else:
        print("Operação Inválida, escolha um opção válida.")
            