def soma(n):
    d = 1
    h = 0
    while d <= n:
        x = 1 / d
        h += x
        d += 1

    return h

def main():
    num = int(input())

    resultado = soma(num)

    print(resultado)

if __name__ == "__main__":
    main()