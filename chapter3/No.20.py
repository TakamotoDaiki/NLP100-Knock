import pandas as pd

def main():
    
    df = pd.read_json('jawiki-country.json', lines=True)
    British = df[df['title'] == 'イギリス']['text'].values[0]
    print(British)

if __name__ == '__main__':
    main()
