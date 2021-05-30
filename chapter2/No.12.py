import pandas as pd
def main():

    df = pd.read_table('popular-names.txt', encoding='utf-8', header=None)

    row1 = df.iloc[:, 0:1]
    row2 = df.iloc[:, 1:2]

    row1.to_csv('col1.txt', encoding='utf-8', sep='\t', header=None, index=False)
    row2.to_csv('col2.txt', encoding='utf-8', sep='\t', header=None, index=False)
        


if __name__ == '__main__':
    main()
                
