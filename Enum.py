from enum import Enum
import sys
class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3

def act_shingou(color):
    if color == 1:
        print("とまれ")
    elif color == 2:
        print("すすめ")
    elif color == 3:
        print("ちゅうい")
    else :
        raise Exception("信号機の色に対応していません")

# shingou = Shingou(1)
# if shingou is Shingou.RED:
#     elif shingou is Shingou.BLUE:
# print(Shingou.name)
# print(Shingou.value)
# for data in Shingou:
#     print(data.value)

if __name__ == "__main__":
    args = sys.argv
    act_shingou(int(args[1]))