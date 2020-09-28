def n_primo(n):
    cont = 0
    for c in range(1, n + 1):
        if n % c == 0:
            cont += 1

    if cont == 2:
        return True
    else:
        return False

def main():
    x = int(input())
    y = int(input())

    for num in range(x, y + 1):
        if n_primo(num) == True:
            print(num)

if __name__ == "__main__":
    main()