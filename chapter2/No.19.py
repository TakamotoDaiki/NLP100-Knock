import pandas as pd

def main():
    df = pd.read_table('popular-names.txt', header=None)
    row1 = df.iloc[:, 0]
    myset = set(row1)
    mylist = list(myset)
    
    df2 = pd.DataFrame(data=mylist)
    df2[1] = 0

    for i in range(len(row1)):
        data = str(row1[i])
        for j in range(len(df2)):
            if str(df2.iat[j, 0]) == data:
                df2.iat[j, 1] += 1

    ans = df2.sort_values([1], ascending=False)
    print(ans)

if __name__ == '__main__':
    main()
