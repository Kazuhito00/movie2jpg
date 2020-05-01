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
python hsv_mask_extracter.py
```
以下のコマンドラインオプションがあります。

--device：OpenCVのVideoCapture()で開くカメラデバイスorファイル

--width：カメラキャプチャサイズ(幅)

--height：カメラキャプチャサイズ(高さ)

--waittime：処理フレーム間スリープ時間

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
movie2jpg is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
