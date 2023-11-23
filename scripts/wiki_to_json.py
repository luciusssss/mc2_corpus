import json
import pandas
from tqdm import tqdm
import argparse
from kazakh_convert_cyrl_to_arab import translate

# read from original data, change writing systems for kazakh, and save to jsonl
def read_and_save_data(data_dir, language):
    # read from parquet file
    df = pandas.read_parquet(data_dir)

    # for kazakh, convert cyrillic to arabic and output to jsonl
    if language == 'kk':
        json_line = df.to_json(orient='records', lines=True, force_ascii=False)
        json_line = json_line.split('\n')
        json_data = []
        for line in tqdm(json_line):
            try:
                data = json.loads(line)
                json_data.append({'title': translate(data['title'], 'kk-arab'), 'text': translate(data['text'], 'kk-arab'), 'url': data['url']})
            except: # skip empty line
                continue
        with open(data_dir.replace(".parquet", ".jsonl"), 'w') as f:
            for data in json_data:
                f.write(json.dumps(data, ensure_ascii=False) + '\n')

    else:
        # output to json with 3 keys: title, text, url
        df = df[['title', 'text', 'url']]
        df.to_json(data_dir.replace(".parquet", ".jsonl"), orient='records', lines=True, index=False, force_ascii=False)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='path/to/wikipedia/parquet/file')
    parser.add_argument('--language', type=str) # 'kk' or 'bo' or 'ug'
    args = parser.parse_args()

    read_and_save_data(args.data_dir, args.language)