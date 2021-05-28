def n_gram(target, n):
    return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]

def main():
    target = "I am an NLPer"

    c_bigram = n_gram(target, 2)
    print(c_bigram)

    words = target.split(' ')
    w_bigram = n_gram(words, 2)
    print(w_bigram)

if __name__ == '__main__':
    main()
