from random import randrange
from icecream import ic


def compute_new_num(number):
    digits = str(number)
    highdigits = list(reversed(sorted(digits)))
    lowdigits = list(sorted(digits))
    high_str = str.join('', highdigits)
    low_str = str.join('', lowdigits)
    high_num = int(high_str)
    low_num = int(low_str)
    # ic(high_num)
    # ic(low_num)
    new_num = high_num - low_num
    return new_num


def get_start_number(digits=4):
    # low =10**(digits - 1)
    high = 10**(digits)
    low = high / 10
    number = randrange(low, high)
    while True:
        if number % int('1' * digits) != 0:
            break
        number = randrange(low, high)
    return number


def main():

    maxtimes, maxval = 0, None
    for i in range(100):
        # number = i
        number = get_start_number(2)
        ic('start_number:',number)
        last = number
        for j in range(100):
            number = compute_new_num(number)
            if number == last: break
            last = number
            ic(number)
        else:
            print('fail on', number)
        if j > maxtimes:
            ic(j)
            maxtimes, maxval = j, i
    print('DONE', maxtimes, maxval)


if __name__ == '__main__':
    main()
