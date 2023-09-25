#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return app.send_static_file("index.html")

# rock、paper 或 scissor
rules = input((
    "游戏规则:\n"
    "1: 石头 2: 剪刀 3: 布\n"
    "石头赢剪刀（损坏剪刀）。\n"
    "剪⼑赢布（剪断布）。\n"
    "布赢⽯头（包住⽯头）。\n"
    "小游戏为多人游戏，计算机扮演你的对手的角色，并从元素列表中选择一个随机元素\n"
    "键入Y|y开始:\n"
))
while rules.lower() != 'y':
    rules = input("键入Y|y开始:\n")

n = 1
err = ''
score = 0
while True:
    uk = input((
        f"{err} \n" if err else ""
        f"轮次{n}: \n"
        "1: 石头 2: 剪刀 3: 布\n"
        "开始:\n"
        ))
    uk = int(uk)
    if uk not in [1,2,3]:
        err = '输入有误,重新输入:'
        continue
    rk = 2
    w = '平局' if uk == rk else ('用户' if uk < rk else "电脑")
    w = '用户' if uk == 3 and rk == 1  else w
    w = '电脑' if rk == 3 and uk == 1  else w
    score += 10 if w == '用户' else 0
    print(f"用户输入: {uk}; 系统输入: {rk}\n")
    print(f"第{n}轮 win: {w} {score}\n")
    print("-----------------------------------\n")
    err = ""
    n += 1
