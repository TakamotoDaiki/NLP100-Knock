import sys
import pandas as pd

def main():
    df = pd.read_table('popular-names.txt', header=None)

    if len(sys.argv) == 1:
        sys.argv += '3'
    output = df.head(int(sys.argv[1]))
    print(output)

if __name__ == '__main__':
    main()
