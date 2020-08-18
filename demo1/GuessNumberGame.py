import sys

number = int(input("请输入谜底数字（1-9）："))
print("")
print("谜底已设置，游戏开始")
print("----------------------------------")
guess = -1
# 3次机会
chance = 3
while chance > 0:

    guess = int(input("请输入猜测的数字："))

    if guess == number:
        print("恭喜您，猜对了！")
        sys.exit(0)
    elif guess < number:
        print("真遗憾，小了点。。。")
    else:
        print("真遗憾：大了点。。。")

    chance -= 1

print("很遗憾，你出局了")
