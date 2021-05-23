import re
def main():
    strings = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    answer = ''

    strings = re.sub(',', '', strings)
    strings = strings.replace('.', '')
    split_string = strings.split()
    for string in zip(split_string):
        answer += str(len(string[0]))

    print(answer)

if __name__ == '__main__':
    main()
