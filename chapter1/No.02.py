def main():
    string1 = 'パトカー'
    string2 = 'タクシー'
    answer = ''

    for i in range(0, len(string1)):
        answer += f"{string1[i]}{string2[i]}"

    print(answer)

if __name__ == '__main__':
    main()
