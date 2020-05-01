# movie2jpg
movie2jpgはOpenCVを用いて、Webカメラ、動画の画像を連番jpgに保存するプログラムです。<br>
また、jpg2movieで連番jpgを動画として保存できます。

# Requirement
* OpenCV 3.4.2(or later)

# Installation
ディレクトリを丸ごとコピーして実行してください。

# Usage
サンプルの実行方法は以下です。

```bash
python 01_movie2jpg.py
```
以下のコマンドラインオプションがあります。<br>
--filepath：動画のファイルパス or Webカメラのデバイスナンバー<br>
--resize_rate：jpg保存時の画像サイズ比率（デフォルトは1.0倍）<br>
--cwidth：Webカメラのキャプチャ幅<br>
--cheight：Webカメラのキャプチャ高さ<br>
--display：キャプチャしている画像をGUI表示するか否か（デフォルトはTrue）<br>
--fps：WebカメラキャプチャのFPS<br>

```bash
python 02_jpg2movie.py
```
以下のコマンドラインオプションがあります。<br>
--filepath：連番jpgの格納パス（デフォルトは'jpg'）<br>
--resize_rate：動画保存時の画像サイズ比率（デフォルトは1.0倍）<br>
--display：キャプチャしている画像をGUI表示するか否か（False）<br>
--fps：保存動画のFPS<br>
--fourcc：動画の保存形式（デフォルトは'mp4v'）

```bash
python 03_rename_serial_number.py
```
以下のコマンドラインオプションがあります。<br>
--folderpath：連番jpgの格納パス（デフォルトは'jpg'）<br>


# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
movie2jpg is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
