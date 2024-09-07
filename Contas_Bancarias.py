import matplotlib.pyplot as plt 
import random

def cadastro_cliente():

    lista_de_cliente = []

    while True:

        nome_do_cliente = input("Digito o primeiro nome do cliente ou 0 para sair:")

        if nome_do_cliente == "0":
            print (lista_de_cliente)
            break

        else:
            lista_de_cliente.append(nome_do_cliente)

    return lista_de_cliente

def cadastro_numero_conta(lista_de_cliente):

    numeros_de_conta = set()        #set garante que os numeros sejam únicos

    while len(numeros_de_conta) < len(lista_de_cliente):
        numeros_de_conta.add(random.randint(100000, 999999))  

    return list(numeros_de_conta)

def saldo_inicial_da_conta(lista_de_cliente):

    saldo_inicial = []

    while len(saldo_inicial) < len(lista_de_cliente):
        primeiro_saldo = float(input("Digite o saldo da conta:"))
        saldo_inicial.append(primeiro_saldo)

    return list(saldo_inicial)

def movimentacao_conta(numeros_de_conta, lista_de_cliente, saldo_inicial):

    codigo_conta = int(input("Digite o código da conta: "))
    if codigo_conta not in numeros_de_conta:
        print("Código de conta inválido.")
        return

    indice = numeros_de_conta.index(codigo_conta)
    nome_cliente = lista_de_cliente[indice]
    saldo_atual = saldo_inicial[indice]

    operacao = input("Digite 'C' para crédito ou 'D' para débito: ").upper()
    if operacao not in ("C", "D"):
        print("Operação inválida.")
        return

    valor = float(input("Digite o valor da operação: "))
    if operacao == "D" and valor > saldo_atual:
        print("Saldo insuficiente.")
        return

    if operacao == "C":
        saldo_inicial[indice] += valor
    else:
        saldo_inicial[indice] -= valor

    print(f"Operação realizada com sucesso para {nome_cliente}. Novo saldo: {saldo_inicial[indice]}")

    while True:
        movimentacao_conta(numeros_de_conta, lista_de_cliente, saldo_inicial)

        continuar = input("Deseja realizar outra operação? (S/N): ").upper()
        if continuar != "S":
            break

#def grafico_conta():


def main():

    lista_de_cliente = cadastro_cliente()  # Armazenar o retorno de cadastro_cliente()
    numeros_de_conta = cadastro_numero_conta(lista_de_cliente)
    saldo_inicial = saldo_inicial_da_conta(lista_de_cliente)
    print(lista_de_cliente)
    print(numeros_de_conta)
    print(saldo_inicial)

    movimentacao_conta(numeros_de_conta, lista_de_cliente, saldo_inicial)


if __name__=="__main__":

    main()
