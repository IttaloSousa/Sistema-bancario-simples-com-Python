
menu = """
================ Bem-vindo ao Italo Bank ===============

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Informe o valor do Deposito: "))
        print("Valor depositado com sucesso! Muito obrigado por ultilizar nossos serviços.")

        if valor > 0: 
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "2":  
        valor = float(input("Informe o valor do saque: "))

        execedeu_saldo = valor > saldo

        execedeu_limite = valor > limite

        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if execedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif execedeu_limite:
            print("Operação falhou! O valor do saque excede o limite diario de saque unico, seu limite são de 3 saques de R$ 500,00 por dia.")

        elif execedeu_saques:
            print("Operação falhou! Número máximo de saques diario excedido, tente novamente em 24 horas. Muito Obrigado!")


        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$: {valor:.2f}\n"
            numero_saques += 1
            print("Valor sacado com sucesso! Muito obrigado por ultilizar nossos serviços.")

        else:
            print("Operação falhou! O valor informado é inválido.")        
        

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$: {saldo:.2f}")
        print("==========================================")


    elif opcao == "0":  
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")      