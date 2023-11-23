import json
import pandas
import hashlib
import argparse
from tqdm import tqdm
from kazakh_convert_cyrl_to_arab import translate


# read from original data
def read_data(data_dir):
    # read from parquet file
    df = pandas.read_parquet(data_dir)
    json_line = df.to_json(orient='records', lines=True, force_ascii=False)
    json_line = json_line.split('\n')

    # output to json with 3 keys: title, text, url
    json_data = []
    for line in tqdm(json_line):
        try:
            data = json.loads(line)
            json_data.append({'title': data['title'] if 'title' in data else '', 'text': data['text'], 'url': data['url']})
        except: # skip empty line
            continue
    return json_data

# extract kk data and save to jsonl
def extract_and_save_data(data, data_dir, sha256_dir, language):
    sha256 = []
    with open(sha256_dir, 'r') as f:
        sha256 = json.loads(f.read())
    if language == 'kk':
        # extract kazakh data from culturax data
        sha256 = sha256['kk_to_select']
        data = filter(lambda d: hashlib.sha256(d['url'].encode("utf-8")).hexdigest() in sha256, data)
    elif language == 'ug':
        # extract uyghur data from culturax data
        sha256 = sha256['ug_to_remove'] + sha256['kk_to_select']
        data = filter(lambda d: hashlib.sha256(d['url'].encode("utf-8")).hexdigest() not in sha256, data)
    
    with open(data_dir.replace(".parquet", ".jsonl"), 'w') as f:
        for d in data:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='path/to/culturax/parquet/file')
    parser.add_argument('--sha256_dir', type=str, default='path/to/sha256/file')
    parser.add_argument('--language', type=str) # 'kk' or 'bo' or 'ug'
    args = parser.parse_args()

    data = read_data(args.data_dir)
    # print(len(data))
    extract_and_save_data(data, args.data_dir, args.sha256_dir, args.language)