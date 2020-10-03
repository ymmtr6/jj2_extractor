#!/usr/bin/env python3
# coding: utf-8

import re
import argparse
import difflib

parser = argparse.ArgumentParser()

# parser.add_argument(    "STUDENT_FILE", help="担当する学生の学籍番号(\d{10})を改行区切りのtxtファイルでまとめたもの")
parser.add_argument("AMSWER_FILE", help="正答例")
parser.add_argument("NOTE_FILE", help="ログファイル。")
parser.add_argument("-l", "--log", action="store_true", help="ノートファイルを表示する")
parser.add_argument("-o", "--output", type=str, default=None,
                    help="抽出したファイルを指定したファイルパスに保存する。")

args = parser.parse_args()

with open(args.NOTE_FILE) as f:
    note_str = f.read()

with open(args.AMSWER_FILE) as f:
    answer = f.read()

# with open(args.STUDENT_FILE) as f:
#    students = [s.replace("\n", "") for s in f.readlines()]

pattern = "(?=\d{2}10370\d{3})"


def reformat(input_str):
    #
    spreaters = [
        "\n",
        " ",
        "　",
        "、",
        "，",
        "：",
        ":",
        ","  # これは過保護
    ]
    pattern = "|".join(spreaters)
    # return input_str.replace("({})".format(pattern), "")
    return re.sub(pattern, "", input_str)


def diff(i1, i2):
    d = difflib.Differ()
    diff = d.compare(i1.split("\n"), i2.split("\n"))
    return "\n".join(diff)


logs = {}
for s in re.split(pattern, note_str):
    if not s:
        continue
    logs[s[:10]] = s[10:]

f_answer = reformat(answer)
for n in logs.keys():
    if f_answer not in reformat(logs[n]):
        print("{}: NG".format(n))
        print(diff(logs[n], answer))
    else:
        print("{}: {}".format(n, "OK"))

print(f_answer)

if args.log:
    print("notes: ")
    for k, v in logs.items():
        print(v)

# if args.output is not None:
#    with open(args.output, "w") as f:
#       f.writelines(logs.values())
