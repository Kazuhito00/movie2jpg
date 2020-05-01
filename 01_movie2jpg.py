#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
[summary]
  Webカメラ、動画の各フレームを連番jpgとして保存する
[description]
  -
"""

import os
import argparse
import time
from distutils.util import strtobool

import cv2 as cv


def get_args():
    """
    [summary]
        引数解析
    Parameters
    ----------
    None
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--filepath", help='camera device number or movie path', default=0)
    parser.add_argument(
        "--resize_rate", help='resize rate', type=float, default=1.0)
    parser.add_argument("--cwidth", help='capture width', type=int)
    parser.add_argument("--cheight", help='capture height', type=int)
    parser.add_argument(
        "--display", help='display imshow', type=strtobool, default=1)
    parser.add_argument("--fps", help='capture fps', type=int, default=30)

    args = parser.parse_args()

    return args


def main():
    """
    [summary]
        main()
    Parameters
    ----------
    None
    """
    # 引数解析 #################################################################
    args = get_args()
    filepath = args.filepath
    resize_rate = args.resize_rate
    is_display = args.display
    fps = args.fps

    # カメラ or 動画準備 #######################################################
    cap = cv.VideoCapture(filepath)
    if args.cwidth is not None:
        cap.set(cv.CAP_PROP_FRAME_WIDTH, args.cwidth)
    if args.cheight is not None:
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, args.cheight)

    # 保存先準備 ###############################################################
    path_save_image = os.path.join('jpg')
    os.makedirs(path_save_image, exist_ok=True)

    # 画像ファイル名用番号
    capture_count = len(os.listdir(path_save_image))

    while True:
        start_time = time.time()

        # フレーム取得 #########################################################
        ret, frame = cap.read()
        if not ret:
            break
        frame_h, frame_w = frame.shape[:2]
        resize_frame = cv.resize(
            frame, (int(frame_w * resize_rate), int(frame_h * resize_rate)))

        # jpg画像書き込み ######################################################
        path_image_file = os.path.join(path_save_image,
                                       '{:06}.jpg'.format(capture_count))
        cv.imwrite(path_image_file, resize_frame)
        # print(path_image_file)

        capture_count += 1

        # 書き込み画像描画 ######################################################
        if is_display == 1:
            cv.imshow('movie2jpg', resize_frame)

            # FPS調整 ##########################################################
            elapsed_time = time.time() - start_time
            sleep_time = int((1000 / fps) - (elapsed_time * 1000))
            if sleep_time <= 0:
                sleep_time = 1

            # キー入力(ESC:プログラム終了) ######################################
            key = cv.waitKey(sleep_time)
            if key == 27:  # ESC
                break


if __name__ == '__main__':
    main()