def numero(data):
    soma = 0
    for d in range(8):
        d = data // (10 ** d) % 10
        soma += d
    return soma

def main():
    numeros = int(input())

    resultado = numero(numeros)

    print(resultado)
if __name__ == '__main__':
    main()