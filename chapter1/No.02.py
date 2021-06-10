def main():
    string1 = 'パトカー'
    string2 = 'タクシー'
    answer = ''

    for chara1, chara2 in zip(string1, string2):
        answer += f"{chara1}{chara2}"

    print(answer)

if __name__ == '__main__':
    main()
