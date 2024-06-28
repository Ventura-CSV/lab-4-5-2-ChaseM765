import random


def main():
    total = 0
    numbers = []
    while True:
        ran = random.randint(0,100)
        numbers.append(ran)
        if total + ran > 100:
            break
        else:
            total += ran



    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
