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
            print(lista_de_cliente)

    return lista_de_cliente

def cadastro_numero_conta(lista_de_cliente):

    numeros_de_conta = set()        #set garante que os numeros sejam únicos

    while len(numeros_de_conta) < len(lista_de_cliente):
        numeros_de_conta.add(random.randint(100000, 999999))  

    return list(numeros_de_conta)

#def saldo_inicial():

#def credito_conta():

#def debito_conta():

#def saldo_conta():

#def grafico_conta():


def main():

    lista_de_cliente = cadastro_cliente()  # Armazenar o retorno de cadastro_cliente()
    numeros_de_conta = cadastro_numero_conta(lista_de_cliente)
    print(numeros_de_conta)



if __name__=="__main__":

    main()
