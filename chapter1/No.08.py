def cipher(target):
    output = ''
    
    for c in target:
        if c.isalpha() == True:
            if c.islower() == True:
                c = chr(219-ord(c))
                
        output += c

    return output

def main():
    string = 'No.08.py'
    print(string)
    
    output = cipher(string)
    print(output)

    output2 = cipher(output)
    print(output2)

if __name__ == '__main__':
    main()
