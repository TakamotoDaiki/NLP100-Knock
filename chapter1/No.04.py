def main():
    strings = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Mght Also Sign Peace Security Clause. Arthur King Can."
    dict = {}
    numbers = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    
    strings = strings.replace(',', '')
    strings = strings.replace('.', '')
    split_strings = strings.split()

    for index, string in enumerate(split_strings, 1):
        if index in numbers:
            dict[index] = string[0]
        else:
            dict[index] = string[0:2]

    print(dict)

if __name__ == '__main__':
    main()
