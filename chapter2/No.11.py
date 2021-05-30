import re
def main():
    
    with open('popular-names.txt', 'r') as f:
        with open('answer-11.txt', 'w') as sf:
            for line in f:
                line = re.sub('\t', ' ', line)
                sf.write(line)


if __name__ == '__main__':
    main()
        
