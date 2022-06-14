# 第１回
## 消えたアルファベットを探すゲーム
### 遊び方
* コマンドラインでalphabet.pyを実行すると、標準出力に問題が表示される.
* 標準入力から解答する.
* 最初に欠損文字数を解答する.
* 正解なら具体的な文字を入力する.
* 不正解ならもう一度出題される
### プログラム内の解説
* main関数：プログラムの全体を担っている.
* quiz関数：ランダムにアルファベットを抽出し、欠損文字もランダムに決めている.
* ans関数：解答の正解をチェックして、結果を出力.
* pro_time関数：プログラムの実行時間を計測している.