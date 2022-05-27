# ママ活勧誘DMコーパス

## ダウンロード
<a href="https://raw.githubusercontent.com/PenguinCabinet/mama-katu-DM-corpus/main/data.txt" download="Mama_katu_DM_corpus.txt">Mama_katu_DM_corpus.txt</a>

## 概要
ママ活の勧誘のDMを集めてコーパスにしたものです。

## 仕様
* 一行に一つのママ活DMのテキストです
* 改行は「__BR__」という記号に変換しています
* 送り先ユーザー名は「__TOUSER__」という記号に変換しています
* 送り元ユーザー名は「__FROMUSER__」という記号に変換しています

## 追加方法
1. in_conv.txtにママ活DMの内容を書き書き
2. python conv.pyを実行
3. Mama_katu_DM_corpus.txtに追加されている
