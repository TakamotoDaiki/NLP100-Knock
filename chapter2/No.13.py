import pandas as pd

def main():
    df1 = pd.read_table('col1.txt', header=None)
    df2 = pd.read_table('col2.txt', header=None)
 
    sd = pd.concat([df1, df2], axis = 1)
    sd.to_csv('col1+2.txt', header=None, index=None, sep='\t')

if __name__ == '__main__':
    main()
