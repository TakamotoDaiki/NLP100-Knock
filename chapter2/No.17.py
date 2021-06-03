import pandas as pd

def main():
    df = pd.read_table('popular-names.txt', header=None)
    myset = set()
    row1 = df.iloc[:, 0:1]

    for i in range(len(row1)):
        data = str(row1.iat[i, 0])
        myset.add(data)

    print(myset)

if __name__ == '__main__':
    main()
