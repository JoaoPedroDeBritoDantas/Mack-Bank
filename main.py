import random

ncon = random.randint(1000, 9999)
sd_conta = 0
cred_limite = 0
extrato = []
countl = 0
nome = ""
senha_cadastrada = ""

while True:
    print("Seja bem-vindo ao Mack Bank")
    print("----------------")
    print("Cadastro (1)")
    print("Depósito (2)")
    print("Saque (3)")
    print("Saldo atual (4)")
    print("Extrato (5)")
    print("Finalizar (6)")
    print("----------------")

    op = int(input("Digite o número da opção que deseja: "))

    if op == 1:
        if countl > 0:
            input("Sua conta já foi cadastrada, aperte enter para voltar ao menu!")
            continue

        print("Seja bem-vindo ao cadastro:")
        print(f"O número de sua conta é {ncon}")
        nome = input("Digite seu nome: ")
        tel = input("Digite seu número com DDD: ")
        mail = input("Nos informe seu email: ")
        sd_inicial = float(input("Digite seu saldo inicial: "))
        cred_limite = float(input("Digite seu limite de crédito: "))
        
        while True:
            senha = input("Crie sua senha: ")
            resenha = input("Digite sua senha novamente: ")

            if senha == resenha:
                senha_cadastrada = senha
                break
            else:
                print("As senhas não coincidem, redigite.")

        sd_conta += sd_inicial
        countl += 1

    elif op in [2, 3, 4, 5]:
        if senha_cadastrada == "":
            print("Você precisa se cadastrar primeiro.")
            continue
        
        tentativas = 0
        while tentativas < 3:
            senha = input("Digite sua senha: ")
            if senha == senha_cadastrada:
                break
            else:
                tentativas += 1
                print(f"Senha incorreta, tente novamente ({3 - tentativas} tentativas restantes).")
        
        if senha != senha_cadastrada:
            print("Número máximo de tentativas excedido. Retornando ao menu.")
            continue

        if op == 2:
            print(f"Seja bem-vindo à opção de depósito {nome}")

            dep = float(input("Quanto deseja depositar: "))

            if dep <= 0:
                print("O valor do depósito deve ser maior do que 0")
            else:
                extrato.append(f"Depósito: R${dep:.2f}")
                sd_conta += dep
                print(f"Seu saldo pós-depósito é R${sd_conta:.2f}")

        elif op == 3:
            print(f"Seja bem-vindo à opção de saque {nome}")

            sq = float(input("Que valor deseja sacar? "))

            if sq <= 0:
                print("O valor do saque deve ser maior que zero")
            elif sq <= sd_conta:
                sd_conta -= sq
                extrato.append(f"Saque: R${sq:.2f}")
                print(f"O seu saldo após saque é R${sd_conta:.2f}")
            else:
                uso_cred = sq - sd_conta

                if uso_cred > cred_limite:
                    print("Não há crédito disponível suficiente para o saque.")
                else:
                    sd_conta = 0
                    cred_limite -= uso_cred
                    extrato.append(f"Saque: R${sq:.2f}")
                    extrato.append(f"Uso de crédito: R${uso_cred:.2f}")
                    print(f"O seu saldo após saque é R${sd_conta:.2f}")
                    print(f"O limite de crédito disponível após o saque é R${cred_limite:.2f}")

        elif op == 4:
            print(f"Seja bem-vindo ao seu saldo {nome}")
            print(f"O seu saldo atual é R${sd_conta:.2f}")
            print(f"O seu crédito atual é R${cred_limite:.2f}")

        elif op == 5:
            print(f"Bem-vindo ao extrato de sua conta {nome}")
            for item in extrato:
                print(item)

    elif op == 6:
        print("Obrigado por utilizar o nosso banco, até outro momento")
        break

    else:
        print("Opção inválida, retornando ao menu")