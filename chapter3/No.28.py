import pandas as pd
import re

def remove_markup(text):
    text = re.sub(r'\'{2,5}', '', text)    
    text = re.sub(r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]', r'\1', text)
    text = re.sub(r'\[https?://[\w!?/\+\-_~=;\.,*&@#$%\(\)\'\[\]]+', '', text)
    text = re.sub(r'<.+?>', '', text)
    #text = re.sub(r'\{\{.+\}\}', '', text)
    text = re.sub(r'\{\{(?:lang|仮リンク)(?:[^|]*?\|)*?([^|]*?)\}}', r'\1', text)
    

    return text

def main():
    
    df = pd.read_json('jawiki-country.json', lines=True)
    British = df[df['title'] == 'イギリス']['text'].values[0]

    template = re.findall(r'^\{\{基礎情報.*?$(.*?)^\}\}', British, re.MULTILINE + re.DOTALL)

    result = dict(re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', template[0], re.MULTILINE + re.DOTALL))

    result_v2 = {}
    for k, v in result.items():
        result_v2[k] = remove_markup(v)
        
    for k, v in result_v2.items():
        print(k + ': ' + v)
        
        
if __name__ == '__main__':
    main()
