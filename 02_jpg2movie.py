#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
[summary]
  連番のjpg画像を動画として保存する
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

    parser.add_argument("--filepath", help='jpg path', default='jpg')
    parser.add_argument(
        "--resize_rate", help='resize rate', type=float, default=1.0)
    parser.add_argument(
        "--display", help='display imshow', type=strtobool, default=0)
    parser.add_argument("--fps", help='capture fps', type=float, default=29.97)
    parser.add_argument("--fourcc", help='fourcc', default='mp4v')

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
    fourcc = args.fourcc

    # ファイル読み込み準備 ######################################################
    cap = cv.VideoCapture(os.path.join(filepath, '%06d.jpg'))

    # 保存先準備 ###############################################################
    path_save_movie = os.path.join('movie')
    os.makedirs(path_save_movie, exist_ok=True)

    # ファイル名用番号
    capture_count = len(os.listdir(path_save_movie))

    # ビデオライター準備 ########################################################
    ret, frame = cap.read()
    if not ret:
        exit()
    frame_h, frame_w = frame.shape[:2]

    writer_fourcc = cv.VideoWriter_fourcc(*fourcc)
    writer = cv.VideoWriter(
        os.path.join(path_save_movie,
                     '{:06}.mp4'.format(capture_count)), writer_fourcc, fps,
        (int(frame_w * resize_rate), int(frame_h * resize_rate)))

    # 1フレーム目書き込み #######################################################
    resize_frame = cv.resize(
        frame, (int(frame_w * resize_rate), int(frame_h * resize_rate)))
    writer.write(resize_frame)

    while True:
        start_time = time.time()

        # フレーム取得 #########################################################
        ret, frame = cap.read()
        if not ret:
            break
        frame_h, frame_w = frame.shape[:2]
        resize_frame = cv.resize(
            frame, (int(frame_w * resize_rate), int(frame_h * resize_rate)))

        # フレーム書き込み #######################################################
        writer.write(resize_frame)

        if is_display == 1:
            cv.imshow('jpg2movie', resize_frame)

            # FPS調整 ###########################################################
            elapsed_time = time.time() - start_time
            sleep_time = int((1000 / fps) - (elapsed_time * 1000))
            if sleep_time <= 0:
                sleep_time = 1

            # キー入力(ESC:プログラム終了) #######################################
            key = cv.waitKey(sleep_time)
            if key == 27:  # ESC
                break

    writer.release()
    cap.release()


if __name__ == '__main__':
    main()
