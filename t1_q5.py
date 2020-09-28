def pop_avaes(pop):
    parada = 0.1 * pop
    pop_total = pop
    ano = 1600

    while pop_total > parada:
        nasc = 0.01 * pop_total
        morte = 0.06 * pop_total
        pop_total = pop_total - morte + nasc

        print(f'{ano},{nasc:.0f},{morte:.0f},{pop_total:.0f}')

        ano += 1


def main():
    pop_i = int(input())

    resultado = pop_avaes(pop_i)

    return resultado

if __name__ == "__main__":
    main()