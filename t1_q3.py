def tempo(populacao_a, populacao_b):
    pop_a = populacao_a
    pop_b = populacao_b
    t = 0

    while True:
        if pop_b > pop_a:
            break

        aumento_a = 0.02 * pop_a
        aumento_b = 0.03 * pop_b

        pop_a = pop_a + aumento_a
        pop_b = pop_b + aumento_b

        t += 1

    return t
def main():
    p_a = int(input())
    p_b = int(input())

    if p_b > p_a:
        i = p_a
        p_a = p_b
        p_b = i

    r = tempo (p_a, p_b)

    print(r)


if __name__ == "__main__":
    main()