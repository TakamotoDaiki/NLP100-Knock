import pandas as pd
import re

def main():
    
    df = pd.read_json('jawiki-country.json', lines=True)
    British = df[df['title'] == 'イギリス']['text'].values[0]

    for file in re.findall(r'\[\[(File|ファイル):([^]|]+?)(\|.*?)+\]\]' ,British):
        print(file[1])

if __name__ == '__main__':
    main()
