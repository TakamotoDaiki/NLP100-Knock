import pandas as pd
import re

def main():
    
    df = pd.read_json('jawiki-country.json', lines=True)
    British = df[df['title'] == 'イギリス']['text'].values[0]

    for section in re.findall(r'(=+)([^=]+)\1\n', British):
        print('{}\t{}'.format(section[1].strip(), len(section[0])-1))

if __name__ == '__main__':
    main()
