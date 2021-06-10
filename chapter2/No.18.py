import pandas as pd

def main():
    df = pd.read_table('popular-names.txt', header=None)
    print(df)
    
    df_s = df.sort_values([2], ascending=False)
    print(df_s)

if __name__ == '__main__':
    main()
