import pandas as pd

def main():
    df = pd.read_table('popular-names.txt', header=None)
    row1 = df.iloc[:, 0]

    myset = set(row1)

    print(myset)

if __name__ == '__main__':
    main()
