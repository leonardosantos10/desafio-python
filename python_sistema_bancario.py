import textwrap

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("\n@@@ Erro: Valor de depósito inválido! @@@")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    print("\n=== Depósito realizado com sucesso! ===")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    falha_saldo = valor > saldo
    falha_limite = valor > limite
    falha_saques = numero_saques >= limite_saques

    if falha_saldo:
        print("\n@@@ Erro: Saldo insuficiente! @@@")
    elif falha_limite:
        print("\n@@@ Erro: O valor excede o limite por saque! @@@")
    elif falha_saques:
        print("\n@@@ Erro: Limite diário de saques atingido! @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Erro: Valor informado é inválido! @@@")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    cabecalho = " EXTRATO ".center(40, "=")
    rodape = "".center(40, "=")
    print(f"\n{cabecalho}")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo Atual:\tR$ {saldo:.2f}")
    print(rodape)


def filtrar_usuario(cpf, usuarios):
    busca = [u for u in usuarios if u["cpf"] == cpf]
    return busca[0] if busca else None

def criar_usuario(usuarios):
    cpf = input("CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Erro: CPF já cadastrado! @@@")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (Logradouro, nº - Bairro - Cidade/UF): ")

    usuarios.append({
        "nome": nome, 
        "data_nascimento": nascimento, 
        "cpf": cpf, 
        "endereco": endereco
    })
    print("\n=== Usuário cadastrado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do titular: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Erro: Usuário não encontrado! Cadastre o usuário primeiro. @@@")
        return None

    print("\n=== Conta criada com sucesso! ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada no sistema. @@@")
        return
        
    for conta in contas:
        info = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 40)
        print(textwrap.dedent(info))


def main():

    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500

    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        menu = """
        [d]  Depositar
        [s]  Sacar
        [e]  Extrato
        [nu] Novo Usuário
        [nc] Nova Conta
        [lc] Listar Contas
        [q]  Sair
        => """
        
        opcao = input(textwrap.dedent(menu)).lower()

        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_VALOR_SAQUE,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema!")
            break

if __name__ == "__main__":
    main()