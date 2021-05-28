from ngram import n_gram

def main():
    string1 = 'paraparaparadise'
    string2 = 'paragraph'
    target = 'se'

    X = set(n_gram(string1, 2))
    Y = set(n_gram(string2, 2))

    print('X = {}'.format(X))
    print('Y = {}'.format(Y))

    union_set = X | Y
    intersection_set = X & Y
    difference_set = X - Y

    print('X | Y = {}'.format(union_set))
    print('X & Y = {}'.format(intersection_set))
    print('X - Y = {}'.format(difference_set))

    if target in X:
        print('{} exist in X'.format(target))
    else:
        print('{} not exist in Y'.format(target))
    if target in Y:
        print('{} exist in X'.format(target))
    else:
        print('{} not exist in Y'.format(target))

if __name__ == '__main__':
    main()
