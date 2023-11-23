menu = """
Escolha a sua operação:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Por favor, insira o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f} em xx/xx/xxxx às xx:xx:xx"
            print(f"O depósito no valor de R$ {valor:.2f} foi realizado. Confira o seu novo saldo!")
        
        else:
            print("Desculpe, não foi possível realizar a operação. O valor informado é inválido! Tente novamente!")

    elif opcao == "s":
        valor = float(input("Por favor, insira o valor que deseja sacar: "))

        if valor > saldo: #É o mais importante antes de liberar a operação. Primeira coisa a ser checada
            print("A operação não pôde ser realizada. O seu saldo é insuficiente. Por favor, verifique o seu saldo!")
        
        elif valor > limite: #Devemos conferir se o valor inserido ultrapassa o limite de saque imposto pela empresa.
            print("Desculpe, a operação não pôde ser realizada. O valor limite para saques (R$ 500,00) foi ultrapassado. Tente novamente!")
        
        elif numero_saques >= LIMITE_SAQUES: #Devemos conferir se o limite de saques não foi ultrapassado, antes de liberar a operação.
            print("Desculpe, a operação não pôde ser realizada. Você atingiu o limite diário de saques. Entre em contato com o seu gerente.")
        
        elif valor > 0: #Agora que já checamos as três condições acima, a operação pode ser realizada.
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f} em xx/xx/xxxx às xx:xx:xx"
            numero_saques += 1
            print(f"O saque no valor de R$ {valor:.2f} foi realizado. Retire o seu dinheiro na boca do caixa!")
        
        else: 
            print("Desculpe, a operação não pôde ser realizada. O valor informado é inválido! Tente novamente!")
    
    elif opcao == "e":
        print("================== EXTRATO ==================")
        print("Até o momento não foram realizadas operações." if not extrato else extrato)
        print(f"\nSaldo disponível: R$ {saldo:.2f}")
        print("\nExtrato realizado em xx/xx/xxxx às xx:xx:xx")
        print("\nObrigado por ser nosso cliente!")
        print("=============================================")
    
    elif opcao == "q": 
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação que desejar realizar.")