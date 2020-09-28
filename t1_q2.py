def meses(valor):
    poupanca = 10000
    m = 0

    while poupanca <= valor:
        taxa_carro = (0.4 / 100) * valor
        taxa_p = (0.7 / 100) * poupanca

        valor += taxa_carro
        poupanca += taxa_p
        m += 1

    return m

def main():
    preco  = float(input())

    resultado = meses(preco)

    print(resultado)
if __name__ == '__main__':
    main()
