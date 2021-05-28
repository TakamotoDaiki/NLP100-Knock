import random
def shuffle(input_word):
    input_word_length = len(input_word)
    
    header = str(input_word[0])
    body = ''
    footer = str(input_word[input_word_length-1])

    body_num = list(range(1,input_word_length-1))
    random.shuffle(body_num)

    if input_word_length <= 4:
        return input_word
    else:
        for num_selector in range(0, input_word_length-2):
            body += input_word[body_num[num_selector]]

    shuffled_word = header + body + footer

    return shuffled_word

def make_typoglycemia(input_sentence):

    if input_sentence == '':
        typoglycemia = ''
        return typoglycemia

    word_split_list = input_sentence.split()
    typoglycemia = ''

    for word_selector in range(len(word_split_list)):
        word_split_list[word_selector] = shuffle(word_split_list[word_selector])

        typoglycemia += word_split_list[word_selector] + ' '

    return typoglycemia

def main():
    string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    output = make_typoglycemia(string)
    print(output)

if __name__ == '__main__':
    main()

