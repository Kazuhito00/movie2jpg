#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
[summary]
  指定フォルダのファイルを連番ファイルにリネームする
[description]
  -
"""

import os
import argparse
import glob


def get_args():
    """
    [summary]
        引数解析
    Parameters
    ----------
    None
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("--folderpath", help='jpg path', default='jpg')
    parser.add_argument("--start", type=int, default=0)

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
    folderpath = args.folderpath
    start_num = args.start

    folderpath = os.path.join(os.getcwd(), folderpath)

    # 引数解析 #################################################################
    files = glob.glob(os.path.join(folderpath, '*'))
    for filepath in files:
        os.rename(filepath,
                  os.path.join(folderpath, '_' + os.path.basename(filepath)))

    files = glob.glob(os.path.join(folderpath, '*'))
    for i, filepath in enumerate(files):
        os.rename(
            filepath,
            os.path.join(
                folderpath, '{:06}'.format(i + start_num) +
                os.path.splitext(filepath)[-1]))


if __name__ == '__main__':
    main()
