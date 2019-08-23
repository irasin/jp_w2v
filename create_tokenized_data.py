import os
import re
import glob
import random
import unicodedata
import MeCab


# テキスト読み込むのイテレータ
class Readtext:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        try:
            with open(self.path, encoding='utf-8') as f:
                for line in f:
                    yield line
        except:
            raise

# 分かち書きして保存するクラス
class Wakati:
    def __init__(self,
                file_path,
                out_path=None,
                patterns=[r'<.*>']):

        self.file_path = file_path
        self.out_path = out_path
        self.patterns = patterns
        self.splited_text = []
        self.tagger = MeCab.Tagger('-Owakati')

    def wakati(self):
        # split the text
        for line in Readtext(self.file_path):
            for pattern in self.patterns:
                line = unicodedata.normalize('NFKC', line)
                line = re.sub(pattern, '', line)
            node = self.tagger.parseToNode(line).next
            splited_line = []
            while node.surface:
                splited_line.append(node.surface)
                node = node.next
            self.splited_text.append(splited_line)

    def tolist(self):
        if not self.splited_text:
            self.wakati()
        return self.splited_text

    def output(self):
        # output
        if not self.splited_text:
            self.wakati()
        if self.out_path == None:
            filename, _ = os.path.splitext(self.file_path)
            self.out_path = filename + '_wakati.txt'
        with open(self.out_path, 'w', encoding='utf-8') as f:
            for line in self.splited_text:
                f.write(' '.join(line))

# 分かち書きを行うメイン関数
def wakati(file_path, out_path=None):
    print('wakati {} start!!'.format(file_path), end=' --> ')
    Wakati(file_path, out_path).output()
    print('finished!!')

# 全サンプルデータからランダムに50個を選ぶ
# 乱数シードの設定や選ぶ文書の数は自由に決めてもいい
path = glob.glob('sample_text/*/*')
sample = random.sample(path, 50)

# 選んだ文書それぞれに対して、分かち書きして、結果を保存する
out_dir = 'tokenized_text'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

for index, file in enumerate(sample, 1):
    print(f'{index}/total:{len(sample)}')
    with open(file) as f:
        wakati(file, out_dir+os.sep+''.join(file.rsplit(os.sep,2)[-2:])+'.txt')


# 分かち書きの結果をまとめて、tokenized_data.txtに保存する
tokenized_text = glob.glob(f'{out_dir}/*')
data = ''
for i in tokenized_text:
    with open(i, encoding='utf-8') as f:
        data += f.read()

with open('tokenized_data.txt', 'w', encoding='utf-8') as f:
    f.write(data)
print(f'tokenized data saved!')
