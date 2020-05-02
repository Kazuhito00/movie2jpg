# movie2jpg
movie2jpgはOpenCVを用いて、Webカメラ、動画の画像を連番jpgに保存するプログラムです。<br>
また、jpg2movieで連番jpgを動画として保存できます。

# Requirement
* OpenCV 3.4.2(or later)

# Installation
ディレクトリを丸ごとコピーして実行してください。

# Usage
### Webカメラから連番jpgを保存
以下を実行すると「jpg」フォルダを作成し、フォルダ内に連番jpgを保存します<br>
「jpg」フォルダが既に存在する場合は、既存のファイルは残したまま、連番jpgを保存します
```bash
python 01_movie2jpg.py --filepath=0 --cwidth=1280 --cheight=720 -fps=30
```
--filepath：動画のファイルパス or Webカメラのデバイスナンバー<br>
--resize_rate：jpg保存時の画像サイズ比率（デフォルトは1.0倍）<br>
--cwidth：Webカメラのキャプチャ幅<br>
--cheight：Webカメラのキャプチャ高さ<br>
--display：キャプチャしている画像をGUI表示するか否か（デフォルトはTrue）<br>
--fps：WebカメラキャプチャのFPS<br>

### 動画から連番jpgを保存
```bash
python 01_movie2jpg.py --filepath='sample.mp4' --display=False
```
--filepath：動画のファイルパス or Webカメラのデバイスナンバー<br>
--resize_rate：jpg保存時の画像サイズ比率（デフォルトは1.0倍）<br>
--display：キャプチャしている画像をGUI表示するか否か（デフォルトはTrue）<br>
--skip：動画フレーム取得の際に間引いて取得する枚数（デフォルトは0）<br>
　　　　例）skip=2を指定した場合は、1、4、7フレーム目……を保存する

### 連番jpgから動画を保存
以下を実行すると、指定フォルダの連番jpgから動画を作成し「movie」フォルダに保存します<br>
※連番jpgは000000.jpgから始まる必要があります
```bash
python 02_jpg2movie.py --filepath='jpg' --fps=10
```
--filepath：連番jpgの格納パス（デフォルトは'jpg'）<br>
--resize_rate：動画保存時の画像サイズ比率（デフォルトは1.0倍）<br>
--display：キャプチャしている画像をGUI表示するか否か（False）<br>
--fps：保存動画のFPS（デフォルトは29.97）<br>
--fourcc：動画の保存形式（デフォルトは'mp4v'）

### フォルダ内のファイルを000000.jpgから始まる連番にリネーム
```bash
python 03_rename_serial_number.py --folderpath='jpg
```
--folderpath：連番jpgの格納パス（デフォルトは'jpg'）<br>


# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
movie2jpg is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
