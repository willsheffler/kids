from collections import defaultdict
import os, math, random
import matplotlib.pyplot as plt
import numpy as np
# from PyDictionary import PyDictionary
# dictionary = PyDictionary()


def readwords(name):
    with open(f'data/{name}.txt') as file:
        words = list()
        for word in file.readlines():
            words.append(word.strip())
        return words


# def word_)
# patt


def test_wordle_match():
    assert '*||  ' == compute_match('avast', 'aavaa')


def obscurity_score(word):
    score = 1.0
    for letter in word:
        # print(letter, letterfreq[letter])
        score *= letterfreq[letter]
    # return score
    return -math.log(score)


def sortdict(x):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}


def compute_match(secret, guess):
    used_letters = defaultdict(int)  # numer of letters already used
    available_letters = defaultdict(
        int)  # number of letters still available in secret
    for secert_letter in secret:
        available_letters[secert_letter] += 1
    # print(available_letters)
    # print(used_letters)
    # d = defaultdict(str)
    # d.update({'E':'MC2', 'JUDES': 'AWESOME', 'JONAH':'SUCKS'})
    # print(d['JONAH'])
    # print(d['E'])
    # print(d['JUDES'])
    # print(d['JUDAH'])

    matches = [' ', ' ', ' ', ' ', ' ']

    # GREEN MATCHES
    for index in range(len(secret)):
        secret_letter = secret[index]
        guess_letter = guess[index]
        # print(index, secret_letter, guess_letter)
        letters_match = (guess_letter == secret_letter)
        if letters_match:  # GREEN MATCH!!!!
            matches[index] = '*'
            available_letters[guess_letter] -= 1
            # print(index, guess_letter, available_letters)
            # used_letters[guess_letter] += 1

    # for i, m in enumerate(matches):
    # print(i, m)
    # print(secret)
    # print(''.join(matches))
    # print(guess)
    # print(available_letters)
    # print(used_letters)

    # YELLOW MATCHES
    for index in range(len(secret)):
        secret_letter = secret[index]
        guess_letter = guess[index]
        if secret_letter == guess_letter:
            continue
        if available_letters[guess_letter] > 0:  # YELLOW MATCH!!!!
            matches[index] = '|'
            available_letters[guess_letter] -= 1
            # print(index, guess_letter, available_letters)

    # print(secret)
    # print(''.join(matches))
    # print(guess)

    return ''.join(matches)


def wordle_round(officialwords, allwords):

    wordobscurity = dict()
    # for word in words:
    # wordobscurity[word] = obscurity_score(word)
    # wordobscurity = sortdict(wordobscurity)
    # top = list(wordobscurity.keys())

    # secret = random.choice(top[-10000:])
    secret = random.choice(officialwords)
    cantuse = set()
    mustuse = set()

    for iguess in range(1, 7):
        # secret = input(f'Enter secret {iguess}: ')

        while True:
            print('cantuse:', str.join('', sorted(cantuse)))
            print('mustuse:', str.join('', sorted(mustuse)))
            guess = input(f'Enter guess {iguess}: ')

            if guess == 'q':
                print(f'secret was {secret}, you quitter!')
                return
            valid = True
            if guess not in allwords:
                print('not valid word')
                valid = False
            for i in range(len(guess)):
                if guess[i] in cantuse:
                    valid = False
                    print('cant use letter', guess[i], 'at positin', i)
            for m in mustuse:
                if m not in guess:
                    valid = False
                    print('must use letter', m)
            if valid:
                break

        match = compute_match(secret, guess)
        for i in range(len(match)):
            # print(i, match[i], guess[i])
            if match[i] == '*':
                mustuse.add(guess[i])
            elif match[i] == '|':
                mustuse.add(guess[i])
            elif match[i] == ' ':
                if guess[i] not in mustuse:
                    cantuse.add(guess[i])
            else:
                assert 0

        print(match)
        print(guess)
        if match == '*****':
            print(f'YOU WIN IN {iguess}!!!')
            break
    else:
        print(f'you loose, the word was {secret}')


def main():
    print('press q to quit')
    test_wordle_match()
    allwords = readwords('wordle_dictionary')
    officialwords = readwords('wordle_dictionary_official_answers')

    while True:
        wordle_round(officialwords, allwords)

    return


def compute_word_obscurity():
    wordobscurity = dict()
    for word in words:
        wordobscurity[word] = obscurity_score(word)
    wordobscurity = sortdict(wordobscurity)
    top = list(wordobscurity.items())
    print('RARE:')
    for wf in top[:10]:
        print(wf[0], wf[1])
    print('COMMON:')
    for wf in top[-10:]:
        print(wf[0], wf[1])
    return top


lettercount = dict(
    a=4467,
    b=1162,
    c=1546,
    d=1399,
    e=4255,
    f=661,
    g=1102,
    h=1323,
    i=2581,
    j=163,
    k=882,
    l=2368,
    m=1301,
    n=2214,
    o=2801,
    p=1293,
    q=84,
    r=3043,
    s=2383,
    t=2381,
    u=1881,
    v=466,
    w=685,
    x=189,
    y=1605,
    z=250,
)

totcount = sum(lettercount.values())
letterfreq = {
    letter: count / totcount
    for letter, count in lettercount.items()
}

if __name__ == '__main__':
    main()
'''
        match = list()
        matches = ''
        seenit = defaultdict(int)
        available = defaultdict(int)
        for g in guess:
            available[g] += 1
        for w, g in zip(secret, guess):
            if w == g: available[g] -= 1

        for w, g in zip(secret, guess):
            match.append(w == g)
            seenit[g] += 1
            print(w, g, 'times in guess', seenit[g], 'num in secret',
                  secret.count(g))
            if w == g:
                matches += '*'
            # elif g in secret and seenit[g] <= secret.count(g):
            elif g in secret and seenit[g] <= available[g]:                
                matches += '|'
            else:
                matches += ' '

        print(matches)
        print(guess)

        if matches == '*****':
            break
'''

# 'green'  if letter matches at exact position
# 'yellow' if secret contains letter at different position
#          and not all occurances of that letter in secret
#          have been used
#
# secret ABCDE
# match  ||*||
# guess  EDCBA
#
# secret AARGH
# match  * |    # have enough A's for the 2nd 'yellow'
# guess  AVAST
#
# secret MAMMA
# match  | |    # not enough A's for the 2nd 'yellow'
# guess  AVAST
#
# secret AABBB
# match  * | x  # not enough A's for the 2nd 'yellow'
# guess  AHAVA
#
# BAD EXAMPLE
# secret ARSES
# match  *|||
# guess  AAAAA
