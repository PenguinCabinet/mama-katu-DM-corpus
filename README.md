# ママ活DMコーパス

## ダウンロード
<a href="https://raw.githubusercontent.com/PenguinCabinet/mama-katu-DM-corpus/main/Mama_katu_DM_corpus.txt" download="Mama_katu_DM_corpus.txt">Mama_katu_DM_corpus.txt</a>

## 概要
ママ活の勧誘DMを集めてコーパスにしたものです

## 仕様
* 文字コードはUTF-8、改行コードはLFです
* 一行に一つのママ活DMのテキストです
* 改行は「\_\_br\_\_」という記号に変換しています
* 送り先ユーザー名は「\_\_to\_user\_\_」という記号に変換しています
* 送り元ユーザー名は「\_\_from\_user\_\_」という記号に変換しています

## 追加方法
1. in_conv.txtに追加するママ活DMの内容を書き書き(一度に一つずつしか追加できません)
2. python3 conv.pyを実行
3. Mama_katu_DM_corpus.txtに追加されている

※conv.pyは「\_\_to\_user\_\_」と「\_\_from\_user\_\_」に置き換える匿名化にはまだ対応できていません。手動で置換をおこなってください
## 注釈
本リポジトリはママ活を推奨するものでもありません。また、そのものをママ活を論じるものではありません。   
また本リポジトリは[LICENSE](./LICENSE)に従い、無保証です。
