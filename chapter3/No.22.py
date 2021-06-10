import pandas as pd
import re

def main():
    
    df = pd.read_json('jawiki-country.json', lines=True)
    British = df[df['title'] == 'イギリス']['text'].values[0]

    categories = []
    for t in re.findall(r'\[\[Category:(.*?)(\|.*?)?\]\]', British):
        categories.append(t[0])

    print(categories)

if __name__ == '__main__':
    main()
