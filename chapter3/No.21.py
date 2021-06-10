import pandas as pd

def main():
    
    df = pd.read_json('jawiki-country.json', lines=True)
    British = df[df['title'] == 'イギリス']['text'].values[0]

    category_lines = []
    for line in British.split('\n'):
        if '[[Category:' in line:
            category_lines.append(line)

    print(category_lines)

if __name__ == '__main__':
    main()
