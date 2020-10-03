#!/usr/bin/env python3
# coding: utf-8

import re
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "STUDENT_FILE", help="担当する学生の学籍番号(\d{10})を改行区切りのtxtファイルでまとめたもの")
parser.add_argument("NOTE_FILE", help="ノートチェックファイル。学籍番号を元に分割する。")
parser.add_argument("-l", "--log", action="store_true", help="ノートファイルを表示する")
parser.add_argument("-o", "--output", type=str, default=None,
                    help="抽出したファイルを指定したファイルパスに保存する。")


class Extractor():

    def __init__(self, STUDENT_FILE, NOTE_FILE, pattern="(?=\d{2}10370\d{3})"):
        with open(STUDENT_FILE, "r") as f:
            self.students = [s.replace("\n", "") for s in f.readlines()]
        with open(NOTE_FILE, "r") as f:
            self.note_str = f.read()
        self.pattern = pattern

    def load(self):
        self.logs = {}
        for s in re.split(self.pattern, self.note_str):
            if s[:10] in self.students:
                self.logs[s[:10]] = s

    def print_students(self):
        for n in self.logs.keys():
            print(n)

    def print_logs(self):
        for k, v in self.logs.keys():
            print(v)

    def output(self, filename):
        with open(filename, "w") as f:
            f.writelines(self.logs.values())


def main():
    args = parser.parse_args()
    obj = Extractor(args.STUDENT_FILE, args.NOTE_FILE)
    obj.load()
    obj.print_students()
    if args.log:
        obj.print_logs()
    if args.output is not None:
        obj.output(args.output)
