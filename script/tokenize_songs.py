import os
from janome.tokenizer import Tokenizer

STUDENT_DATA_DIR = "../data/tokenized"
RAW_DATA_DIR = "../data/raw"

tokenizer = Tokenizer()

for year in range(1968, 2025):
    raw_dir = f'{RAW_DATA_DIR}/{year}'

    files = os.listdir(raw_dir)
    for filename in files:
        rank, title, artist = filename.replace('__', '_').replace('IZ_ONE', 'IZONE').replace('Re_LIVE', 'ReLIVE').replace('_1_2', '_2分の1').strip('.txt').split('_')
        new_filename = f'{rank}_{artist}_{title}.tsv'

        filepath = f'{raw_dir}/{filename}'
        filepath_to = f'{STUDENT_DATA_DIR}/{year}/{new_filename}'

        with open(filepath) as f:
            lyrics = ''
            for line in f:
                lyrics += line.strip()

            tokens = tokenizer.tokenize(lyrics)

            os.makedirs(os.path.dirname(filepath_to), exist_ok=True)
            with open(filepath_to, 'w+') as ft:
                for token in tokens:
                    pos = token.part_of_speech.split(',')[0]
                    detail_pos = token.part_of_speech.split(',')[1]
                    base_form = token.base_form
                    term = token.surface

                    if ',' in term:
                        pos = '記号'

                    if term != '\n':
                        ft.write(f'{term}\t{base_form}\t{pos}\t{detail_pos}\n')
