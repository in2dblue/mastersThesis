import csv
import pandas as pd

from nltk import word_tokenize


def levels(word):
    word = ''.join(word.split()).lower()
    try:
        df = all_levels.loc[all_levels['word'] == word]
        # level = df.iloc[0]['level']
        level = min(df['level'])
        if int(level) > 3:
            return 'C'
        else:
            return 'N'
    except:
        try:
            df = all_levels.loc[all_levels['word'] == word]
            level = df.iloc[0]['level']
            if int(level) > 3:
                return 'C'
            else:
                return 'N'
        except:
            return 'N'


all_levels = pd.read_table('cefr_levels.tsv', names=('word', 'level'))

df = pd.read_csv("data/INSCRIPT_TESTDATA.csv", usecols=["caption"])

with open('data/INSCRIPT_TESTDATA_final_token2.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for index, row in df.iterrows():
        # sentence = row['caption'].split()
        sentence = word_tokenize(row['caption'])
        i = 0
        for word in sentence:
            i += 1
            if word != '.' and word[-1] == '.':
                word = word[:-1]
                tsv_writer.writerow([word, levels(word)])
                tsv_writer.writerow(['.', 'N'])
                tsv_writer.writerow('')
            else:
                tsv_writer.writerow([word, levels(word)])

            if word == '.':
                tsv_writer.writerow('')
