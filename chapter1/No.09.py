import random
def shuffle(input_word):

    if len(input_word) <= 4:
        return input_word
    else:
        body = list(input_word[1:-1])
        random.shuffle(body)

    return input_word[0] + ''.join(body) + input_word[-1]

def make_typoglycemia(input_sentence):

    typoglycemia = ''
    if input_sentence == '':
        return typoglycemia

    word_split_list = input_sentence.split()

    for word in word_split_list:
        typoglycemia += shuffle(word) + ' '

    return typoglycemia

def main():
    string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    output = make_typoglycemia(string)
    print(output)

if __name__ == '__main__':
    main()
