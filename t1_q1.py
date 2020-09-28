def metros_minutos(n):
    t = n
    l = 0
    minutos = 0

    if n == 0:
        minutos = 0
    else:
        while l < t:
            l += 10
            t += 1
            minutos += 1
    return minutos
def main():
    distancia = int(input())

    resultado = metros_minutos(distancia)

    print(resultado)

if __name__ == "__main__":
    main()
