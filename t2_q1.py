def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def main():
    n = int(input())

    resultado= fatorial(n)

    print(resultado)

if __name__ == "__main__":
    main()