#!/usr/bin/env python3
# coding: utf-8

import re
import argparse
import difflib

parser = argparse.ArgumentParser()

# parser.add_argument(    "STUDENT_FILE", help="担当する学生の学籍番号(\d{10})を改行区切りのtxtファイルでまとめたもの")
parser.add_argument("ANSWER_FILE", help="正答例")
parser.add_argument("NOTE_FILE", help="ログファイル。")
parser.add_argument("-l", "--log", action="store_true", help="ノートファイルを表示する")
parser.add_argument("-o", "--output", type=str, default=None,
                    help="抽出したファイルを指定したファイルパスに保存する。")


class Checker(object):

    def __init__(self, ANSWER_FILE, NOTE_FILE, pattern="(?=\d{2}10370\d{3})"):
        with open(NOTE_FILE) as f:
            self.note_str = f.read()
        with open(ANSWER_FILE) as f:
            self.answer = f.read()
        self.pattern = pattern
        self.logs = {}
        self.trans = str.maketrans({
            "：": ":",
            "、": ",",
            "，": ",",
            "。": ".",
            "．": ".",
            "　": "",
            "”": "\"",
            "＞": ">",
            "＜": "<",
            "０": "0",
            "１": "1",
            "＼": "\\",
            "ー": "-",
            "（": "(",
            "）": ")",
            "＝": "=",
            "！": "!",
            "〜": "~",
            "＠": "@",
            "＃": "#",
            "＄": "$",
            "％": "%",
            "＆": "&",
            "＾": "^",
            "＊": "*",
            "＋": "+",
            "｜": "|",
            "｛": "{",
            "｝": "}",
            "；": ";",
            "？": "?",
            "／": "/",
        })

    def translate(self, input1):
        return input1.strip().translate(self.trans).replace(" ", "").replace("\t", "")

    def reformat(self, input_str):
        input_str = input_str.strip().translate(self.trans)
        spliter = [
            "\n",
            "\r\n",
            " ",
            "　",
            "\t"
        ]
        p = "|".join(spliter)
        return re.sub(p, "", input_str)

    def diff(self, i1, i2):
        d = difflib.Differ()
        diff = d.compare(self.translate(i1).split(
            "\n"), self.translate(i2).split("\n"))
        return "\n".join(diff)

    def load(self):
        for s in re.split(self.pattern, self.note_str):
            if not s:
                continue
            self.logs[s[:10]] = s[10:]

    def run(self):
        f_answer = self.reformat(self.answer)
        for n in self.logs.keys():
            if f_answer not in self.reformat(self.logs[n]):
                print("{}: NG".format(n))
                print(self.diff(self.answer, self.logs[n]).strip())
            else:
                print("{}: {}".format(n, "OK"))


def main():
    args = parser.parse_args()
    obj = Checker(args.ANSWER_FILE, args.NOTE_FILE)
    obj.load()
    obj.run()


if __name__ == "__main__":
    main()
