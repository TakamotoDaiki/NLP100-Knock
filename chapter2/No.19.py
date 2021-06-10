import pandas as pd

def main():
    df = pd.read_table('popular-names.txt', header=None)
    row1 = df.iloc[:, 0]

    ans = row1.value_counts()
    print(ans)

if __name__ == '__main__':
    main()
