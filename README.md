# robosys_2020_ROS

# robosys2020 課題２
### 動作環境
今回の課題で使用した環境は以下の表に示す。
|||
|:--:|:--:|
|ROS|ROS melodic|
|OS| Ubuntu18.04|

## 課題2の内容
数字０と１と２にそれぞれにグー、チョキ、パーを割り当てじゃんけんをし、勝敗を決める。

## インストール手順
### gitcloneでもってくる
```bash:
$git clone https://github.com/pohsho/robosys_2020_-_ros.git
$cd mypkg/scripts
```

# 動作方法
動作＜じゃんけん＞
１つめの端末でroscoreを立ち上げる
```bash:
$roscore
```
２つめの端末で以下のコマンド打つ
```bash:
$rosrun mypkg player1.py
```
３つめの端末で以下のコマンドでを打ち込み、グーとチョキとパーのどれかを選択する。
```bash:
$rosrun mypkg player2.py
```
## アピールポイント
車の運転手や荷物持ちなどのじゃんけんで決める際に、使用することで後出しなどの不正行為を防ぐことができる点である。
## ライセンス
BSD 3-Clause License
