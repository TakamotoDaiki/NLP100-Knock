import pandas as pd
import re

def main():
    
    df = pd.read_json('jawiki-country.json', lines=True)
    British = df[df['title'] == 'イギリス']['text'].values[0]

    template = re.findall(r'^\{\{基礎情報.*?$(.*?)^\}\}', British, re.MULTILINE + re.DOTALL)

    result = dict(re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', template[0], re.MULTILINE + re.DOTALL))
    for k, v in result.items():
        print(k + ': ' + v)
        
if __name__ == '__main__':
    main()
