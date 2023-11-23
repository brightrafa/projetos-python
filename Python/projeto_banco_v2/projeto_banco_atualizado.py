import textwrap

def menu():
    menu = """\n
==================== MENU ====================
    
Escolha a sua operação:

[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[u]\tNovo usuário
[c]\tNova conta
[l]\tListar contas
[q]\tSair   
=> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"\nDepósito:\tR$ {valor:.2f} em xx/xx/xxxx às xx:xx:xx\n"
            print(f"\nO depósito no valor de R$ {valor:.2f} foi realizado. Confira o seu novo saldo!")
        
    else:
        print("\nDesculpe, não foi possível realizar a operação. O valor informado é inválido! Tente novamente!")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
     

    if valor > saldo: #É o mais importante antes de liberar a operação. Primeira coisa a ser checada
        print("\nA operação não pôde ser realizada. O seu saldo é insuficiente. Por favor, verifique o seu saldo!")
        
    elif valor > limite: #Devemos conferir se o valor inserido ultrapassa o limite de saque imposto pela empresa.
        print("\nDesculpe, a operação não pôde ser realizada. O valor limite para saques (R$ 500,00) foi ultrapassado. Tente novamente!")
        
    elif numero_saques >= limite_saques: #Devemos conferir se o limite de saques não foi ultrapassado, antes de liberar a operação.
        print("\nDesculpe, a operação não pôde ser realizada. Você atingiu o limite diário de saques. Entre em contato com o seu gerente.")
        
    elif valor > 0: #Agora que já checamos as três condições acima, a operação pode ser realizada.
        saldo -= valor
        extrato += f"\nSaque:\t\tR$ {valor:.2f} em xx/xx/xxxx às xx:xx:xx\n"
        numero_saques += 1
        print(f"\nO saque no valor de R$ {valor:.2f} foi realizado. Retire o seu dinheiro na boca do caixa!")
        
    else: 
        print("\nDesculpe, a operação não pôde ser realizada. O valor informado é inválido! Tente novamente!")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("================== EXTRATO ==================")
    print("Até o momento não foram realizadas operações." if not extrato else extrato)
    print(f"\nSaldo disponível: R$ {saldo:.2f}")
    print("\nExtrato realizado em xx/xx/xxxx às xx:xx:xx")
    print("\nObrigado por ser nosso cliente!")
    print("=============================================")

def criar_usuario(usuarios):
    cpf = input("Digite o número do seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário cadastrado com esse CPF!")
        return

    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento. Exemplo: 09/10/1995: ")
    endereco = input("Informe o seu endereço(logradouro, número - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("===== O usuário foi cadastrado com sucesso! =====")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o número do seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n===== A sua conta foi criada com sucesso! =====")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nO usuário não foi encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t\t{conta['agencia']}
            Conta Corrente:\t\t{conta['numero_conta']}
            Titular da conta:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))
        
def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
   
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Por favor, insira o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        

        elif opcao == "s":
            valor = float(input("Por favor, insira o valor que deseja sacar: "))

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
    
        elif opcao == "u":
            criar_usuario(usuarios)
    
        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break
    
        else:
            print("Operação inválida. Por favor, selecione novamente a operação que desejar realizar.")

main()