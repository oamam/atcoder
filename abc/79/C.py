def main():
    A, B, C, D = input()
    for ab in ['+', '-']:
        for bc in ['+', '-']:
            for cd in ['+', '-']:
                if eval(A + ab + B + bc + C + cd + D) == 7:
                    print(A + ab + B + bc + C + cd + D + '=7')
                    return


main()
