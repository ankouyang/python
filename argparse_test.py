import argparse

parser = argparse.ArgumentParser(description="用来演示参数处理的")
parser.add_argument("-number", type=int, help="输入一个数字", default=1)
args = parser.parse_args()
print(f"你输入的参数为{args.number}")
