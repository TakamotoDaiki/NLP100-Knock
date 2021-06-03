import sys

def count_lines(file_name):
    return sum([1 for _ in open(file_name)])

def save_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)

def main():
    if len(sys.argv) == 1:
        sys.argv += '5'
    N = int(sys.argv[1])

    with open('popular-names.txt', 'r') as f:
        lines = f.readlines()
        n_line = len(lines)
        if n_line % N != 0:
            flag = 1
            print('割り切れないため、余りの行を格納するファイルを追加します.')
        else:
            flag = 0
        sep_line = int(n_line / N)

        for i in range(N):
            sf = str('sep_file' + str(i+1) + '.txt')
            offset = i * sep_line
            text = lines[offset : offset + sep_line]
            save_file(sf, ''.join(text))

        if flag == 1:
            N += 1
            sf = str('sep_file' + str(N) + '.txt')
            text = lines[offset + sep_line : len(lines)]
            save_file(sf, ''.join(text))
            
        for i in range(N):
            sf = str('sep_file' + str(i+1) + '.txt')
            n = count_lines(sf)
            print('{0}:{1}行'.format(sf, n))

if __name__ == '__main__':
    main()
