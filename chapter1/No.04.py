def main():
    strings = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Mght Also Sign Peace Security Clause. Arthur King Can."
    dict = {}
    numbers = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    
    strings = strings.replace(',', '')
    strings = strings.replace('.', '')
    split_strings = strings.split()

    index = 1
    for string in zip(split_strings):
        if index in numbers:
            dict[str(index)] = string[0][0]
        else:
            dict[str(index)] = string[0][0:2]
            
        index += 1

    print(dict)

if __name__ == '__main__':
    main()
