import csv
import zipfile

import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    with zipfile.ZipFile('NewsAggregatorDataset.zip') as z:
        with z.open('newsCorpora.csv') as f:
            names = ('ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP')
            df = pd.read_table(f, names=names, quoting=csv.QUOTE_NONE)


    publisher_set = {"Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"}
    df = df[df['PUBLISHER'].isin(publisher_set)]
    df, valid_test_df = train_test_split(df, train_size=0.8, random_state=0)
    df.to_csv('train.txt', columns=('CATEGORY', 'TITLE'), sep='\t', header=False, index=False)
    valid_df, test_df = train_test_split(valid_test_df, test_size=0.5, random_state=0)
    valid_df.to_csv('valid.txt', columns=('CATEGORY', 'TITLE'), sep='\t', header=False, index=False)
    test_df.to_csv('test.txt', columns=('CATEGORY', 'TITLE'), sep='\t', header=False, index=False)

if __name__ == '__main__':
    main()
