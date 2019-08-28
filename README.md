# 日本語wikipediaによるword2vec

このrepoは、日本語wikipediaの一部本文のデータを使って,word2vecを試すコードを提供する。

repoの構成は以下のようである。

```
├ README.md .. 説明
│
├ sample_text .. wikipediaの一部本文データ
│
├ create_tokenized_data.py .. sample_textからランダムサンプリングして、分かち書き済みのデータを生成
│
├ jp_word2vec.ipynb ..Google Colabでword2vecの学習を行う
│
├ train_word2vec.py ..ローカルで学習するスクリプト
│
├ test.py ..Google Colabで学習済みのWord2vecモデルをローカルでテストする

```

## Requirement

- MeCab
- Python3.6+ (miniconda/anaconda recommended!)
- Google アカウント


## Google Colabの使い方
Google ColabはGPU付きのネット上の計算環境であり、Googleアカウントを持っていれば、誰でも無料で使える

1. Google ColabのJP公式イントロページへアクセスして、簡単な説明を読む

https://colab.research.google.com/notebooks/welcome.ipynb?hl=ja

2. `ファイル/ノートブックをアップロード`で、ローカルにダウンロードして本repoの`jp_word2vec.ipynb`を開く

あるいは、github上で、`jp_word2vec.ipynb`をクリックして、`Open in Colab`というアイコンをクリックする


## Usage

1. このrepoをローカルにcloneまたはdownloadする

```
git clone https://github.com/irasin/jp_w2v
cd jp_w2v
```

2. `create_tokenized_data.py`を実行し、分かち書き済みのデータを生成する。このスクリプトは、`sample_text`にある100個のファイルからランダムに50個を選び、それぞれに対して、分かち書きを行なって、最後に結果をまとめて、`tokenized_data.txt`に保存する。

```bash
python create_tokenized_data.py
```

3. 分かち書き済みのデータ`tokenized_data.txt`を自分のGoogle Driveにアップロードする

4. Google Colabを開いて、`jp_word2vec.ipynb`を開く。

5. Google Driveに保存された`word2vec.model`をローカルにダウンロードして、類似語の計算などを行う前、先に`gensim`を入れる必要がある。

```
pip install gensim
```
### Google Colabを使用する際の注意点

1. `ランタイム/ランタイムの変更`でGPUの使用を確保する

2. `!pip install -U chainer`を実行する際に、`typing`のエラーとランタイム再起動の要求が出たら、`ランタイム/ランタイムを再起動`を選択して、ノートブックを再起動する

3. `from google.colab import drive
   drive.mount('/content/drive')`

    はGoogle Driveのアクセス権限を与えるコードである。実行後、青いリンクを押して、確認コードをコピーして、ノートブックのブランクに貼って、確認する。後ほど、学習済みの結果をGoogle Driveに保存する際に、似たような認証過程がある。

4. 学習ずみの`word2vec.model`は自分のGoogle Driveに保存されるため、ローカルにダウンロードして、`test.py`を実行すれば、色々試せる。
